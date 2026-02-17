# Mallory MCP Server

[![PyPI](https://img.shields.io/pypi/v/mallorymcp.svg)](https://pypi.org/project/mallorymcp/)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![License: Apache 2.0](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

[Mallory](https://mallory.ai) provides a robust source of cyber and threat intelligence. This MCP server exposes the Mallory API to AI agents via the [malloryapi](https://github.com/malloryai/malloryapi) Python client, with tools for vulnerabilities, threat actors, malware, exploits, organizations, attack patterns, breaches, products, advisories, stories, mentions, search, and sources.

Once connected, your AI assistant (Cursor, Claude Desktop, or another MCP client) can look up CVEs, threat actors, malware, and more directly from Mallory — no copy-pasting from the dashboard.

## Quick Start

### 1. Set your API key

Get an API key at [mallory.ai](https://mallory.ai) and add it to your shell profile (`~/.zshrc`, `~/.bashrc`, etc.):

```bash
export MALLORY_API_KEY=your_api_key_here
```

Reload your shell (or run `source ~/.zshrc`) so the variable is available.

Optionally override the API base URL:

```bash
export MALLORY_BASE_URL=https://api.mallory.ai/v1
```

### 2. Install

```bash
pip install mallorymcp
```

Or with uv:

```bash
uv pip install mallorymcp
```

### 3. Add to your AI client

See [Client Configuration](#client-configuration) below.

### 4. Start using it

Ask your assistant to query Mallory:

- _"Look up CVE-2024-1234 and summarize the risk."_
- _"List threat actors trending in the last 7 days."_
- _"Find vulnerabilities that are known to be exploited."_
- _"Search for intelligence on APT28."_
- _"What malware is associated with technique T1566?"_

The assistant calls the MCP tools automatically.

## Client Configuration

### Cursor

Add to your Cursor MCP config file (e.g. `~/.cursor/mcp.json`):

```json
{
  "mcpServers": {
    "Mallory": {
      "command": "mallorymcp"
    }
  }
}
```

Or in Cursor, open **Settings → MCP** and add a server:

| Field   | Value        |
| ------- | ------------ |
| Name    | Mallory      |
| Command | `mallorymcp` |

### Claude Desktop

Add to `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "Mallory": {
      "command": "mallorymcp"
    }
  }
}
```

### Running with uvx (no install)

If you prefer not to install the package globally, you can run it directly with `uvx`:

```json
{
  "mcpServers": {
    "Mallory": {
      "command": "uvx",
      "args": ["mallorymcp"]
    }
  }
}
```

This downloads and runs the package in an isolated environment each time.

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

## Development

### Install from source

```bash
git clone https://github.com/malloryai/mallorymcp.git
cd mallorymcp
uv sync
uv run mallorymcp
```

### Lint

```bash
uv sync --extra lint
uv run ruff check src/ tests/
uv run ruff format src/ tests/
```

### Project Structure

```
src/mallorymcp/
├── __init__.py
├── _version.py          # Auto-generated by hatch-vcs from git tags
├── app.py               # Entry point (main, stdio transport)
├── config/              # Env-based config (MALLORY_API_KEY, MALLORY_BASE_URL)
├── decorator/           # API error handling for tools
├── server/              # FastMCP server and tool loader
├── tools/               # Tool modules (one per resource area)
└── utils/               # Serialization, debug
```

### Releasing

1. Tag a release: `git tag v0.3.0 && git push --tags`
2. Create a GitHub release from the tag
3. GitHub Actions builds and publishes to PyPI via trusted publisher

## License

Apache 2.0.
