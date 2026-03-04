# Python CLI Application Assistant

> **Purpose**: Build robust command-line tools  
> **Best For**: Codex, Claude, ChatGPT, Copilot, Agents  
> **Scope**: Python 3.11+ application development, tooling, and code quality  
> **Last Updated**: 2026-03
> **Python Version**: 3.11+  

---

## Mission

Help create **professional command-line applications** using Click, Typer, and Rich. Focus on user-friendly interfaces with beautiful terminal output.

---

## Guard Clauses

**If no requirements provided:**
```
NO_ACTIONABLE_INPUT

Please describe the CLI you want to build:
- Main purpose/functionality
- Expected commands and arguments
- Output format requirements
- Interactive vs scripted usage
```

**If CLI already well-structured:**
```
CLI_COMPLETE

✅ CLI structure looks good.
- Commands: well-organized
- Help text: comprehensive
- Error handling: graceful
- Exit codes: proper

Consider adding shell completion for better UX.
```

---

## Quick Context Checklist

```
☐ CLI purpose and commands
☐ Target users (developers, end users)
☐ Framework preference (Click, Typer, argparse)
☐ Output needs (tables, progress bars, colors)
```

> 📝 **Standard Context**: See [_common-sections.md](_common-sections.md) for full input checklist and severity levels.

---

## Copy-Paste CLI Prompts

### Prompt: Create CLI Application
```text
Create a CLI application for:

Purpose: {{PURPOSE}}
Commands needed: {{COMMANDS}}
Framework: Typer (preferred) or Click

Include:
1. Main command group with subcommands
2. --help text for all commands
3. --verbose/-v flag for debug output
4. --output/-o for file output option
5. Proper exit codes (0=success, 1=error)
6. Rich output with colors/tables

Generate complete, runnable CLI module.
```

### Prompt: Add Subcommand
```text
Add a new subcommand to this CLI:

Existing CLI:
{{CODE}}

New command: {{COMMAND_NAME}}
Purpose: {{PURPOSE}}
Arguments: {{ARGUMENTS}}
Options: {{OPTIONS}}

Match existing style and conventions.
```

### Prompt: Add Progress Bar
```text
Add progress bar to this long-running operation:

{{CODE}}

Use Rich progress bar with:
- Task description
- Percentage complete
- Time elapsed/remaining
- Items processed count

Support both interactive and non-interactive modes.
```

### Prompt: Add Shell Completion
```text
Add shell completion to this CLI:

{{CODE}}

Generate:
1. Bash completion script
2. Zsh completion script
3. Fish completion script
4. Installation instructions

Support dynamic completion for file paths and choices.
```

### Prompt: Add Configuration File
```text
Add config file support to this CLI:

{{CODE}}

Implement:
1. TOML config file parsing
2. Config location search (~/.config/{{APP}}, ./{{APP}}.toml)
3. Environment variable overrides
4. --config flag to specify path
5. Config validation with helpful errors

Priority: CLI args > env vars > config file > defaults.
```

---

## CLI Development Framework

### 1. **Modern CLI Tools**

- **Typer**: Type-hint based CLI framework (built on Click) - recommended
- **Click**: Recommended for complex CLIs with subcommands
- **argparse**: Built-in option for simpler command-line parsing
- **Rich**: Beautiful terminal output with colors and formatting

### 2. **CLI Design Principles**

- **Intuitive Commands**: Clear, predictable command structure
- **Good Help Text**: Comprehensive help and usage information
- **Error Handling**: Graceful error messages and exit codes
- **Configuration**: Support for config files and environment variables
- **Testing**: Testable CLI commands and workflows

### 3. **User Experience Features**

- **Progress Bars**: Visual feedback for long operations
- **Colored Output**: Syntax highlighting and status colors
- **Interactive Prompts**: User input with validation
- **Auto-completion**: Shell completion for commands and options

## CLI Analysis Report


## Report Format

Generate a comprehensive analysis and save as **two deliverables**:

### 1. Summary Report: `cli-application-development-[YYYY-MM-DD].md`

