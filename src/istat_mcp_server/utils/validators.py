"""Input validation helpers."""

import logging
import re

logger = logging.getLogger(__name__)


def validate_keywords(keywords: str) -> list[str]:
    """Parse and validate comma-separated keywords.

    Args:
        keywords: Comma-separated keywords string

    Returns:
        List of cleaned keywords
    """
    if not keywords or not keywords.strip():
        return []

    # Split by comma and clean up
    cleaned = [k.strip().lower() for k in keywords.split(',') if k.strip()]
    logger.debug(f'Parsed keywords: {cleaned}')
    return cleaned


def validate_dataflow_id(dataflow_id: str) -> bool:
    """Validate dataflow ID format.

    Args:
        dataflow_id: Dataflow ID to validate

    Returns:
        True if valid, False otherwise
    """
    # Basic validation - dataflow IDs typically contain numbers, letters, and underscores
    if not dataflow_id or not dataflow_id.strip():
        return False

    # Check for reasonable characters
    if not re.match(r'^[A-Za-z0-9_]+$', dataflow_id):
        return False

    return True
