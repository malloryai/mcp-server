import importlib
import pkgutil
from pathlib import Path

from malloryapi import AsyncMalloryApi
from mcp.server.fastmcp import FastMCP

from ..config import MALLORY_API_KEY, MALLORY_BASE_URL
from ..utils.debug import debug_log

mcp = FastMCP("Mallory")

client = AsyncMalloryApi(
    api_key=MALLORY_API_KEY or None,
    base_url=MALLORY_BASE_URL,
)


def load_tools():
    """Dynamically load all tool modules in the tools package."""
    tools_dir = Path(__file__).resolve().parent.parent / "tools"
    for _, module_name, _ in pkgutil.iter_modules([str(tools_dir)]):
        if module_name != "__init__":
            importlib.import_module(
                f"mallorymcp.tools.{module_name}"
            )
            debug_log(f"Loaded tool: {module_name}")


def initialize_server():
    """Initialize the server by loading all tools."""
    try:
        debug_log("Starting tool loading...")
        load_tools()
        debug_log("Tools loaded successfully")
        return mcp
    except Exception as e:
        debug_log(f"Error during initialization: {str(e)}")
        raise
