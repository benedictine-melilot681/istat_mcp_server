"""Tool: get_concepts - Get concept schemes and their descriptions."""

import logging
from typing import Any

from mcp.types import TextContent

from ..api.client import ApiClient
from ..cache.manager import CacheManager
from ..utils.tool_helpers import (
    format_json_response,
    get_cached_conceptschemes,
    handle_tool_errors,
)

logger = logging.getLogger(__name__)

@handle_tool_errors
async def handle_get_concepts(
    arguments: dict[str, Any],
    cache: CacheManager,
    api: ApiClient,
) -> list[TextContent]:
    """Handle get_concepts tool.

    Args:
        arguments: Raw arguments dict from MCP (empty for this tool)
        cache: Cache manager instance
        api: API client instance

    Returns:
        List of TextContent with JSON-formatted response or error message
    """
    logger.info('get_concepts: fetching concept schemes')

    schemes = await get_cached_conceptschemes(cache, api)

    # Format response
    response = {
        'count': len(schemes),
        'concept_schemes': [s.model_dump() for s in schemes],
    }

    return format_json_response(response)
