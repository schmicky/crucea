param(
    [int]$Port = 8000,
    [string]$Path = "C:\Work\crucea\poienel.ro"
)

$listener = New-Object System.Net.HttpListener
$listener.Prefixes.Add("http://localhost:$Port/")
$listener.Start()

Write-Host "HTTP server started on http://localhost:$Port" -ForegroundColor Green
Write-Host "Serving files from: $Path" -ForegroundColor Cyan
Write-Host "Press Ctrl+C to stop`n" -ForegroundColor Yellow

try {
    while ($listener.IsListening) {
        $context = $listener.GetContext()
        $request = $context.Request
        $response = $context.Response

        $localPath = $request.Url.LocalPath
        if ($localPath -eq "/") { $localPath = "/index.html" }

        $filePath = Join-Path $Path $localPath.TrimStart("/").Replace("/", "\")

        if (-not (Test-Path $filePath)) {
            $response.StatusCode = 404
            $buffer = [Text.Encoding]::UTF8.GetBytes("404 Not Found")
            $response.ContentLength64 = $buffer.Length
            $response.OutputStream.Write($buffer, 0, $buffer.Length)
        } else {
            $file = Get-Item $filePath
            if ($file.PSIsContainer) {
                $filePath = Join-Path $filePath "index.html"
                if (-not (Test-Path $filePath)) {
                    $response.StatusCode = 404
                    $buffer = [Text.Encoding]::UTF8.GetBytes("404 Not Found")
                    $response.ContentLength64 = $buffer.Length
                    $response.OutputStream.Write($buffer, 0, $buffer.Length)
                } else {
                    $content = [IO.File]::ReadAllBytes($filePath)
                    $response.ContentType = "text/html; charset=utf-8"
                    $response.ContentLength64 = $content.Length
                    $response.OutputStream.Write($content, 0, $content.Length)
                }
            } else {
                $content = [IO.File]::ReadAllBytes($filePath)
                $ext = $file.Extension.ToLower()

                $contentTypes = @{
                    ".html" = "text/html; charset=utf-8"
                    ".css" = "text/css; charset=utf-8"
                    ".js" = "application/javascript; charset=utf-8"
                    ".json" = "application/json; charset=utf-8"
                    ".png" = "image/png"
                    ".jpg" = "image/jpeg"
                    ".jpeg" = "image/jpeg"
                    ".gif" = "image/gif"
                    ".svg" = "image/svg+xml"
                    ".ico" = "image/x-icon"
                    ".txt" = "text/plain; charset=utf-8"
                }

                $response.ContentType = $contentTypes[$ext] -or "application/octet-stream"
                $response.ContentLength64 = $content.Length
                $response.OutputStream.Write($content, 0, $content.Length)
            }
        }

        $response.OutputStream.Close()
    }
} finally {
    $listener.Close()
    Write-Host "`nServer stopped" -ForegroundColor Yellow
}
