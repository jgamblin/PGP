# MCP Server Development — Model Context Protocol

> **Purpose**: Build production-ready MCP servers for AI tools  
> **Best For**: Codex, Claude, ChatGPT, Copilot, Agents  
> **Scope**: Tool design, server implementation, deployment  
> **Last Updated**: 2026-03

---

## Mission

Help build **robust, well-designed MCP servers** that extend AI capabilities with custom tools, resources, and prompts. Focus on clean interfaces, proper error handling, and excellent developer experience.

---

## Guard Clauses

**If no MCP context provided:**
```
NO_MCP_CONTEXT

Please provide context:
- What tools/capabilities should the server expose?
- What data/resources should be accessible?
- Target AI clients (Claude, Copilot, etc.)
- Or describe your use case
```

**If MCP server is well-designed:**
```
MCP_SERVER_APPROVED

✅ MCP server review complete — production ready.

Checks performed:
- Tool design: ✓ (clear names, good descriptions)
- Error handling: ✓ (graceful failures, informative messages)
- Security: ✓ (input validation, safe operations)
- DX: ✓ (typed schemas, documentation)

MCP server follows best practices.
```

---

## Quick Context Checklist

```
☐ Tools to expose
☐ Resources to provide
☐ Authentication needs
☐ Rate limiting requirements
☐ Error handling strategy
☐ Logging/monitoring
☐ Deployment target
☐ Client compatibility
```

---

## Copy-Paste Prompts

### Prompt: Design MCP Server
```text
Design an MCP server for:

Purpose: {{PURPOSE}}
Target clients: {{CLIENTS}}
Environment: {{ENVIRONMENT}}

Capabilities needed:
- {{CAPABILITY_1}}
- {{CAPABILITY_2}}
- {{CAPABILITY_3}}

Generate:
1. Tool definitions with schemas
2. Resource definitions
3. Error handling strategy
4. Server implementation
5. Deployment configuration
6. Example usage
```

### Prompt: Review MCP Server
```text
Review this MCP server implementation:

{{CODE}}

Check for:
1. **Tool Design**
   - Clear, descriptive names
   - Complete input schemas
   - Good descriptions
   - Appropriate return types

2. **Error Handling**
   - Input validation
   - Graceful failures
   - Informative messages
   - Recovery strategies

3. **Security**
   - Input sanitization
   - Safe file operations
   - Rate limiting
   - Authentication

4. **DX**
   - TypeScript types
   - Documentation
   - Examples
   - Testing

Rate each: 🟢 Good | 🟡 Needs attention | 🔴 Critical issue
```

### Prompt: Add Tool to Server
```text
Add a new tool to this MCP server:

Existing server:
{{CODE}}

New tool requirements:
- Name: {{TOOL_NAME}}
- Purpose: {{PURPOSE}}
- Inputs: {{INPUTS}}
- Output: {{OUTPUT}}

Generate:
1. Tool definition
2. Handler implementation
3. Input validation
4. Error handling
5. Tests
6. Documentation
```

---

## MCP Server Templates

