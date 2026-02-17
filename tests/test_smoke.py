"""Basic smoke tests for the mallorymcp package."""


def test_import():
    """Package can be imported."""
    import mallorymcp

    assert mallorymcp.__version__


def test_server_initializes():
    """Server initializes and loads all tools."""
    from mallorymcp.server.server import load_tools, mcp

    load_tools()
    assert mcp.name == "Mallory"


def test_tools_registered():
    """All tool modules register their tools."""
    from mallorymcp.server.server import mcp

    tools = mcp._tool_manager._tools
    assert len(tools) >= 40


def test_entry_point():
    """Entry point function exists."""
    from mallorymcp.app import main

    assert callable(main)
