"""MCP tools for story (intelligence story) content."""

from typing import Any

from ..decorator.api import handle_api_errors
from ..server.server import client, mcp
from ..utils.serialize import paginated_to_dict


@mcp.tool()
@handle_api_errors
async def get_story(identifier: str) -> dict[str, Any]:
    """Get an intelligence story by UUID or identifier.

    Use for: full story content, references, entities, related events.

    Args:
        identifier: Story UUID or identifier.

    Returns:
        Story record with title, summary, content, references, entities.
    """
    return await client.stories.get(identifier)


@mcp.tool()
@handle_api_errors
async def list_stories(
    filter: str = "",
    offset: int = 0,
    limit: int = 10,
    sort: str = "created_at",
    order: str = "desc",
) -> dict[str, Any]:
    """List or search intelligence stories with optional filters and pagination.

    Use for: recent intel, topic-based discovery.

    Args:
        filter: Optional filter.
        offset: Pagination offset. Default 0.
        limit: Max items per page. Default 10.
        sort: Field to sort by. Default created_at.
        order: asc or desc.

    Returns:
        Paginated result with items, total, offset, limit, has_more.
    """
    resp = await client.stories.list(
        filter=filter or None,
        offset=offset,
        limit=limit,
        sort=sort,
        order=order,
    )
    return paginated_to_dict(resp)


@mcp.tool()
@handle_api_errors
async def list_story_topics() -> Any:
    """List available story topics for filtering.

    Use for: discovering topic taxonomy, filtering stories by topic.

    Returns:
        List of topic identifiers/names.
    """
    return await client.stories.topics()