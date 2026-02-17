"""MCP tools for entity mentions from intelligence sources."""

from ..decorator.api import handle_api_errors
from ..server.server import client, mcp
from ..utils.serialize import paginated_to_dict


@mcp.tool()
@handle_api_errors
async def list_mentions(
    offset: int = 0,
    limit: int = 10,
) -> dict:
    """List recent mentions across entity types.

    Use for: latest intel coverage, cross-entity activity.

    Args:
        offset: Pagination offset. Default 0.
        limit: Max items per page. Default 10.

    Returns:
        Paginated result with mention items.
    """
    resp = await client.mentions.list(
        offset=offset,
        limit=limit,
    )
    return paginated_to_dict(resp)


@mcp.tool()
@handle_api_errors
async def list_mentions_actors(
    offset: int = 0,
    limit: int = 10,
) -> dict:
    """List recent threat actor mentions from intelligence sources.

    Use for: emerging threats, latest actor reporting.

    Args:
        offset: Pagination offset. Default 0.
        limit: Max items. Default 10.

    Returns:
        Paginated result with threat actor mention items.
    """
    resp = await client.mentions.actors(
        offset=offset,
        limit=limit,
    )
    return paginated_to_dict(resp)


@mcp.tool()
@handle_api_errors
async def list_mentions_vulnerabilities(
    offset: int = 0,
    limit: int = 10,
) -> dict:
    """List recent vulnerability mentions from intelligence sources.

    Use for: CVE discussion in intel, trending CVEs in reporting.

    Args:
        offset: Pagination offset. Default 0.
        limit: Max items. Default 10.

    Returns:
        Paginated result with vulnerability mention items.
    """
    resp = await client.mentions.vulnerabilities(
        offset=offset,
        limit=limit,
    )
    return paginated_to_dict(resp)