"""Esempio del formato di logging avanzato implementato.

FORMATO LOG PER MCP TOOL CALLS:
================================

Quando Claude chiama un tool, il log includerà:

================================================================================
MCP TOOL CALL: get_data
Arguments: {
  "id_dataflow": "183_1163_DF_DICA_ASIAULP_TERRIFDATA_4",
  "dimension_filters": {
    "FREQ": ["A"],
    "REF_AREA": ["IT"]
  },
  "start_period": "2023",
  "end_period": "2023"
}
→ HTTP GET: https://esploradati.istat.it/SDMXWS/rest/dataflow
← HTTP 200: 152340 bytes in 1.234s
→ HTTP GET: https://esploradati.istat.it/SDMXWS/rest/datastructure/DSI_12345
← HTTP 200: 45678 bytes in 0.567s
→ HTTP GET: https://esploradati.istat.it/SDMXWS/rest/data/183_1163_DF_DICA_ASIAULP_TERRIFDATA_4/A.IT../ALL/
  Query params: {'detail': 'full', 'startPeriod': '2023', 'endPeriod': '2023'}
← HTTP 200: 987654 bytes in 3.456s
TOOL SUCCESS: get_data
Execution time: 5.345s
Response size: 1000000 bytes
================================================================================


FORMATO LOG PER ERRORI:
=======================

In caso di errore:

================================================================================
MCP TOOL CALL: get_data
Arguments: {
  "id_dataflow": "INVALID_ID"
}
✗ HTTP ERROR 404 for https://esploradati.istat.it/SDMXWS/rest/data/INVALID_ID/ALL/
  Response: <?xml version="1.0" encoding="UTF-8"?><error>...</error>
TOOL ERROR: get_data
Error type: ApiError
Error message: HTTP error: 404
Execution time: 0.234s
Full traceback:
Traceback (most recent call last):
  ...
================================================================================


INFORMAZIONI TRACCIATE:
========================

Per ogni chiamata MCP tool:
✓ Nome del tool
✓ Parametri completi in formato JSON
✓ Tutte le chiamate HTTP effettuate (URL, parametri, tempo, dimensione risposta)
✓ Tempo totale di esecuzione
✓ Dimensione della risposta
✓ Errori dettagliati con traceback completo

Per ogni chiamata HTTP API:
✓ URL completo dell'endpoint
✓ Parametri query (se presenti)
✓ Status code HTTP
✓ Dimensione della risposta in bytes
✓ Tempo di esecuzione in secondi
✓ Errori di rete o HTTP con dettagli

SIMBOLI USATI:
==============
→ Chiamata HTTP in uscita
← Risposta HTTP ricevuta
✗ Errore HTTP o di rete
"""

if __name__ == '__main__':
    print(__doc__)