### Python MCP Server (Complete)
```python
# server.py
"""
MCP Server: {{SERVER_NAME}}

A Model Context Protocol server that provides:
- {{CAPABILITY_1}}
- {{CAPABILITY_2}}
"""

from __future__ import annotations

import asyncio
import json
import logging
from contextlib import asynccontextmanager
from dataclasses import dataclass
from enum import Enum
from typing import Any, Sequence

from mcp.server import Server
from mcp.server.models import InitializationOptions
from mcp.server.stdio import stdio_server
from mcp.types import (
    CallToolResult,
    GetPromptResult,
    ListPromptsResult,
    ListResourcesResult,
    ListToolsResult,
    Prompt,
    PromptArgument,
    PromptMessage,
    ReadResourceResult,
    Resource,
    TextContent,
    Tool,
)
from pydantic import BaseModel, Field, ValidationError


# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


# ============================================
# Tool Input Schemas
# ============================================

class SearchInput(BaseModel):
    """Input schema for search tool."""
    query: str = Field(description="The search query")
    limit: int = Field(default=10, ge=1, le=100, description="Max results")
    

class FileReadInput(BaseModel):
    """Input schema for file read tool."""
    path: str = Field(description="Path to the file")
    encoding: str = Field(default="utf-8", description="File encoding")


class AnalyzeInput(BaseModel):
    """Input schema for analyze tool."""
    content: str = Field(description="Content to analyze")
    analysis_type: str = Field(
        description="Type of analysis: 'summary', 'sentiment', 'entities'"
    )


# ============================================
# Tool Handlers
# ============================================

async def handle_search(query: str, limit: int = 10) -> dict[str, Any]:
    """
    Search for information.
    
    Args:
        query: The search query
        limit: Maximum number of results
        
    Returns:
        Search results with relevance scores
    """
    logger.info(f"Searching for: {query} (limit: {limit})")
    
    # TODO: Implement actual search logic
    results = [
        {"title": f"Result {i}", "score": 0.9 - i * 0.1}
        for i in range(min(limit, 5))
    ]
    
    return {
        "query": query,
        "total": len(results),
        "results": results,
    }


async def handle_file_read(path: str, encoding: str = "utf-8") -> dict[str, Any]:
    """
    Read a file and return its contents.
    
    Args:
        path: Path to the file
        encoding: File encoding
        
    Returns:
        File contents and metadata
    """
    import os
    
    # Security: Validate path
    if ".." in path or path.startswith("/"):
        raise ValueError("Invalid path: must be relative without '..'")
    
    # Check allowed paths
    allowed_paths = os.environ.get("MCP_ALLOWED_PATHS", ".").split(",")
    if not any(path.startswith(p) for p in allowed_paths):
        raise PermissionError(f"Path not in allowed paths: {allowed_paths}")
    
    try:
        with open(path, encoding=encoding) as f:
            content = f.read()
        
        return {
            "path": path,
            "size": len(content),
            "content": content,
        }
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {path}")
    except UnicodeDecodeError:
        raise ValueError(f"Cannot decode file with encoding: {encoding}")


async def handle_analyze(content: str, analysis_type: str) -> dict[str, Any]:
    """
    Analyze content.
    
    Args:
        content: Content to analyze
        analysis_type: Type of analysis
        
    Returns:
        Analysis results
    """
    valid_types = ["summary", "sentiment", "entities"]
    if analysis_type not in valid_types:
        raise ValueError(f"Invalid analysis_type. Must be one of: {valid_types}")
    
    # TODO: Implement actual analysis
    return {
        "type": analysis_type,
        "input_length": len(content),
        "result": f"Analysis result for {analysis_type}",
    }


# ============================================
# Resource Handlers
# ============================================

async def get_config_resource() -> str:
    """Get server configuration as a resource."""
    import os
    
    config = {
        "version": "1.0.0",
        "allowed_paths": os.environ.get("MCP_ALLOWED_PATHS", "."),
        "max_file_size": os.environ.get("MCP_MAX_FILE_SIZE", "10MB"),
    }
    
    return json.dumps(config, indent=2)


async def get_status_resource() -> str:
    """Get server status as a resource."""
    import platform
    
    status = {
        "status": "healthy",
        "python_version": platform.python_version(),
        "platform": platform.system(),
    }
    
    return json.dumps(status, indent=2)


# ============================================
# MCP Server Setup
# ============================================

# Tool definitions
TOOLS: list[Tool] = [
    Tool(
        name="search",
        description="Search for information. Returns relevant results with scores.",
        inputSchema=SearchInput.model_json_schema(),
    ),
    Tool(
        name="read_file",
        description="Read a file from the allowed paths. Returns file contents.",
        inputSchema=FileReadInput.model_json_schema(),
    ),
    Tool(
        name="analyze",
        description="Analyze content. Supports: summary, sentiment, entities.",
        inputSchema=AnalyzeInput.model_json_schema(),
    ),
]

# Resource definitions
RESOURCES: list[Resource] = [
    Resource(
        uri="config://server",
        name="Server Configuration",
        description="Current server configuration and limits",
        mimeType="application/json",
    ),
    Resource(
        uri="status://server",
        name="Server Status",
        description="Current server health status",
        mimeType="application/json",
    ),
]

# Prompt definitions
PROMPTS: list[Prompt] = [
    Prompt(
        name="analyze_document",
        description="Analyze a document comprehensively",
        arguments=[
            PromptArgument(
                name="document",
                description="The document content to analyze",
                required=True,
            ),
            PromptArgument(
                name="focus",
                description="What to focus on (optional)",
                required=False,
            ),
        ],
    ),
]


def create_server() -> Server:
    """Create and configure the MCP server."""
    server = Server("example-server")
    
    @server.list_tools()
    async def list_tools() -> list[Tool]:
        """List available tools."""
        return TOOLS
    
    @server.call_tool()
    async def call_tool(name: str, arguments: dict) -> Sequence[TextContent]:
        """Handle tool calls."""
        logger.info(f"Tool call: {name} with {arguments}")
        
        try:
            if name == "search":
                validated = SearchInput(**arguments)
                result = await handle_search(validated.query, validated.limit)
            elif name == "read_file":
                validated = FileReadInput(**arguments)
                result = await handle_file_read(validated.path, validated.encoding)
            elif name == "analyze":
                validated = AnalyzeInput(**arguments)
                result = await handle_analyze(validated.content, validated.analysis_type)
            else:
                raise ValueError(f"Unknown tool: {name}")
            
            return [TextContent(type="text", text=json.dumps(result, indent=2))]
            
        except ValidationError as e:
            error_msg = f"Invalid input: {e.errors()}"
            logger.error(error_msg)
            return [TextContent(type="text", text=json.dumps({"error": error_msg}))]
        except Exception as e:
            error_msg = f"Tool error: {type(e).__name__}: {str(e)}"
            logger.error(error_msg)
            return [TextContent(type="text", text=json.dumps({"error": error_msg}))]
    
    @server.list_resources()
    async def list_resources() -> list[Resource]:
        """List available resources."""
        return RESOURCES
    
    @server.read_resource()
    async def read_resource(uri: str) -> str:
        """Read a resource by URI."""
        logger.info(f"Resource read: {uri}")
        
        if uri == "config://server":
            return await get_config_resource()
        elif uri == "status://server":
            return await get_status_resource()
        else:
            raise ValueError(f"Unknown resource: {uri}")
    
    @server.list_prompts()
    async def list_prompts() -> list[Prompt]:
        """List available prompts."""
        return PROMPTS
    
    @server.get_prompt()
    async def get_prompt(name: str, arguments: dict | None) -> GetPromptResult:
        """Get a prompt by name."""
        if name == "analyze_document":
            document = (arguments or {}).get("document", "")
            focus = (arguments or {}).get("focus", "general analysis")
            
            return GetPromptResult(
                description="Comprehensive document analysis",
                messages=[
                    PromptMessage(
                        role="user",
                        content=TextContent(
                            type="text",
                            text=f"Analyze this document with focus on {focus}:\n\n{document}",
                        ),
                    ),
                ],
            )
        
        raise ValueError(f"Unknown prompt: {name}")
    
    return server


async def main():
    """Run the MCP server."""
    server = create_server()
    
    async with stdio_server() as (read_stream, write_stream):
        logger.info("Starting MCP server...")
        await server.run(
            read_stream,
            write_stream,
            InitializationOptions(
                server_name="example-server",
                server_version="1.0.0",
                capabilities=server.get_capabilities(
                    notification_options=None,
                    experimental_capabilities={},
                ),
            ),
        )


if __name__ == "__main__":
    asyncio.run(main())
```

