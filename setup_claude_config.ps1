# Script per configurare Claude Desktop con il server ISTAT MCP
# Usare PRIMA di avviare Claude Desktop

$configPath = "$env:APPDATA\Claude\claude_desktop_config.json"

Write-Host "`nVerifica se Claude Desktop e' in esecuzione..." -ForegroundColor Cyan
$claudeProcess = Get-Process "Claude" -ErrorAction SilentlyContinue
if ($claudeProcess) {
    Write-Host "ERRORE: Claude Desktop e' attualmente in esecuzione (PID: $($claudeProcess.Id))" -ForegroundColor Red
    Write-Host "Chiudilo completamente e riesegui questo script." -ForegroundColor Yellow
    exit 1
}

Write-Host "OK: Claude Desktop non e' in esecuzione" -ForegroundColor Green

# Backup del file esistente
if (Test-Path $configPath) {
    $backupPath = "$configPath.backup_$(Get-Date -Format 'yyyyMMdd_HHmmss')"
    Copy-Item $configPath $backupPath -Force
    Write-Host "OK: Backup creato: $backupPath" -ForegroundColor Green
}

# Configura il file JSON
$config = @'
{
  "mcpServers": {
    "istat": {
      "command": "C:\\Users\\patru\\Dropbox\\mcp\\istat_mcp_server\\.venv\\Scripts\\python.exe",
      "args": [
        "-m",
        "istat_mcp_server"
      ],
      "cwd": "C:\\Users\\patru\\Dropbox\\mcp\\istat_mcp_server"
    }
  },
  "preferences": {
    "coworkWebSearchEnabled": true,
    "coworkScheduledTasksEnabled": true,
    "ccdScheduledTasksEnabled": true
  }
}
'@

# Salva il file
[System.IO.File]::WriteAllText($configPath, $config, [System.Text.Encoding]::UTF8)

Write-Host "OK: Configurazione salvata in: $configPath" -ForegroundColor Green

# Verifica
Write-Host "`nContenuto del file di configurazione:" -ForegroundColor Cyan
Get-Content $configPath | Write-Host

Write-Host "`nConfigurazione completata!" -ForegroundColor Green
Write-Host "`nProssimi passi:" -ForegroundColor Cyan
Write-Host "1. NON avviare ancora Claude Desktop" -ForegroundColor Yellow
Write-Host "2. Verifica che la configurazione sopra sia corretta" -ForegroundColor Yellow
Write-Host "3. Avvia Claude Desktop" -ForegroundColor Yellow
Write-Host "4. Controlla il log: $env:APPDATA\Claude\logs\main.log" -ForegroundColor Yellow
Write-Host "5. Cerca nel log: MCP Server connection requested for: istat" -ForegroundColor Yellow
