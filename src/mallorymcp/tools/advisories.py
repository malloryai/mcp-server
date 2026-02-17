"""MCP tools for technology product advisory intelligence."""

from typing import Any

from ..decorator.api import handle_api_errors
from ..server.server import client, mcp
from ..utils.serialize import paginated_to_dict


@mcp.tool()
@handle_api_errors
async def get_advisory(identifier: str) -> dict[str, Any]:
    """Get a technology product advisory by UUID or identifier.

    Use for: vendor advisory details, patching guidance, linked CVEs.

    Args:
        identifier: Advisory UUID or identifier.

    Returns:
        Advisory record with description, dates, related products/CVEs.
    """
    return await client.advisories.get(identifier)


@mcp.tool()
@handle_api_errors
async def list_advisories(
    offset: int = 0,
    limit: int = 10,
    sort: str = "created_at",
    order: str = "desc",
) -> dict[str, Any]:
    """List technology product advisories with optional pagination and sorting.

    Use for: advisory catalogs, recent vendor bulletins.

    Args:
        offset: Pagination offset. Default 0.
        limit: Max items per page. Default 10.
        sort: Field to sort by. Default created_at.
        order: asc or desc.

    Returns:
        Paginated result with items, total, offset, limit, has_more.
    """
    resp = await client.advisories.list(
        offset=offset,
        limit=limit,
        sort=sort,
        order=order,
    )
    return paginated_to_dict(resp)


@mcp.tool()
@handle_api_errors
async def get_advisory_vulnerabilities(
    identifier: str,
    offset: int = 0,
    limit: int = 10,
) -> Any:
    """Get vulnerabilities associated with an advisory.

    Use for: CVE coverage of a vendor advisory.

    Args:
        identifier: Advisory UUID or identifier.
        offset: Pagination offset. Default 0.
        limit: Max items. Default 10.

    Returns:
        Vulnerabilities linked to this advisory.
    """
    return await client.advisories.vulnerabilities(
        identifier,
        offset=offset,
        limit=limit,
    )