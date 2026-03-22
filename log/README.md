# Directory Log

Questa cartella contiene i file di log del server ISTAT MCP.

## File di log

- `istat_mcp_server.log` - Log principale del server con rotazione automatica (max 10MB per file)
- `istat_mcp_server.log.1` - Backup del file di log precedente
- `istat_mcp_server.log.2` - Backup più vecchio
- ... fino a `istat_mcp_server.log.5`

## Rotazione dei log

I log vengono automaticamente ruotati quando raggiungono 10MB. Il sistema mantiene gli ultimi 5 file di backup.

## Livello di log

Il livello di log predefinito è `INFO`. Per debug più dettagliato, modifica il file `.env`:

```bash
LOG_LEVEL=DEBUG
```

Livelli disponibili:
- `DEBUG` - Massimo dettaglio, include tutte le operazioni
- `INFO` - Informazioni standard sulle operazioni (default)
- `WARNING` - Solo avvisi e errori
- `ERROR` - Solo errori

## Contenuto dei log

I log includono:
- Inizializzazione del server
- Operazioni di cache (quando attivo il caching)
- Chiamate API all'ISTAT SDMX
- Errori e retry
- Chiamate ai tool MCP
- Path delle directory usate (cache, log)

## Debug della cache

Per verificare dove viene salvata la cache, cerca nel log:
```
Cache system initialized at: <path>
```

## Configurazione custom

Puoi specificare una directory custom per i log nel file `.env`:

```bash
LOG_DIR=/path/personalizzato/per/log
```

Se non specificato, usa la cartella `log` nella root del progetto.
