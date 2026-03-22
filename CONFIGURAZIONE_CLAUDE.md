# Configurazione Claude Desktop - Server ISTAT MCP

## Problema
Claude Desktop **riscrive il file di configurazione** `claude_desktop_config.json` all'avvio, rimuovendo potenzialmente la sezione `mcpServers`.

## Soluzione

### Script Disponibili

#### 1. `setup_claude_config.ps1`
**Quando usarlo:** Prima di avviare Claude Desktop

**Funzione:**
- Verifica che Claude Desktop non sia in esecuzione
- Crea un backup del file di configurazione esistente
- Scrive la configurazione corretta con il server ISTAT MCP
- Mostra il contenuto del file configurato

**Come usarlo:**
```powershell
cd C:\Users\patru\Dropbox\mcp\istat_mcp_server
.\setup_claude_config.ps1
```

#### 2. `verify_claude_config.ps1`
**Quando usarlo:** Dopo aver avviato Claude Desktop

**Funzione:**
- Verifica se Claude Desktop è in esecuzione
- Controlla se la sezione `mcpServers` è ancora presente nel file
- Analizza il log per vedere se il server ISTAT è stato avviato
- Mostra eventuali errori nel log

**Come usarlo:**
```powershell
cd C:\Users\patru\Dropbox\mcp\istat_mcp_server
.\verify_claude_config.ps1
```

## Procedura Completa

### Step 1: Chiudi Claude Desktop
Assicurati che Claude Desktop sia completamente chiuso.

### Step 2: Configura il file
```powershell
.\setup_claude_config.ps1
```

### Step 3: Avvia Claude Desktop
Apri Claude Desktop normalmente.

### Step 4: Verifica la configurazione
Aspetta circa 10 secondi, poi esegui:
```powershell
.\verify_claude_config.ps1
```

### Step 5: Interpreta i risultati

**Caso A: Configurazione OK**
```
OK: Sezione 'mcpServers' presente nel file
OK: Server 'istat' configurato
OK: Riferimenti al server 'istat' trovati nel log!
```
✅ Il server ISTAT MCP è stato caricato correttamente!

**Caso B: Configurazione Persa**
```
ERRORE: Sezione 'mcpServers' NON presente nel file!
Claude ha riscritto il file rimuovendo la configurazione MCP
```
❌ Claude Desktop ha sovrascritto il file.

### Se la configurazione viene persa

Se Claude Desktop continua a sovrascrivere il file, ci sono 3 opzioni:

#### Opzione 1: Configurazione via Interfaccia
Controlla se Claude Desktop ha un'interfaccia grafica per aggiungere server MCP:
- Apri Claude Desktop
- Cerca nelle impostazioni/preferenze una sezione "MCP Servers" o "Plugins"
- Aggiungi il server ISTAT manualmente

#### Opzione 2: File Read-Only (temporaneo)
```powershell
# Dopo aver configurato il file
$configPath = "$env:APPDATA\Claude\claude_desktop_config.json"
Set-ItemProperty $configPath -Name IsReadOnly -Value $true

# Per rimuovere il read-only quando necessario
Set-ItemProperty $configPath -Name IsReadOnly -Value $false
```

⚠️ **Attenzione:** Questo potrebbe impedire a Claude Desktop di salvare altre impostazioni.

#### Opzione 3: Contatta il Supporto
Se il problema persiste, potrebbe essere un bug di Claude Desktop. Controlla:
- La versione di Claude Desktop installata
- Se ci sono aggiornamenti disponibili
- La documentazione ufficiale per configurare server MCP personalizzati

## Configurazione Corretta

Il file `claude_desktop_config.json` dovrebbe contenere:

```json
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
```

## File di Log

Claude Desktop scrive i log in:
```
%APPDATA%\Claude\logs\main.log
```

Per monitorare il log in tempo reale:
```powershell
Get-Content "$env:APPDATA\Claude\logs\main.log" -Wait -Tail 20
```

## Test Manuale del Server

Per verificare che il server ISTAT funzioni indipendentemente da Claude Desktop:
```powershell
cd C:\Users\patru\Dropbox\mcp\istat_mcp_server
.venv\Scripts\python.exe -m istat_mcp_server
```

Il server dovrebbe avviarsi e mostrare:
```
Starting ISTAT MCP Server on stdio
MCP server configured with 7 tools
```

Premi `Ctrl+C` per terminare il test.
