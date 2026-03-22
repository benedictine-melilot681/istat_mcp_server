# Claude Desktop Configuration Example

Example configuration for using the ISTAT MCP server with Claude Desktop.

## Installation Steps

1. Install the server:
```bash
cd /path/to/istat_mcp_server
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install -e .
```

2. Find your Claude Desktop configuration file:
   - **macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`
   - **Windows**: `%APPDATA%\Claude\claude_desktop_config.json`

3. Add the ISTAT server configuration:

### macOS/Linux Configuration

```json
{
  "mcpServers": {
    "istat": {
      "command": "/path/to/istat_mcp_server/.venv/bin/python",
      "args": ["-m", "istat_mcp_server"],
      "cwd": "/path/to/istat_mcp_server"
    }
  }
}
```

### Windows Configuration

```json
{
  "mcpServers": {
    "istat": {
      "command": "C:\\path\\to\\istat_mcp_server\\.venv\\Scripts\\python.exe",
      "args": ["-m", "istat_mcp_server"],
      "cwd": "C:\\path\\to\\istat_mcp_server"
    }
  }
}
```

## Environment Variables (Optional)

Create a `.env` file in the project root to customize settings:

```env
# API Configuration
API_BASE_URL=https://esploradati.istat.it/SDMXWS/rest
API_TIMEOUT_SECONDS=120
AVAILABLECONSTRAINT_TIMEOUT_SECONDS=180
API_MAX_RETRIES=3

# Cache Configuration
PERSISTENT_CACHE_DIR=./cache
MEMORY_CACHE_TTL_SECONDS=300
DATAFLOWS_CACHE_TTL_SECONDS=604800
METADATA_CACHE_TTL_SECONDS=2592000
OBSERVED_DATA_CACHE_TTL_SECONDS=3600
MAX_MEMORY_CACHE_ITEMS=512

# Logging
LOG_LEVEL=INFO
```

## Testing the Connection

After configuring Claude Desktop:

1. Restart Claude Desktop
2. Start a new conversation
3. Try asking Claude:
   - "What ISTAT dataflows are available about population?"
   - "Can you list the available Italian statistical datasets?"

Claude should now have access to the ISTAT MCP tools!

## Troubleshooting

If the server doesn't work:

1. Check Claude Desktop logs:
   - **macOS**: `~/Library/Logs/Claude/`
   - **Windows**: `%APPDATA%\Claude\logs\`

2. Test the server manually:
```bash
cd /path/to/istat_mcp_server
source .venv/bin/activate
python -m istat_mcp_server
```

3. Verify Python path is correct in configuration

4. Ensure all dependencies are installed:
```bash
pip install -e .
```
