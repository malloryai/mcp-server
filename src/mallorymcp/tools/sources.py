"""MCP tools for intelligence source metadata."""

from ..decorator.api import handle_api_errors
from ..server.server import client, mcp
from ..utils.serialize import paginated_to_dict


@mcp.tool()
@handle_api_errors
async def list_sources(
    offset: int = 0,
    limit: int = 50,
) -> dict:
    """List intelligence sources (feeds, blogs, etc.) in the platform.

    Use for: discovering available sources, source metadata.

    Args:
        offset: Pagination offset. Default 0.
        limit: Max items per page. Default 50.

    Returns:
        Paginated result with source items (name, slug, type, etc.).
    """
    resp = await client.sources.list(
        offset=offset,
        limit=limit,
    )
    return paginated_to_dict(resp)