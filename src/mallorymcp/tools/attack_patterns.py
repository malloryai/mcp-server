"""MCP tools for MITRE ATT&CK pattern intelligence."""

from typing import Any

from ..decorator.api import handle_api_errors
from ..server.server import client, mcp
from ..utils.serialize import paginated_to_dict


@mcp.tool()
@handle_api_errors
async def get_attack_pattern(identifier: str) -> dict[str, Any]:
    """Get an attack pattern (MITRE ATT&CK technique) by UUID or ID.

    Use for: TTP details, detection guidance, related actors and malware.

    Args:
        identifier: Attack pattern UUID or technique ID.

    Returns:
        Attack pattern record with name, description, references.
    """
    return await client.attack_patterns.get(identifier)


@mcp.tool()
@handle_api_errors
async def list_attack_patterns(
    filter: str = "",
    offset: int = 0,
    limit: int = 10,
    sort: str = "created_at",
    order: str = "desc",
) -> dict[str, Any]:
    """List or search attack patterns with optional filters and pagination.

    Use for: browsing techniques, mapping TTPs, detection coverage.

    Args:
        filter: Optional filter.
        offset: Pagination offset. Default 0.
        limit: Max items per page. Default 10.
        sort: Field to sort by. Default created_at.
        order: asc or desc.

    Returns:
        Paginated result with items, total, offset, limit, has_more.
    """
    resp = await client.attack_patterns.list(
        filter=filter or None,
        offset=offset,
        limit=limit,
        sort=sort,
        order=order,
    )
    return paginated_to_dict(resp)


@mcp.tool()
@handle_api_errors
async def get_attack_pattern_threat_actors(
    identifier: str,
    offset: int = 0,
    limit: int = 10,
) -> Any:
    """Get threat actors associated with an attack pattern.

    Use for: attribution, actor TTP mapping.

    Args:
        identifier: Attack pattern UUID or technique ID.
        offset: Pagination offset. Default 0.
        limit: Max items. Default 10.

    Returns:
        Threat actors linked to this technique.
    """
    return await client.attack_patterns.threat_actors(
        identifier,
        offset=offset,
        limit=limit,
    )


@mcp.tool()
@handle_api_errors
async def get_attack_pattern_malware(
    identifier: str,
    offset: int = 0,
    limit: int = 10,
) -> Any:
    """Get malware associated with an attack pattern.

    Use for: malware TTP mapping, detection engineering.

    Args:
        identifier: Attack pattern UUID or technique ID.
        offset: Pagination offset. Default 0.
        limit: Max items. Default 10.

    Returns:
        Malware linked to this technique.
    """
    return await client.attack_patterns.malware(
        identifier,
        offset=offset,
        limit=limit,
    )
