"""In-memory cache implementation using cachetools."""

import logging
from typing import Any

from cachetools import TTLCache

logger = logging.getLogger(__name__)


class MemoryCache:
    """In-memory cache with TTL support using cachetools.TTLCache."""

    def __init__(self, ttl: int = 300, max_size: int = 512):
        """Initialize memory cache.

        Args:
            ttl: Time to live in seconds (default: 5 minutes)
            max_size: Maximum number of items in cache
        """
        self._cache = TTLCache(maxsize=max_size, ttl=ttl)
        logger.info(f'MemoryCache initialized with TTL={ttl}s, max_size={max_size}')

    def get(self, key: str) -> Any | None:
        """Get value from cache.

        Args:
            key: Cache key

        Returns:
            Cached value or None if not found
        """
        value = self._cache.get(key)
        if value is not None:
            logger.debug(f'MemoryCache HIT: {key}')
        else:
            logger.debug(f'MemoryCache MISS: {key}')
        return value

    def set(self, key: str, value: Any) -> None:
        """Set value in cache.

        Args:
            key: Cache key
            value: Value to cache
        """
        self._cache[key] = value
        logger.debug(f'MemoryCache SET: {key}')

    def delete(self, key: str) -> None:
        """Delete value from cache.

        Args:
            key: Cache key
        """
        if key in self._cache:
            del self._cache[key]
            logger.debug(f'MemoryCache DELETE: {key}')

    def clear(self) -> None:
        """Clear all cached values."""
        self._cache.clear()
        logger.info('MemoryCache cleared')

    def __len__(self) -> int:
        """Return number of items in cache."""
        return len(self._cache)
