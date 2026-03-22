#  Script per verificare la configurazione di Claude Desktop dopo l'avvio
# Eseguire DOPO aver avviato Claude Desktop

$configPath = "$env:APPDATA\Claude\claude_desktop_config.json"
$logPath = "$env:APPDATA\Claude\logs\main.log"

Write-Host "`n=== VERIFICA CONFIGURAZIONE CLAUDE DESKTOP ===" -ForegroundColor Cyan

# 1. Controlla se Claude e' in esecuzione
Write-Host "`n1. Verifica processo Claude..." -ForegroundColor Yellow
$claudeProcess = Get-Process "Claude" -ErrorAction SilentlyContinue
if ($claudeProcess) {
    Write-Host "   OK: Claude Desktop e' in esecuzione (PID: $($claudeProcess.Id))" -ForegroundColor Green
} else {
    Write-Host "   ATTENZIONE: Claude Desktop non sembra essere in esecuzione" -ForegroundColor Yellow
}

# 2. Controlla il contenuto del file di configurazione
Write-Host "`n2. Controllo file di configurazione..." -ForegroundColor Yellow
$config = Get-Content $configPath -Raw | ConvertFrom-Json

if ($config.PSObject.Properties.Name -contains "mcpServers") {
    Write-Host "   OK: Sezione 'mcpServers' presente nel file" -ForegroundColor Green
    
    if ($config.mcpServers.PSObject.Properties.Name -contains "istat") {
        Write-Host "   OK: Server 'istat' configurato" -ForegroundColor Green
        Write-Host "   - Command: $($config.mcpServers.istat.command)" -ForegroundColor Gray
        Write-Host "   - Args: $($config.mcpServers.istat.args -join ' ')" -ForegroundColor Gray
        Write-Host "   - Cwd: $($config.mcpServers.istat.cwd)" -ForegroundColor Gray
    } else {
        Write-Host "   ERRORE: Server 'istat' NON trovato nella configurazione!" -ForegroundColor Red
    }
} else {
    Write-Host "   ERRORE: Sezione 'mcpServers' NON presente nel file!" -ForegroundColor Red
    Write-Host "   Claude ha riscritto il file rimuovendo la configurazione MCP" -ForegroundColor Red
}

# 3. Controlla il log per vedere se il server e' stato avviato
Write-Host "`n3. Controllo log di Claude..." -ForegroundColor Yellow
if (Test-Path $logPath) {
    $logContent = Get-Content $logPath -Tail 200
    
    $mcpConnections = $logContent | Select-String -Pattern "MCP Server connection requested for" | Select-Object -Last 5
    if ($mcpConnections) {
        Write-Host "   Server MCP richiesti:" -ForegroundColor Cyan
        foreach ($conn in $mcpConnections) {
            Write-Host "   $conn" -ForegroundColor Gray
        }
        
        $istatConnection = $logContent | Select-String -Pattern "istat" -CaseSensitive
        if ($istatConnection) {
            Write-Host "`n   OK: Riferimenti al server 'istat' trovati nel log!" -ForegroundColor Green
        } else {
            Write-Host "`n   ATTENZIONE: Nessun riferimento al server 'istat' nel log" -ForegroundColor Yellow
        }
    } else {
        Write-Host "   Nessuna connessione MCP trovata nel log" -ForegroundColor Yellow
    }
    
    # Cerca eventuali errori
    $errors = $logContent | Select-String -Pattern "\[error\].*istat|\[error\].*mcp" -CaseSensitive | Select-Object -Last 3
    if ($errors) {
        Write-Host "`n   ERRORI trovati:" -ForegroundColor Red
        foreach ($err in $errors) {
            Write-Host "   $err" -ForegroundColor Red
        }
    }
} else {
    Write-Host "   ATTENZIONE: File di log non trovato" -ForegroundColor Yellow
}

Write-Host "`n=== FINE VERIFICA ===" -ForegroundColor Cyan

# 4. Mostra il contenuto completo del file di configurazione
Write-Host "`n4. Contenuto completo del file di configurazione:" -ForegroundColor Yellow
Get-Content $configPath

Write-Host "`n"
