param(
    [string]$SourcePath = "C:\Work\crucea\poienel.ro",
    [string]$FtpServer = "ftp.poienel.ro",
    [string]$FtpUser = "claude@poienel.ro",
    [string]$FtpPass = "MJ2ilH4g4FCW",
    [string]$FtpPath = "/public_html"
)

function Create-FtpDirectory {
    param(
        [string]$FtpPath
    )

    try {
        $uri = "ftp://$FtpServer$FtpPath"
        $ftpRequest = [System.Net.FtpWebRequest]::Create($uri)
        $ftpRequest.Method = [System.Net.WebRequestMethods+Ftp]::MakeDirectory
        $ftpRequest.Credentials = New-Object System.Net.NetworkCredential($FtpUser, $FtpPass)
        $ftpRequest.UsePassive = $true

        $response = $ftpRequest.GetResponse()
        $response.Close()
    }
    catch {
        # Directory might already exist, ignore error
    }
}

function Upload-FtpFolder {
    param(
        [string]$LocalPath,
        [string]$RemotePath
    )

    Write-Host "Uploading to FTP: $RemotePath" -ForegroundColor Cyan

    $files = Get-ChildItem -Path $LocalPath -Recurse -File |
        Where-Object { $_.Name -ne "sync-to-ftp.ps1" }

    foreach ($file in $files) {
        $relativePath = $file.FullName.Substring($LocalPath.Length).TrimStart('\')
        $ftpTargetPath = "$RemotePath/$($relativePath.Replace('\', '/'))"

        # Create subdirectories if needed
        $ftpDir = Split-Path -Parent $ftpTargetPath
        if ($ftpDir -ne $RemotePath) {
            Create-FtpDirectory -FtpPath $ftpDir
        }

        try {
            $uri = "ftp://$FtpServer$ftpTargetPath"
            $ftpRequest = [System.Net.FtpWebRequest]::Create($uri)
            $ftpRequest.Method = [System.Net.WebRequestMethods+Ftp]::UploadFile
            $ftpRequest.Credentials = New-Object System.Net.NetworkCredential($FtpUser, $FtpPass)
            $ftpRequest.UseBinary = $true
            $ftpRequest.UsePassive = $true

            $fileStream = [System.IO.File]::OpenRead($file.FullName)
            $ftpStream = $ftpRequest.GetRequestStream()
            $fileStream.CopyTo($ftpStream)
            $ftpStream.Close()
            $fileStream.Close()

            $response = $ftpRequest.GetResponse()
            Write-Host "[OK] $relativePath" -ForegroundColor Green
            $response.Close()
        }
        catch {
            Write-Host "[ERROR] $relativePath - $($_.Exception.Message)" -ForegroundColor Red
        }
    }
}

Upload-FtpFolder -LocalPath $SourcePath -RemotePath $FtpPath
Write-Host "`n[DONE] Sync completed!" -ForegroundColor Green
