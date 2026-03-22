# Script PowerShell per visualizzare e monitorare i log

## Visualizza gli ultimi 50 log
```powershell
Get-Content log\istat_mcp_server.log -Tail 50
```

## Segui i log in tempo reale (come tail -f)
```powershell
Get-Content log\istat_mcp_server.log -Wait -Tail 10
```

## Cerca errori nei log
```powershell
Select-String -Path log\istat_mcp_server.log -Pattern "ERROR"
```

## Cerca log di una specifica operazione
```powershell
Select-String -Path log\istat_mcp_server.log -Pattern "discover_dataflows"
```

## Filtra log per oggi
```powershell
$oggi = Get-Date -Format "yyyy-MM-dd"
Select-String -Path log\istat_mcp_server.log -Pattern $oggi
```

## Conta quanti errori ci sono
```powershell
(Select-String -Path log\istat_mcp_server.log -Pattern "ERROR").Count
```

## Visualizza solo i log di cache
```powershell
Select-String -Path log\istat_mcp_server.log -Pattern "cache"
```

## Trova tutti i file di log (inclusi i backup rotati)
```powershell
Get-ChildItem log\*.log*
```

## Dimensione totale dei log
```powershell
(Get-ChildItem log\*.log* | Measure-Object -Property Length -Sum).Sum / 1MB
```

## Elimina i vecchi log di backup (mantieni solo quello corrente)
```powershell
Remove-Item log\istat_mcp_server.log.* -Confirm
```
