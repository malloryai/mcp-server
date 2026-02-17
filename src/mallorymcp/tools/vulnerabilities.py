"""MCP tools for vulnerability intelligence."""

from typing import Any

from ..decorator.api import handle_api_errors
from ..server.server import client, mcp
from ..utils.serialize import paginated_to_dict


@mcp.tool()
@handle_api_errors
async def get_vulnerability(identifier: str) -> dict[str, Any]:
    """Get a vulnerability by CVE ID or UUID.

    Use for: threat assessment, patching priority, technical details of a CVE.

    Args:
        identifier: CVE ID (e.g. CVE-2024-1234) or vulnerability UUID.

    Returns:
        Vulnerability record with description, CVSS/EPSS scores, timestamps.
    """
    return await client.vulnerabilities.get(identifier)


@mcp.tool()
@handle_api_errors
async def list_vulnerabilities(
    filter: str = "",
    offset: int = 0,
    limit: int = 10,
    sort: str = "created_at",
    order: str = "desc",
) -> dict[str, Any]:
    """List or search vulnerabilities with optional filters and pagination.

    Use for: recent CVEs, search by description, high-severity or trending lists.

    Args:
        filter: Optional filter (e.g. cve:, uuid:, desc:).
        offset: Pagination offset. Default 0.
        limit: Max items per page. Default 10.
        sort: Field to sort by (e.g. created_at, cvss_3_base_score).
        order: asc or desc.

    Returns:
        Paginated result with items, total, offset, limit, has_more.
    """
    resp = await client.vulnerabilities.list(
        filter=filter or None,
        offset=offset,
        limit=limit,
        sort=sort,
        order=order,
    )
    return paginated_to_dict(resp)


@mcp.tool()
@handle_api_errors
async def list_trending_vulnerabilities(
    period: str = "7d",
    offset: int = 0,
    limit: int = 10,
) -> dict[str, Any]:
    """List vulnerabilities trending over a time period.

    Use for: prioritising recently active or discussed CVEs.

    Args:
        period: 1d, 7d, or 30d.
        offset: Pagination offset. Default 0.
        limit: Max items. Default 10.

    Returns:
        Paginated result with trending vulnerability items.
    """
    resp = await client.vulnerabilities.trending(
        period=period,
        offset=offset,
        limit=limit,
    )
    return paginated_to_dict(resp)


@mcp.tool()
@handle_api_errors
async def list_exploited_vulnerabilities(
    offset: int = 0,
    limit: int = 10,
) -> dict[str, Any]:
    """List vulnerabilities known to be exploited in the wild.

    Use for: prioritising remediation, CISA KEV-style lists.

    Args:
        offset: Pagination offset. Default 0.
        limit: Max items. Default 10.

    Returns:
        Paginated result with exploited vulnerability items.
    """
    resp = await client.vulnerabilities.exploited(
        offset=offset,
        limit=limit,
    )
    return paginated_to_dict(resp)


@mcp.tool()
@handle_api_errors
async def get_vulnerability_detection_signatures(
    identifier: str,
) -> Any:
    """Get detection signatures for a vulnerability (e.g. CVE).

    Use for: building detection rules, IOCs, verifying detection coverage.

    Args:
        identifier: CVE ID or vulnerability UUID.

    Returns:
        Detection signatures (source, method, description, etc.).
    """
    return await client.vulnerabilities.detection_signatures(identifier)


@mcp.tool()
@handle_api_errors
async def get_vulnerability_exploitations(
    identifier: str,
) -> Any:
    """Get exploitation records for a vulnerability.

    Use for: confirming in-the-wild exploitation, timelines, detection refs.

    Args:
        identifier: CVE ID or vulnerability UUID.

    Returns:
        Exploitation records (begins_at, ends_at, count, detection refs).
    """
    return await client.vulnerabilities.exploitations(identifier)


@mcp.tool()
@handle_api_errors
async def get_vulnerability_configurations(
    identifier: str,
) -> Any:
    """Get affected configurations (CPE) for a vulnerability.

    Use for: scope of impact, asset mapping, filtering false positives.

    Args:
        identifier: CVE ID or vulnerability UUID.

    Returns:
        Configuration records (CPE, vendor, product, version ranges).
    """
    return await client.vulnerabilities.configurations(identifier)
