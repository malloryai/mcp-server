"""Serialization helpers for MCP tool responses."""

from malloryapi import PaginatedResponse


def paginated_to_dict(response: PaginatedResponse) -> dict:
    """Convert a PaginatedResponse to a JSON-serializable dict for MCP tools."""
    return {
        "items": response.items,
        "total": response.total,
        "offset": response.offset,
        "limit": response.limit,
        "has_more": response.has_more,
    }