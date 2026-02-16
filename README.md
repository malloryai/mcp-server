# Mallory MCP Server

[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Mallory provides a robust source of cyber and threat intelligence. This MCP server exposes the Mallory API to AI agents via the [malloryapi](https://github.com/malloryai/malloryapi) Python client, with tools for vulnerabilities, threat actors, malware, exploits, organizations, attack patterns, breaches, products, advisories, stories, mentions, search, and sources.

Once connected, your AI assistant (Cursor, Claude Desktop, or another MCP client) can look up CVEs, threat actors, malware, and more directly from Mallory—no copy-pasting from the dashboard.

## Prerequisites

- Python 3.11 or higher
- [uv](https://docs.astral.sh/uv/) for install and run (recommended)
- A Mallory API key ([Mallory](https://mallory.ai))

## Quick Start

### Installation

```bash
git clone https://github.com/malloryai/mallory-mcp-server.git
cd mallory-mcp-server
uv sync
```

The server depends on the [malloryapi](https://pypi.org/project/malloryapi/) package from PyPI. `uv sync` creates a virtual environment and installs dependencies from `uv.lock`.

### Configuration

Set the API key (required). Optionally override the API base URL (e.g. for a local or staging endpoint):

```bash
export MALLORY_API_KEY=your_api_key_here
# optional:
export MALLORY_BASE_URL=https://api.mallory.ai/v1
```

No `.env` file is required; the server reads from the environment. You can use a `.env` file and load it yourself (e.g. via your shell or process manager) if you prefer.

### Running the Server

```bash
uv run python -m mallory.mcp.app
```

Or use the installed entry point:

```bash
uv run mallory-mcp-server
```

## How to use

1. **Install** (see above): clone the repo, run `uv sync`.
2. **Get an API key** at [Mallory](https://mallory.ai) and set `MALLORY_API_KEY` in your environment or in your MCP config.
3. **Connect your AI client** using one of the configs below.
4. **Use the tools** by asking your assistant to query Mallory. For example:
   - _"Look up CVE-2024-1234 and summarize the risk."_
   - _"List threat actors trending in the last 7 days."_
   - _"Find vulnerabilities that are known to be exploited."_
   - _"Search for intelligence on APT28."_
   - _"What malware is associated with technique T1566?"_

The assistant will call the MCP tools automatically; you don’t need to invoke tool names yourself.

### Cursor

In Cursor, open **Settings → MCP** and add a server. If you installed the server in `~/projects/mallory-mcp-server`:

| Field   | Value                                                |
| ------- | ---------------------------------------------------- |
| Name    | MalloryAI (or any label)                             |
| Command | `uv`                                                 |
| Args    | `run`, `mallory-mcp-server`                          |
| Cwd     | `~/projects/mallory-mcp-server` (or your clone path) |
| Env     | `MALLORY_API_KEY` = your API key                     |

Or add to your Cursor MCP config file (e.g. `~/.cursor/mcp.json`):

```json
{
  "mcpServers": {
    "MalloryAI": {
      "command": "uv",
      "args": ["run", "mallory-mcp-server"],
      "cwd": "/path/to/your/mallory-mcp-server",
      "env": {
        "MALLORY_API_KEY": "your_api_key_here"
      }
    }
  }
}
```

Replace `/path/to/your/mallory-mcp-server` with the path where you cloned this repo.

### Claude Desktop

Clone this repo and point Claude at it. In `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "MalloryAI": {
      "command": "uv",
      "args": ["run", "mallory-mcp-server"],
      "cwd": "/path/to/mallory-mcp-server",
      "env": {
        "MALLORY_API_KEY": "your_api_key_here"
      }
    }
  }
}
```

Replace `cwd` with the path where you ran `git clone` (e.g. `~/projects/mallory-mcp-server`). Run `uv sync` in that directory once before using Claude.

## Tools

The server exposes the following tools, backed by the Mallory API.

### Vulnerabilities (7)

| Tool                                     | Description                                             |
| ---------------------------------------- | ------------------------------------------------------- |
| `get_vulnerability`                      | Get a vulnerability by CVE ID or UUID                   |
| `list_vulnerabilities`                   | List/search vulnerabilities with filters and pagination |
| `list_trending_vulnerabilities`          | List vulnerabilities trending over 1d/7d/30d            |
| `list_exploited_vulnerabilities`         | List vulnerabilities known to be exploited in the wild  |
| `get_vulnerability_detection_signatures` | Detection signatures for a CVE                          |
| `get_vulnerability_exploitations`        | Exploitation records for a CVE                          |
| `get_vulnerability_configurations`       | Affected configurations (CPE) for a CVE                 |

### Threat Actors (5)

| Tool                               | Description                                     |
| ---------------------------------- | ----------------------------------------------- |
| `get_threat_actor`                 | Get a threat actor by UUID or name              |
| `list_threat_actors`               | List/search threat actors                       |
| `list_trending_threat_actors`      | List trending threat actors                     |
| `list_mentioned_threat_actors`     | Recent threat actor mentions from intel sources |
| `get_threat_actor_attack_patterns` | MITRE ATT&CK patterns for an actor              |

### Malware (5)

| Tool                          | Description                          |
| ----------------------------- | ------------------------------------ |
| `get_malware`                 | Get a malware entity by UUID or name |
| `list_malware`                | List/search malware                  |
| `list_trending_malware`       | List trending malware                |
| `get_malware_vulnerabilities` | Vulnerabilities linked to a malware  |
| `get_malware_attack_patterns` | MITRE ATT&CK patterns for a malware  |

### Exploits (2)

| Tool            | Description                          |
| --------------- | ------------------------------------ |
| `get_exploit`   | Get an exploit by UUID or identifier |
| `list_exploits` | List/search exploits                 |

### Organizations (4)

| Tool                          | Description                              |
| ----------------------------- | ---------------------------------------- |
| `get_organization`            | Get an organization by UUID or name      |
| `list_organizations`          | List/search organizations                |
| `list_trending_organizations` | List trending organizations              |
| `get_organization_breaches`   | Breaches associated with an organization |

### Attack Patterns (4)

| Tool                               | Description                                                  |
| ---------------------------------- | ------------------------------------------------------------ |
| `get_attack_pattern`               | Get an attack pattern (MITRE ATT&CK technique) by UUID or ID |
| `list_attack_patterns`             | List/search attack patterns                                  |
| `get_attack_pattern_threat_actors` | Threat actors associated with a technique                    |
| `get_attack_pattern_malware`       | Malware associated with a technique                          |

### Breaches (3)

| Tool                       | Description                            |
| -------------------------- | -------------------------------------- |
| `get_breach`               | Get a breach by UUID or identifier     |
| `list_breaches`            | List breaches                          |
| `get_breach_organizations` | Organizations associated with a breach |

### Products (3)

| Tool                     | Description                              |
| ------------------------ | ---------------------------------------- |
| `get_product`            | Get a technology product by UUID or name |
| `list_products`          | List/search technology products          |
| `get_product_advisories` | Security advisories for a product        |

### Advisories (3)

| Tool                           | Description                                             |
| ------------------------------ | ------------------------------------------------------- |
| `get_advisory`                 | Get a technology product advisory by UUID or identifier |
| `list_advisories`              | List technology product advisories                      |
| `get_advisory_vulnerabilities` | Vulnerabilities associated with an advisory             |

### Stories (3)

| Tool                | Description                                     |
| ------------------- | ----------------------------------------------- |
| `get_story`         | Get an intelligence story by UUID or identifier |
| `list_stories`      | List/search intelligence stories                |
| `list_story_topics` | List available story topics                     |

### Mentions (3)

| Tool                            | Description                              |
| ------------------------------- | ---------------------------------------- |
| `list_mentions`                 | List recent mentions across entity types |
| `list_mentions_actors`          | Recent threat actor mentions             |
| `list_mentions_vulnerabilities` | Recent vulnerability mentions            |

### Search and Sources (2)

| Tool           | Description                                    |
| -------------- | ---------------------------------------------- |
| `search`       | Search across all entity types by query string |
| `list_sources` | List intelligence sources in the platform      |

## Project Structure

```
mallory/
├── __init__.py
└── mcp/
    ├── __init__.py
    ├── app.py              # Entry point (main, stdio transport)
    ├── config/             # Env-based config (MALLORY_API_KEY, MALLORY_BASE_URL)
    ├── decorator/          # API error handling for tools
    ├── server/             # FastMCP server and tool loader
    ├── tools/              # Tool modules (one per resource area)
    └── utils/              # Serialization, debug
pyproject.toml
README.md
```

## Development

### Lint

Optional lint dependency uses [ruff](https://docs.astral.sh/ruff/):

```bash
uv sync --extra lint
uv run ruff check .
uv run ruff format .
```

### Commit Messages

Conventional commits preferred, e.g. `feat(tools): add malware tools`, `fix(server): client init with base_url`.

## License

MIT.