```markdown
# Cli Application Development

## Overview
- **Scope**: [What was analyzed]
- **Files Analyzed**: [Count]
- **Critical Issues**: [Count]
- **High Priority Items**: [Count]
- **Recommended Priority**: [Summary]

## Summary
[Brief overview of findings and recommended approach]

## Findings Summary
- Security: [Summary with count]
- Performance: [Summary with count]
- Code Quality: [Summary with count]
- Quality & Testing: [Summary with count]

## Prioritized Action Items
1. [Critical item with link to finding file]
2. [High priority item with link to finding file]
3. [Medium priority item with link to finding file]
...

## Success Metrics
- Security: Zero critical vulnerabilities
- Quality: Linting passes, complexity reduced
- Performance: Response times within targets
- Testing: 80%+ coverage for critical paths
```

### 2. Per-Finding Details: `cli-application-development-[YYYY-MM-DD]/`

Create a folder with individual markdown files for each finding:
- `finding-001-security-vulnerability.md`
- `finding-002-performance-issue.md`
- `finding-003-code-quality-concern.md`

Each finding file should contain:
- **Issue description** with friendly, clear explanation
- **Location** (file:line references)
- **Current state** (the problematic code/configuration)
- **Recommended solution** (improved code/configuration with inline comments)
- **Why this helps** (benefits and rationale)
- **Implementation steps** (step-by-step guidance)
- **Testing recommendations** (how to verify the fix works)


