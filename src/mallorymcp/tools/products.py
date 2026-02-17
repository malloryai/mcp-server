"""MCP tools for technology product intelligence."""

from typing import Any

from ..decorator.api import handle_api_errors
from ..server.server import client, mcp
from ..utils.serialize import paginated_to_dict


@mcp.tool()
@handle_api_errors
async def get_product(identifier: str) -> dict[str, Any]:
    """Get a technology product by UUID or name.

    Use for: product details, linked advisories, vulnerability scope.

    Args:
        identifier: Product UUID or name.

    Returns:
        Product record with display_name, vendor, related advisories.
    """
    return await client.products.get(identifier)


@mcp.tool()
@handle_api_errors
async def list_products(
    filter: str = "",
    offset: int = 0,
    limit: int = 10,
    sort: str = "created_at",
    order: str = "desc",
) -> dict[str, Any]:
    """List or search technology products with optional filters and pagination.

    Use for: product catalogs, vendor mapping, affected software.

    Args:
        filter: Optional filter.
        offset: Pagination offset. Default 0.
        limit: Max items per page. Default 10.
        sort: Field to sort by. Default created_at.
        order: asc or desc.

    Returns:
        Paginated result with items, total, offset, limit, has_more.
    """
    resp = await client.products.list(
        filter=filter or None,
        offset=offset,
        limit=limit,
        sort=sort,
        order=order,
    )
    return paginated_to_dict(resp)


@mcp.tool()
@handle_api_errors
async def get_product_advisories(
    identifier: str,
    offset: int = 0,
    limit: int = 10,
) -> Any:
    """Get security advisories for a technology product.

    Use for: vendor advisories, patching guidance.

    Args:
        identifier: Product UUID or name.
        offset: Pagination offset. Default 0.
        limit: Max items. Default 10.

    Returns:
        Advisories linked to this product.
    """
    return await client.products.advisories(
        identifier,
        offset=offset,
        limit=limit,
    )
