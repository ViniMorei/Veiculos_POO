$exclude = @("venv", "veiculoPOO.zip")
$files = Get-ChildItem -Path . -Exclude $exclude
Compress-Archive -Path $files -DestinationPath "veiculoPOO.zip" -Force