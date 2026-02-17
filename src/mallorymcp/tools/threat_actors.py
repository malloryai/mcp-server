"""MCP tools for threat actor intelligence."""

from typing import Any

from ..decorator.api import handle_api_errors
from ..server.server import client, mcp
from ..utils.serialize import paginated_to_dict


@mcp.tool()
@handle_api_errors
async def get_threat_actor(identifier: str) -> dict[str, Any]:
    """Get a threat actor by UUID or name.

    Use for: TTPs, attribution, sophistication, target sectors/regions.

    Args:
        identifier: Threat actor UUID or name (e.g. dark_cloud_shield).

    Returns:
        Actor record with display_name, description, mentions, etc.
    """
    return await client.threat_actors.get(identifier)


@mcp.tool()
@handle_api_errors
async def list_threat_actors(
    filter: str = "",
    offset: int = 0,
    limit: int = 10,
    sort: str = "created_at",
    order: str = "desc",
) -> dict[str, Any]:
    """List or search threat actors with optional filters and pagination.

    Use for: discovering actors, building briefings, comparing actors.

    Args:
        filter: Optional filter (e.g. name:, uuid:).
        offset: Pagination offset. Default 0.
        limit: Max items per page. Default 10.
        sort: Field to sort by (e.g. name, created_at).
        order: asc or desc.

    Returns:
        Paginated result with items, total, offset, limit, has_more.
    """
    resp = await client.threat_actors.list(
        filter=filter or None,
        offset=offset,
        limit=limit,
        sort=sort,
        order=order,
    )
    return paginated_to_dict(resp)


@mcp.tool()
@handle_api_errors
async def list_trending_threat_actors(
    period: str = "7d",
    offset: int = 0,
    limit: int = 10,
) -> dict[str, Any]:
    """List threat actors trending over a time period.

    Use for: active threats, current reporting focus.

    Args:
        period: 1d, 7d, or 30d.
        offset: Pagination offset. Default 0.
        limit: Max items. Default 10.

    Returns:
        Paginated result with trending threat actor items.
    """
    resp = await client.threat_actors.trending(
        period=period,
        offset=offset,
        limit=limit,
    )
    return paginated_to_dict(resp)


@mcp.tool()
@handle_api_errors
async def list_mentioned_threat_actors(
    offset: int = 0,
    limit: int = 10,
    sort: str = "created_at",
    order: str = "desc",
) -> dict[str, Any]:
    """List recent threat actor mentions from intelligence sources.

    Use for: emerging threats, latest reporting, situational awareness.

    Args:
        offset: Pagination offset. Default 0.
        limit: Max items. Default 10.
        sort: Field to sort by. Default created_at.
        order: asc or desc.

    Returns:
        Paginated result with mention records (overview, source, dates).
    """
    resp = await client.mentions.actors(
        offset=offset,
        limit=limit,
        sort=sort,
        order=order,
    )
    return paginated_to_dict(resp)


@mcp.tool()
@handle_api_errors
async def get_threat_actor_attack_patterns(
    identifier: str,
    offset: int = 0,
    limit: int = 10,
) -> Any:
    """Get MITRE ATT&CK patterns associated with a threat actor.

    Use for: TTP mapping, detection engineering, adversary emulation.

    Args:
        identifier: Threat actor UUID or name.
        offset: Pagination offset. Default 0.
        limit: Max items. Default 10.

    Returns:
        Attack patterns linked to this actor.
    """
    return await client.threat_actors.attack_patterns(
        identifier,
        offset=offset,
        limit=limit,
    )