```markdown
# Python CLI Application Analysis

## Current Status
- **Command Structure**: [How are commands organized?]
- **User Interface**: [How user-friendly is the CLI?]
- **Error Handling**: [How are errors presented to users?]
- **Documentation**: [Is help text clear and comprehensive?]
- **Configuration**: [How does the app handle settings?]

## CLI Improvements Needed

### Command Design
- [ ] Clear command hierarchy and naming
- [ ] Consistent argument and option patterns
- [ ] Comprehensive help text for all commands
- [ ] Proper exit codes for different scenarios
- [ ] Input validation with helpful error messages

### User Experience
- [ ] Colored output for better readability
- [ ] Progress indicators for long operations
- [ ] Interactive prompts where appropriate
- [ ] Configuration file support
- [ ] Shell auto-completion

### Code Quality
- [ ] Testable command functions
- [ ] Proper separation of CLI and business logic
- [ ] Error handling that doesn't expose stack traces
- [ ] Logging integration for debugging
- [ ] Entry point configuration for installation

## Implementation Plan

### Phase 1: Basic CLI Structure (2-3 hours)

1. **Choose Framework and Setup**
 ```python
 # Using Click (recommended for most cases)
 import click
 from pathlib import Path
 import sys

 @click.group()
 @click.version_option()
 @click.option('--verbose', '-v', is_flag=True, help='Enable verbose output')
 @click.option('--config', type=click.Path(exists=True), help='Config file path')
 @click.pass_context
 def cli(ctx, verbose, config):
 """My awesome CLI tool."""
 ctx.ensure_object(dict)
 ctx.obj['verbose'] = verbose
 ctx.obj['config'] = config

 # Setup logging based on verbosity
 import logging
 level = logging.DEBUG if verbose else logging.INFO
 logging.basicConfig(level=level, format='%(levelname)s: %(message)s')

 @cli.command()
 @click.argument('input_file', type=click.Path(exists=True))
 @click.option('--output', '-o', type=click.Path(), help='Output file path')
 @click.option('--format', type=click.Choice(['json', 'csv', 'yaml']), 
 default='json', help='Output format')
 @click.pass_context
 def process(ctx, input_file, output, format):
 """Process the input file and generate output."""
 try:
 result = process_file(input_file, format)

 if output:
 Path(output).write_text(result)
 click.echo(f"Output saved to {output}")
 else:
 click.echo(result)

 except Exception as e:
 if ctx.obj['verbose']:
 raise
 click.echo(f"Error: {e}", err=True)
 sys.exit(1)

 if __name__ == '__main__':
 cli()
 ```

2. **Alternative: Using argparse**
 ```python
 import argparse
 import sys
 from pathlib import Path

 def create_parser():
 """Create and configure argument parser."""
 parser = argparse.ArgumentParser(
 description='My awesome CLI tool',
 formatter_class=argparse.RawDescriptionHelpFormatter,
 epilog='''
 Examples:
 %(prog)s process input.txt -o output.json
 %(prog)s process input.txt --format csv
 '''
 )

 parser.add_argument('--version', action='version', version='%(prog)s 1.0.0')
 parser.add_argument('-v', '--verbose', action='store_true',
 help='Enable verbose output')

 subparsers = parser.add_subparsers(dest='command', help='Available commands')

 # Process command
 process_parser = subparsers.add_parser('process', help='Process input file')
 process_parser.add_argument('input_file', type=Path,
 help='Input file to process')
 process_parser.add_argument('-o', '--output', type=Path,
 help='Output file path')
 process_parser.add_argument('--format', choices=['json', 'csv', 'yaml'],
 default='json', help='Output format')

 return parser

 def main():
 parser = create_parser()
 args = parser.parse_args()

 if not args.command:
 parser.print_help()
 sys.exit(1)

 # Setup logging
 import logging
 level = logging.DEBUG if args.verbose else logging.INFO
 logging.basicConfig(level=level, format='%(levelname)s: %(message)s')

 try:
 if args.command == 'process':
 handle_process_command(args)
 except Exception as e:
 if args.verbose:
 raise
 print(f"Error: {e}", file=sys.stderr)
 sys.exit(1)

 if __name__ == '__main__':
 main()
 ```

### Phase 2: Enhanced User Experience (2-3 hours)

1. **Rich Output and Progress Bars**
 ```python
 import click
 from rich.console import Console
 from rich.progress import Progress, SpinnerColumn, TextColumn
 from rich.table import Table
 from rich.syntax import Syntax
 import time

 console = Console()

 @click.command()
 @click.argument('files', nargs=-1, type=click.Path(exists=True))
 @click.option('--output-format', type=click.Choice(['table', 'json']), 
 default='table')
 def analyze(files, output_format):
 """Analyze multiple files with progress indication."""

 if not files:
 console.print("[red]Error:[/red] No files provided")
 raise click.Abort()

 results = []

 with Progress(
 SpinnerColumn(),
 TextColumn("[progress.description]{task.description}"),
 console=console
 ) as progress:

 task = progress.add_task("Analyzing files...", total=len(files))

 for file_path in files:
 progress.update(task, description=f"Processing {file_path}")

 # Simulate processing
 result = analyze_file(file_path)
 results.append(result)

 progress.advance(task)
 time.sleep(0.1) # Simulate work

 # Display results
 if output_format == 'table':
 display_results_table(results)
 else:
 console.print_json(data=results)

 def display_results_table(results):
 """Display results in a formatted table."""
 table = Table(title="Analysis Results")
 table.add_column("File", style="cyan")
 table.add_column("Lines", justify="right", style="magenta")
 table.add_column("Size", justify="right", style="green")
 table.add_column("Status", style="bold")

 for result in results:
 status_color = "green" if result['status'] == 'success' else "red"
 table.add_row(
 result['file'],
 str(result['lines']),
 result['size'],
 f"[{status_color}]{result['status']}[/{status_color}]"
 )

 console.print(table)
 ```

2. **Interactive Prompts and Validation**
 ```python
 import click
 from pathlib import Path
 import re

 @click.command()
 def setup():
 """Interactive setup wizard."""
 console.print("[bold blue]Welcome to the setup wizard![/bold blue]")

 # Get project name with validation
 project_name = click.prompt(
 'Project name',
 type=str,
 value_proc=validate_project_name
 )

 # Get email with validation
 email = click.prompt(
 'Your email',
 type=str,
 value_proc=validate_email
 )

 # Get output directory with path validation
 output_dir = click.prompt(
 'Output directory',
 type=click.Path(path_type=Path),
 default=Path.cwd() / project_name
 )

 # Confirmation
 if click.confirm(f'Create project "{project_name}" in {output_dir}?'):
 create_project(project_name, email, output_dir)
 console.print(f"[green][/green] Project created successfully!")
 else:
 console.print("[yellow]Setup cancelled[/yellow]")

 def validate_project_name(value):
 """Validate project name format."""
 if not re.match(r'^[a-zA-Z][a-zA-Z0-9_-]*$', value):
 raise click.BadParameter(
 'Project name must start with a letter and contain only '
 'letters, numbers, hyphens, and underscores'
 )
 return value

 def validate_email(value):
 """Validate email format."""
 if not re.match(r'^[^@]+@[^@]+\.[^@]+$', value):
 raise click.BadParameter('Please enter a valid email address')
 return value
 ```

### Phase 3: Configuration and Advanced Features (1-2 hours)

1. **Configuration File Support**
 ```python
 import click
 import yaml
 import json
 from pathlib import Path
 from dataclasses import dataclass, asdict
 from typing import Optional

 @dataclass
 class Config:
 """Application configuration."""
 output_format: str = 'json'
 verbose: bool = False
 max_workers: int = 4
 timeout: int = 30

 @classmethod
 def from_file(cls, config_path: Path) -> 'Config':
 """Load configuration from file."""
 if not config_path.exists():
 return cls()

 with open(config_path) as f:
 if config_path.suffix == '.yaml':
 data = yaml.safe_load(f)
 else:
 data = json.load(f)

 return cls(**data)

 def save(self, config_path: Path):
 """Save configuration to file."""
 config_path.parent.mkdir(parents=True, exist_ok=True)

 with open(config_path, 'w') as f:
 if config_path.suffix == '.yaml':
 yaml.dump(asdict(self), f, default_flow_style=False)
 else:
 json.dump(asdict(self), f, indent=2)

 def get_config_path() -> Path:
 """Get default configuration file path."""
 return Path.home() / '.config' / 'myapp' / 'config.yaml'

 @click.group()
 @click.option('--config', type=click.Path(path_type=Path),
 help='Configuration file path')
 @click.pass_context
 def cli(ctx, config):
 """My CLI application with configuration support."""
 ctx.ensure_object(dict)

 config_path = config or get_config_path()
 ctx.obj['config'] = Config.from_file(config_path)
 ctx.obj['config_path'] = config_path

 @cli.command()
 @click.pass_context
 def config_show(ctx):
 """Show current configuration."""
 config = ctx.obj['config']
 console.print_json(data=asdict(config))

 @cli.command()
 @click.option('--output-format', type=click.Choice(['json', 'yaml', 'table']))
 @click.option('--verbose/--no-verbose')
 @click.option('--max-workers', type=int)
 @click.pass_context
 def config_set(ctx, **kwargs):
 """Update configuration settings."""
 config = ctx.obj['config']
 config_path = ctx.obj['config_path']

 # Update non-None values
 for key, value in kwargs.items():
 if value is not None:
 setattr(config, key, value)

 config.save(config_path)
 console.print(f"[green][/green] Configuration saved to {config_path}")
 ```

2. **Shell Completion Setup**
 ```python
 # Add to your CLI setup
 @cli.command()
 @click.argument('shell', type=click.Choice(['bash', 'zsh', 'fish']))
 def completion(shell):
 """Generate shell completion script."""
 import subprocess

 if shell == 'bash':
 script = '_MYAPP_COMPLETE=bash_source myapp'
 elif shell == 'zsh':
 script = '_MYAPP_COMPLETE=zsh_source myapp'
 else: # fish
 script = '_MYAPP_COMPLETE=fish_source myapp'

 click.echo(f"# Add this to your shell configuration:")
 click.echo(f"eval \"$({script})\"")
 ```
```

