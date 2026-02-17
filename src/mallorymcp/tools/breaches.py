"""MCP tools for breach intelligence."""

from typing import Any

from ..decorator.api import handle_api_errors
from ..server.server import client, mcp
from ..utils.serialize import paginated_to_dict


@mcp.tool()
@handle_api_errors
async def get_breach(identifier: str) -> dict[str, Any]:
    """Get a breach by UUID or identifier.

    Use for: breach details, affected organizations, timeline.

    Args:
        identifier: Breach UUID or identifier.

    Returns:
        Breach record with description, dates, related organizations.
    """
    return await client.breaches.get(identifier)


@mcp.tool()
@handle_api_errors
async def list_breaches(
    offset: int = 0,
    limit: int = 10,
    sort: str = "created_at",
    order: str = "desc",
) -> dict[str, Any]:
    """List breaches with optional pagination and sorting.

    Use for: breach catalogs, recent incidents.

    Args:
        offset: Pagination offset. Default 0.
        limit: Max items per page. Default 10.
        sort: Field to sort by. Default created_at.
        order: asc or desc.

    Returns:
        Paginated result with items, total, offset, limit, has_more.
    """
    resp = await client.breaches.list(
        offset=offset,
        limit=limit,
        sort=sort,
        order=order,
    )
    return paginated_to_dict(resp)


@mcp.tool()
@handle_api_errors
async def get_breach_organizations(
    identifier: str,
    offset: int = 0,
    limit: int = 10,
) -> Any:
    """Get organizations associated with a breach.

    Use for: affected entities, scope of breach.

    Args:
        identifier: Breach UUID or identifier.
        offset: Pagination offset. Default 0.
        limit: Max items. Default 10.

    Returns:
        Organizations linked to this breach.
    """
    return await client.breaches.organizations(
        identifier,
        offset=offset,
        limit=limit,
    )
