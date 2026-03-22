"""Tool: get_structure - Get data structure definition for a datastructure."""

import logging
from typing import Any

from mcp.types import TextContent

from ..api.client import ApiClient
from ..api.models import GetStructureInput
from ..cache.manager import CacheManager
from ..utils.tool_helpers import (
    format_json_response,
    get_cached_datastructure,
    handle_tool_errors,
)

logger = logging.getLogger(__name__)

@handle_tool_errors
async def handle_get_structure(
    arguments: dict[str, Any],
    cache: CacheManager,
    api: ApiClient,
) -> list[TextContent]:
    """Handle get_structure tool.

    Args:
        arguments: Raw arguments dict from MCP
        cache: Cache manager instance
        api: API client instance

    Returns:
        List of TextContent with JSON-formatted response or error message
    """
    # Validate input
    params = GetStructureInput.model_validate(arguments)
    logger.info(f'get_structure: id_datastructure={params.id_datastructure}')

    datastructure = await get_cached_datastructure(
        cache,
        api,
        params.id_datastructure,
    )

    # Format response
    return format_json_response(datastructure)