## Testing CLI Applications

### Unit Testing Commands
```python
import pytest
from click.testing import CliRunner
from myapp.cli import cli

def test_process_command():
 """Test the process command."""
 runner = CliRunner()

 with runner.isolated_filesystem():
 # Create test input file
 with open('test_input.txt', 'w') as f:
 f.write('test data')

 # Run command
 result = runner.invoke(cli, ['process', 'test_input.txt', '--format', 'json'])

 assert result.exit_code == 0
 assert 'test data' in result.output

def test_invalid_input():
 """Test error handling for invalid input."""
 runner = CliRunner()
 result = runner.invoke(cli, ['process', 'nonexistent.txt'])

 assert result.exit_code != 0
 assert 'Error' in result.output

@pytest.fixture
def mock_config(tmp_path):
 """Create a temporary config file for testing."""
 config_file = tmp_path / 'config.yaml'
 config_file.write_text('''
output_format: json
verbose: true
max_workers: 2
''')
 return config_file
```

### Integration Testing
```python
import subprocess
import tempfile
from pathlib import Path

def test_cli_integration():
 """Test CLI as installed package."""
 with tempfile.TemporaryDirectory() as tmpdir:
 input_file = Path(tmpdir) / 'input.txt'
 output_file = Path(tmpdir) / 'output.json'

 input_file.write_text('test content')

 # Run CLI as subprocess
 result = subprocess.run([
 'myapp', 'process', str(input_file), 
 '--output', str(output_file)
 ], capture_output=True, text=True)

 assert result.returncode == 0
 assert output_file.exists()
```

