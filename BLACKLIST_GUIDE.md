# Dataflow Blacklist - Usage Guide

## Overview

The ISTAT MCP Server now supports a blacklist system to exclude specific dataflows from all queries. This is useful for filtering out deprecated, problematic, or internal datasets.

## Configuration

### Via Environment Variable

The blacklist is configured through the `DATAFLOW_BLACKLIST` environment variable. Add it to your `.env` file:

```bash
# Single dataflow
DATAFLOW_BLACKLIST=149_577_DF_DCSC_OROS_1_1

# Multiple dataflows (comma-separated)
DATAFLOW_BLACKLIST=149_577_DF_DCSC_OROS_1_1,22_315_DF_DCIS_POPORESBIL1_2,101_1015_DF_DCSP_COLTIVAZIONI_1

# With whitespace (automatically trimmed)
DATAFLOW_BLACKLIST= 149_577_DF_DCSC_OROS_1_1 , 22_315_DF_DCIS_POPORESBIL1_2 
```

### Example .env File

```bash
# API Configuration
API_BASE_URL=https://esploradati.istat.it/SDMXWS/rest
API_TIMEOUT_SECONDS=120
AVAILABLECONSTRAINT_TIMEOUT_SECONDS=180
API_MAX_RETRIES=3

# Cache Configuration
PERSISTENT_CACHE_DIR=./cache
MEMORY_CACHE_TTL_SECONDS=300
MAX_MEMORY_CACHE_ITEMS=512

# Dataflow Blacklist
DATAFLOW_BLACKLIST=149_577_DF_DCSC_OROS_1_1,22_315_DF_DCIS_POPORESBIL1_2

# Logging
LOG_LEVEL=INFO
LOG_DIR=./log
```

## Behavior

### In `discover_dataflows` Tool

Blacklisted dataflows are automatically filtered out from search results:

```
User: "Show me all dataflows about agriculture"

Claude: Searching... (blacklisted dataflows are hidden)
Results: 15 dataflows (excludes blacklisted ones)
```

### In `get_data` Tool

Attempts to fetch data from blacklisted dataflows will return an error:

```
User: "Get data from dataflow 149_577_DF_DCSC_OROS_1_1"

Claude: Error: "Dataflow 149_577_DF_DCSC_OROS_1_1 is blacklisted and cannot be accessed"
```

## Use Cases

### 1. Exclude Deprecated Dataflows

```bash
# Hide old versions of datasets
DATAFLOW_BLACKLIST=OLD_DATAFLOW_V1,DEPRECATED_DATASET
```

### 2. Filter Problematic Datasets

```bash
# Exclude dataflows that cause errors or have data quality issues
DATAFLOW_BLACKLIST=PROBLEMATIC_DF_1,ERROR_PRONE_DF_2
```

### 3. Hide Internal/Test Dataflows

```bash
# Hide internal or test datasets from production use
DATAFLOW_BLACKLIST=TEST_DF_123,INTERNAL_DATA_456
```

## Logging

When the server starts, it logs blacklist information:

```
2026-03-13 10:30:00,123 - INFO - Blacklist initialized with 2 dataflow(s): ['149_577_DF_DCSC_OROS_1_1', '22_315_DF_DCIS_POPORESBIL1_2']
```

When filtering occurs:

```
2026-03-13 10:30:05,456 - INFO - Filtered out 2 blacklisted dataflow(s)
```

When blocked access is attempted:

```
2026-03-13 10:30:10,789 - WARNING - Dataflow 149_577_DF_DCSC_OROS_1_1 is blacklisted and cannot be accessed
```

## Programmatic Usage

The blacklist can also be used programmatically in Python code:

```python
from istat_mcp_server.utils.blacklist import DataflowBlacklist

# Create blacklist
blacklist = DataflowBlacklist(['DF_123', 'DF_456'])

# Check if blacklisted
if blacklist.is_blacklisted('DF_123'):
    print("This dataflow is blacklisted")

# Filter dataflows
filtered = blacklist.filter_dataflows(all_dataflows)

# Add/remove dynamically
blacklist.add_to_blacklist('DF_789')
blacklist.remove_from_blacklist('DF_456')

# Get all blacklisted IDs
ids = blacklist.get_blacklisted_ids()
```

## Testing

The blacklist system includes comprehensive tests. Run them with:

```bash
pytest tests/test_blacklist.py -v
```

All tests:
- ✅ Empty blacklist initialization
- ✅ Blacklist with specific IDs
- ✅ Checking if dataflow is blacklisted
- ✅ Filtering dataflows list
- ✅ Loading from environment variable
- ✅ Whitespace handling
- ✅ Dynamic add/remove operations
- ✅ Immutable ID set returns

## Troubleshooting

### Blacklist Not Working

1. **Check environment variable is set:**
   ```bash
   echo $DATAFLOW_BLACKLIST  # Unix/Mac
   $env:DATAFLOW_BLACKLIST   # PowerShell
   ```

2. **Verify .env file is in correct location:**
   - Must be in project root directory
   - Named exactly `.env` (not `.env.txt`)

3. **Check server logs on startup:**
   - Look for "Blacklist initialized" message
   - Verify correct IDs are loaded

4. **Restart server after changing .env:**
   - Changes only take effect on server restart

### Dataflow Still Appears

- Verify the exact dataflow ID
- Check for typos in DATAFLOW_BLACKLIST
- IDs are case-sensitive
- No wildcards supported (must be exact match)

### Empty Results

- Too many dataflows blacklisted?
- Check if keywords are too restrictive combined with blacklist

## Implementation Details

### Files Modified

- `src/istat_mcp_server/utils/blacklist.py` - Core blacklist manager
- `src/istat_mcp_server/utils/__init__.py` - Export blacklist class
- `src/istat_mcp_server/server.py` - Initialize and pass blacklist
- `src/istat_mcp_server/tools/discover_dataflows.py` - Filter results
- `src/istat_mcp_server/tools/get_data.py` - Validate access
- `.env.example` - Configuration template
- `tests/test_blacklist.py` - Test suite

### Architecture

```
Server Startup
    ↓
Load DATAFLOW_BLACKLIST env var
    ↓
Initialize DataflowBlacklist
    ↓
Pass to tools
    ↓
┌─────────────────────┬─────────────────────┐
│ discover_dataflows  │ get_data           │
│ - Filter results    │ - Validate access   │
└─────────────────────┴─────────────────────┘
```

## Future Enhancements

Potential improvements for future versions:

- Pattern matching (e.g., `*_TEST_*` to exclude all test dataflows)
- Whitelist mode (only allow specific dataflows)
- Per-user blacklists
- UI for managing blacklist
- Blacklist caching and invalidation
- Export/import blacklist configuration
- Blacklist statistics and analytics

## Support

For issues or questions:
- Check logs in `./log/mcp-server-istat.log`
- Review `TROUBLESHOOTING_CLAUDE.md`
- Open GitHub issue with reproduction steps