### TypeScript MCP Server
```typescript
// server.ts
import { Server } from "@modelcontextprotocol/sdk/server/index.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import {
  CallToolRequestSchema,
  ListToolsRequestSchema,
  ListResourcesRequestSchema,
  ReadResourceRequestSchema,
  Tool,
  Resource,
} from "@modelcontextprotocol/sdk/types.js";
import { z } from "zod";

// ============================================
// Input Schemas
// ============================================

const SearchInputSchema = z.object({
  query: z.string().describe("The search query"),
  limit: z.number().min(1).max(100).default(10).describe("Max results"),
});

const FileReadInputSchema = z.object({
  path: z.string().describe("Path to the file"),
  encoding: z.string().default("utf-8").describe("File encoding"),
});

// ============================================
// Tool Handlers
// ============================================

async function handleSearch(
  query: string,
  limit: number = 10
): Promise<object> {
  console.error(`Searching for: ${query} (limit: ${limit})`);
  
  // TODO: Implement actual search
  const results = Array.from({ length: Math.min(limit, 5) }, (_, i) => ({
    title: `Result ${i}`,
    score: 0.9 - i * 0.1,
  }));
  
  return { query, total: results.length, results };
}

async function handleFileRead(
  path: string,
  encoding: BufferEncoding = "utf-8"
): Promise<object> {
  const fs = await import("fs/promises");
  
  // Security: Validate path
  if (path.includes("..") || path.startsWith("/")) {
    throw new Error("Invalid path: must be relative without '..'");
  }
  
  const content = await fs.readFile(path, { encoding });
  
  return { path, size: content.length, content };
}

// ============================================
// Resource Handlers
// ============================================

async function getConfigResource(): Promise<string> {
  return JSON.stringify(
    {
      version: "1.0.0",
      allowedPaths: process.env.MCP_ALLOWED_PATHS || ".",
    },
    null,
    2
  );
}

// ============================================
// Server Setup
// ============================================

const tools: Tool[] = [
  {
    name: "search",
    description: "Search for information. Returns relevant results with scores.",
    inputSchema: {
      type: "object",
      properties: {
        query: { type: "string", description: "The search query" },
        limit: { type: "number", description: "Max results", default: 10 },
      },
      required: ["query"],
    },
  },
  {
    name: "read_file",
    description: "Read a file from allowed paths.",
    inputSchema: {
      type: "object",
      properties: {
        path: { type: "string", description: "Path to the file" },
        encoding: { type: "string", description: "File encoding", default: "utf-8" },
      },
      required: ["path"],
    },
  },
];

const resources: Resource[] = [
  {
    uri: "config://server",
    name: "Server Configuration",
    description: "Current server configuration",
    mimeType: "application/json",
  },
];

async function main() {
  const server = new Server(
    { name: "example-server", version: "1.0.0" },
    { capabilities: { tools: {}, resources: {} } }
  );

  // List tools
  server.setRequestHandler(ListToolsRequestSchema, async () => ({
    tools,
  }));

  // Call tool
  server.setRequestHandler(CallToolRequestSchema, async (request) => {
    const { name, arguments: args } = request.params;
    
    try {
      let result: object;
      
      switch (name) {
        case "search": {
          const input = SearchInputSchema.parse(args);
          result = await handleSearch(input.query, input.limit);
          break;
        }
        case "read_file": {
          const input = FileReadInputSchema.parse(args);
          result = await handleFileRead(input.path, input.encoding as BufferEncoding);
          break;
        }
        default:
          throw new Error(`Unknown tool: ${name}`);
      }
      
      return {
        content: [{ type: "text", text: JSON.stringify(result, null, 2) }],
      };
    } catch (error) {
      const message = error instanceof Error ? error.message : String(error);
      return {
        content: [{ type: "text", text: JSON.stringify({ error: message }) }],
        isError: true,
      };
    }
  });

  // List resources
  server.setRequestHandler(ListResourcesRequestSchema, async () => ({
    resources,
  }));

  // Read resource
  server.setRequestHandler(ReadResourceRequestSchema, async (request) => {
    const { uri } = request.params;
    
    if (uri === "config://server") {
      return {
        contents: [{ uri, mimeType: "application/json", text: await getConfigResource() }],
      };
    }
    
    throw new Error(`Unknown resource: ${uri}`);
  });

  // Start server
  const transport = new StdioServerTransport();
  await server.connect(transport);
  console.error("MCP server running on stdio");
}

main().catch(console.error);
```