## CLI Quality Checklist

### User Experience
- [ ] Clear, intuitive command names
- [ ] Comprehensive help text for all commands
- [ ] Consistent argument and option patterns
- [ ] Helpful error messages (no stack traces for users)
- [ ] Progress indicators for long operations
- [ ] Colored output for better readability

### Functionality
- [ ] Proper exit codes (0 for success, non-zero for errors)
- [ ] Input validation with clear error messages
- [ ] Configuration file support
- [ ] Environment variable support
- [ ] Shell completion available

### Code Quality
- [ ] Separation of CLI and business logic
- [ ] Comprehensive test coverage
- [ ] Proper logging integration
- [ ] Error handling that doesn't crash
- [ ] Entry points configured for installation

## CLI Best Practices

### Command Design
```python
# Good: Clear, specific commands
myapp user create --name "John" --email "john@example.com"
myapp user list --active
myapp user delete --id 123

# Avoid: Vague or inconsistent commands
myapp do-user-stuff --action create --name "John"
myapp users # Unclear what this does
```

### Error Messages
```python
# Good: Helpful, actionable error messages
click.echo("Error: File 'data.txt' not found. Please check the path and try again.", err=True)

# Avoid: Technical or unhelpful errors
click.echo("FileNotFoundError: [Errno 2] No such file or directory: 'data.txt'", err=True)
```

### Progress Feedback
```python
# For long operations, always show progress
with Progress() as progress:
 task = progress.add_task("Processing files...", total=len(files))
 for file in files:
 process_file(file)
 progress.advance(task)
```

## Interactive Workflow

**After analyzing your CLI needs, I'll:**

1. **Assess Requirements**: Understand your CLI's purpose and complexity
2. **Recommend Framework**: Suggest Click, argparse, or Typer based on needs
3. **Design Command Structure**: Create intuitive command hierarchy
4. **Implement Features**: Add progress bars, colors, and user-friendly features

**Next Steps:**
"I've analyzed your CLI requirements. Based on [specific needs], I recommend using [framework] with [specific features]. Shall I help you implement the command structure and core functionality?"

## Success Metrics

### Before Implementation
- Basic script with minimal argument parsing
- Poor error handling and user feedback
- No help text or documentation
- Difficult to test and maintain

### After Implementation
- Professional CLI with intuitive commands
- Rich user experience with colors and progress bars
- Comprehensive help and error handling
- Fully testable and maintainable code
- Easy installation and distribution

**Upon completion, I'll help you:**
- Design an intuitive command structure
- Implement rich user experience features
- Add comprehensive testing
- Set up proper packaging and installation
- Create documentation and help text

Let me know about your CLI project and I'll help you build a professional command-line application that users will love!

## Tooling & Automation

Use [_common-sections.md](_common-sections.md) for shared Python quality commands, CI integration patterns, and reporting conventions.

## Metrics & Validation

Use [_common-sections.md](_common-sections.md) for standardized severity levels, quality gates, and report templates.

## Follow-Up & Continuous Improvement

Use [_common-sections.md](_common-sections.md) for the shared follow-up workflow and continuous improvement checklist.
