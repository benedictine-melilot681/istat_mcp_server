"""Tool: get_codelist_description - Get descriptions for codelist values."""

import logging
from typing import Any

from mcp.types import TextContent

from ..api.client import ApiClient
from ..api.models import GetCodelistDescriptionInput
from ..cache.manager import CacheManager
from ..utils.tool_helpers import (
    format_json_response,
    get_cached_codelist,
    handle_tool_errors,
)

logger = logging.getLogger(__name__)

@handle_tool_errors
async def handle_get_codelist_description(
    arguments: dict[str, Any],
    cache: CacheManager,
    api: ApiClient,
) -> list[TextContent]:
    """Handle get_codelist_description tool.

    Args:
        arguments: Raw arguments dict from MCP
        cache: Cache manager instance
        api: API client instance

    Returns:
        List of TextContent with JSON-formatted response or error message
    """
    # Validate input
    params = GetCodelistDescriptionInput.model_validate(arguments)
    logger.info(f'get_codelist_description: codelist_id={params.codelist_id}')

    codelist = await get_cached_codelist(cache, api, params.codelist_id)

    # Format response
    return format_json_response(codelist)