---

## Tool Design Guidelines

### Good Tool Design
```python
# ✅ Good: Clear name, comprehensive schema, helpful description
Tool(
    name="search_codebase",
    description="""Search the codebase for code matching a query.
    
Returns matching files with:
- File path and line numbers
- Relevance score
- Code snippets with context

Supports regex and semantic search.""",
    inputSchema={
        "type": "object",
        "properties": {
            "query": {
                "type": "string",
                "description": "Search query (supports regex with /pattern/)",
            },
            "file_pattern": {
                "type": "string",
                "description": "Glob pattern for files, e.g., '**/*.py'",
                "default": "**/*",
            },
            "max_results": {
                "type": "integer",
                "description": "Maximum results to return",
                "default": 20,
                "minimum": 1,
                "maximum": 100,
            },
            "include_context": {
                "type": "boolean",
                "description": "Include surrounding code lines",
                "default": True,
            },
        },
        "required": ["query"],
    },
)

# ❌ Bad: Vague name, missing description, minimal schema
Tool(
    name="search",
    description="Search stuff",
    inputSchema={
        "type": "object",
        "properties": {
            "q": {"type": "string"},
        },
    },
)
```

### Error Handling Patterns
```python
# Comprehensive error handling
async def handle_tool(name: str, args: dict) -> list[TextContent]:
    """Handle tool calls with proper error handling."""
    try:
        # Validate inputs
        schema = get_schema_for_tool(name)
        validated = schema(**args)
        
        # Execute with timeout
        result = await asyncio.wait_for(
            execute_tool(name, validated),
            timeout=30.0,
        )
        
        return [TextContent(type="text", text=json.dumps(result, indent=2))]
        
    except ValidationError as e:
        # Input validation failed
        return [TextContent(
            type="text",
            text=json.dumps({
                "error": "validation_error",
                "message": "Invalid input parameters",
                "details": e.errors(),
            }),
        )]
        
    except asyncio.TimeoutError:
        # Operation timed out
        return [TextContent(
            type="text",
            text=json.dumps({
                "error": "timeout",
                "message": f"Tool '{name}' timed out after 30 seconds",
            }),
        )]
        
    except PermissionError as e:
        # Security violation
        return [TextContent(
            type="text",
            text=json.dumps({
                "error": "permission_denied",
                "message": str(e),
            }),
        )]
        
    except Exception as e:
        # Unexpected error
        logger.exception(f"Tool error: {name}")
        return [TextContent(
            type="text",
            text=json.dumps({
                "error": "internal_error",
                "message": f"An unexpected error occurred: {type(e).__name__}",
            }),
        )]
```

