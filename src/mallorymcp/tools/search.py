"""MCP tools for cross-entity search."""

from typing import Any

from ..decorator.api import handle_api_errors
from ..server.server import client, mcp


@mcp.tool()
@handle_api_errors
async def search(q: str, **kwargs: Any) -> Any:
    """Search across all entity types (vulnerabilities, threat actors, malware, etc.).

    Use for: open-ended intel lookup, finding entities by keyword or name.

    Args:
        q: Search query string.
        **kwargs: Additional API query parameters (e.g. limit, offset).

    Returns:
        Search results across entity types matching the query.
    """
    return await client.search.query(q, **kwargs)