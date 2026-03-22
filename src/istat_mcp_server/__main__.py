"""Entry point for running the server with `python -m istat_mcp_server`."""

import asyncio
import logging

from mcp.server.stdio import stdio_server

from .server import create_server

logger = logging.getLogger(__name__)


async def main():
    """Run the MCP server using stdio transport."""
    server = create_server()
    logger.info('Starting ISTAT MCP Server on stdio')

    async with stdio_server() as (read_stream, write_stream):
        await server.run(read_stream, write_stream, server.create_initialization_options())


if __name__ == '__main__':
    asyncio.run(main())