---

## Security Patterns

### Input Sanitization
```python
import re
from pathlib import Path


def sanitize_path(path: str, allowed_roots: list[str]) -> Path:
    """Sanitize and validate a file path."""
    # Resolve to absolute path
    resolved = Path(path).resolve()
    
    # Check against allowed roots
    for root in allowed_roots:
        root_path = Path(root).resolve()
        try:
            resolved.relative_to(root_path)
            return resolved
        except ValueError:
            continue
    
    raise PermissionError(f"Path '{path}' is not within allowed directories")


def sanitize_command(command: str, allowed_commands: list[str]) -> str:
    """Sanitize a shell command."""
    # Extract base command
    base = command.split()[0] if command else ""
    
    if base not in allowed_commands:
        raise PermissionError(f"Command '{base}' is not allowed")
    
    # Check for shell injection patterns
    dangerous_patterns = [
        r"[;&|`$]",  # Shell operators
        r"\$\(",      # Command substitution
        r"\${",       # Variable expansion
        r">\s*&",     # Redirect to fd
    ]
    
    for pattern in dangerous_patterns:
        if re.search(pattern, command):
            raise ValueError(f"Command contains dangerous pattern: {pattern}")
    
    return command
```

### Rate Limiting
```python
import time
from collections import defaultdict
from dataclasses import dataclass


@dataclass
class RateLimitConfig:
    """Rate limit configuration."""
    requests_per_minute: int = 60
    requests_per_hour: int = 1000
    burst_limit: int = 10


class RateLimiter:
    """Simple rate limiter for MCP tools."""
    
    def __init__(self, config: RateLimitConfig | None = None):
        self.config = config or RateLimitConfig()
        self._minute_counts: dict[str, list[float]] = defaultdict(list)
        self._hour_counts: dict[str, list[float]] = defaultdict(list)
    
    def check(self, tool_name: str) -> bool:
        """Check if request is allowed."""
        now = time.time()
        minute_ago = now - 60
        hour_ago = now - 3600
        
        # Clean old entries
        self._minute_counts[tool_name] = [
            t for t in self._minute_counts[tool_name] if t > minute_ago
        ]
        self._hour_counts[tool_name] = [
            t for t in self._hour_counts[tool_name] if t > hour_ago
        ]
        
        # Check limits
        if len(self._minute_counts[tool_name]) >= self.config.requests_per_minute:
            return False
        if len(self._hour_counts[tool_name]) >= self.config.requests_per_hour:
            return False
        
        return True
    
    def record(self, tool_name: str) -> None:
        """Record a request."""
        now = time.time()
        self._minute_counts[tool_name].append(now)
        self._hour_counts[tool_name].append(now)
