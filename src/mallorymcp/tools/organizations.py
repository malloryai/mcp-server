"""MCP tools for organization (breach target) intelligence."""

from typing import Any

from ..decorator.api import handle_api_errors
from ..server.server import client, mcp
from ..utils.serialize import paginated_to_dict


@mcp.tool()
@handle_api_errors
async def get_organization(identifier: str) -> dict[str, Any]:
    """Get an organization by UUID or name.

    Use for: breach targets, company intel, linked breaches and products.

    Args:
        identifier: Organization UUID or name.

    Returns:
        Organization record with display_name, description, related data.
    """
    return await client.organizations.get(identifier)


@mcp.tool()
@handle_api_errors
async def list_organizations(
    filter: str = "",
    offset: int = 0,
    limit: int = 10,
    sort: str = "created_at",
    order: str = "desc",
) -> dict[str, Any]:
    """List or search organizations with optional filters and pagination.

    Use for: discovering breached or tracked organizations.

    Args:
        filter: Optional filter (e.g. name:, uuid:).
        offset: Pagination offset. Default 0.
        limit: Max items per page. Default 10.
        sort: Field to sort by. Default created_at.
        order: asc or desc.

    Returns:
        Paginated result with items, total, offset, limit, has_more.
    """
    resp = await client.organizations.list(
        filter=filter or None,
        offset=offset,
        limit=limit,
        sort=sort,
        order=order,
    )
    return paginated_to_dict(resp)


@mcp.tool()
@handle_api_errors
async def list_trending_organizations(
    period: str = "7d",
    offset: int = 0,
    limit: int = 10,
) -> dict[str, Any]:
    """List organizations trending over a time period.

    Use for: recent breach or reporting focus.

    Args:
        period: 1d, 7d, or 30d.
        offset: Pagination offset. Default 0.
        limit: Max items. Default 10.

    Returns:
        Paginated result with trending organization items.
    """
    resp = await client.organizations.trending(
        period=period,
        offset=offset,
        limit=limit,
    )
    return paginated_to_dict(resp)


@mcp.tool()
@handle_api_errors
async def get_organization_breaches(
    identifier: str,
    offset: int = 0,
    limit: int = 10,
) -> Any:
    """Get breaches associated with an organization.

    Use for: breach history, incident timeline.

    Args:
        identifier: Organization UUID or name.
        offset: Pagination offset. Default 0.
        limit: Max items. Default 10.

    Returns:
        Breaches linked to this organization.
    """
    return await client.organizations.breaches(
        identifier,
        offset=offset,
        limit=limit,
    )