```

---

## Deployment Configuration

### Docker
```dockerfile
# Dockerfile
FROM python:3.12-slim

WORKDIR /app

# Install dependencies
COPY pyproject.toml .
RUN pip install uv && uv pip install --system .

# Copy source
COPY . .

# Run server
CMD ["python", "-m", "server"]
```

### Claude Desktop Config
```json
{
  "mcpServers": {
    "my-server": {
      "command": "python",
      "args": ["-m", "server"],
      "cwd": "/path/to/server",
      "env": {
        "MCP_ALLOWED_PATHS": "./data,./config",
        "MCP_LOG_LEVEL": "INFO"
      }
    }
  }
}
```

### VS Code MCP Config
```json
{
  "mcp": {
    "servers": {
      "my-server": {
        "command": "npx",
        "args": ["tsx", "server.ts"],
        "env": {
          "NODE_ENV": "production"
        }
      }
    }
  }
}
```

---

## Testing MCP Servers

```python
# test_server.py
import pytest
from server import create_server, handle_search, handle_file_read


@pytest.fixture
def server():
    """Create test server."""
    return create_server()


class TestTools:
    """Test tool handlers."""
    
    @pytest.mark.asyncio
    async def test_search_returns_results(self):
        """Test search tool returns expected structure."""
        result = await handle_search("test query", limit=5)
        
        assert "query" in result
        assert "results" in result
        assert len(result["results"]) <= 5
    
    @pytest.mark.asyncio
    async def test_search_respects_limit(self):
        """Test search respects limit parameter."""
        result = await handle_search("test", limit=3)
        
        assert len(result["results"]) <= 3
    
    @pytest.mark.asyncio
    async def test_file_read_rejects_absolute_path(self):
        """Test file read rejects absolute paths."""
        with pytest.raises(ValueError, match="Invalid path"):
            await handle_file_read("/etc/passwd")
    
    @pytest.mark.asyncio
    async def test_file_read_rejects_traversal(self):
        """Test file read rejects path traversal."""
        with pytest.raises(ValueError, match="Invalid path"):
            await handle_file_read("../../../etc/passwd")


class TestIntegration:
    """Integration tests with actual MCP protocol."""
    
    @pytest.mark.asyncio
    async def test_list_tools(self, server):
        """Test listing tools returns all tools."""
        tools = await server.list_tools()
        
        assert len(tools) >= 2
        names = [t.name for t in tools]
        assert "search" in names
    
    @pytest.mark.asyncio
    async def test_call_tool(self, server):
        """Test calling a tool."""
        result = await server.call_tool("search", {"query": "test"})
        
        assert result is not None
        assert len(result) > 0
```

---

## Report Template

```markdown
# MCP Server Review — {{SERVER_NAME}}

**Date**: {{DATE}}
**Version**: {{VERSION}}

## Summary

| Aspect | Status | Notes |
|--------|--------|-------|
| Tool Design | 🟢/🟡/🔴 | {{NOTES}} |
| Error Handling | 🟢/🟡/🔴 | {{NOTES}} |
| Security | 🟢/🟡/🔴 | {{NOTES}} |
| DX | 🟢/🟡/🔴 | {{NOTES}} |

## Tools Provided
{{TOOLS_LIST}}

## Resources Provided
{{RESOURCES_LIST}}

## Issues Found
{{ISSUES}}

## Recommendations
{{RECOMMENDATIONS}}
```

---

## Best Practices Checklist

### Tool Design
- [ ] Clear, descriptive names
- [ ] Comprehensive descriptions
- [ ] Complete input schemas
- [ ] Appropriate defaults

### Error Handling
- [ ] Input validation
- [ ] Graceful failures
- [ ] Informative messages
- [ ] Timeout handling

### Security
- [ ] Input sanitization
- [ ] Path validation
- [ ] Rate limiting
- [ ] Logging

### Developer Experience
- [ ] TypeScript types / Pydantic models
- [ ] Good documentation
- [ ] Example usage
- [ ] Tests

---

## Severity Guide

| Level | Icon | Examples |
|-------|------|----------|
| **Critical** | 🔴 | No input validation, path traversal, no error handling |
| **High** | 🟠 | Missing schemas, poor descriptions, no timeouts |
| **Medium** | 🟡 | Missing defaults, limited logging |
| **Low** | 🟢 | Documentation gaps, minor naming issues |
