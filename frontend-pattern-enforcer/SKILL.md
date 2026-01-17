---
name: frontend-pattern-enforcer
description: "Use for ANY frontend development work - creating components, writing code, styling, or working with React, Vue, Angular, TypeScript, JavaScript, CSS, Tailwind, Shadcn, or any web UI framework. Automatically analyzes existing project patterns and enforces consistency in design tokens, component structure, naming conventions, and code organization. Always loads when user works on frontend code to ensure new code matches existing project patterns. Triggers on component creation, code writing, styling, refactoring, file creation, or any frontend development task."
---

# Frontend Pattern Enforcer

This skill ensures new frontend components strictly follow existing project patterns by analyzing the codebase and enforcing consistency in design tokens, component structure, naming conventions, and folder organization.

## Automatic Workflow

**This skill automatically activates for ANY frontend work.** When the user works on frontend code, Claude should:

1. **Auto-detect the project** from context or ask for project path
2. **Check if patterns exist** - Look for `project_patterns.json` in the conversation history or project
3. **If patterns don't exist** - Automatically analyze the project first
4. **Then proceed** with the user's request while following extracted patterns

**Key principle:** ALWAYS ensure patterns are analyzed before creating/modifying code. The user should not have to explicitly request pattern analysis.

## Trigger Scenarios

This skill activates automatically when user:
- Creates a new component ("Create a Button component")
- Writes any frontend code ("Add a modal to the page")
- Works with CSS/styling ("Style this card")
- Modifies existing components
- Asks about code organization
- Works with React, Vue, Angular, or any frontend framework
- Uses TypeScript, JavaScript, Tailwind, CSS, etc.

**If user is working in a frontend project, this skill is active.**

## Core Workflow

### Pattern Analysis (Runs Automatically)

**Claude handles this automatically** - users don't need to request it explicitly.

When a user starts frontend work, Claude should:

1. **Detect project path** from context or ask once
2. **Check if analysis exists** in conversation history
3. **If not analyzed:**
   - Automatically run: `python scripts/analyze_project.py /path/to/project project_patterns.json`
   - Generate report: `python scripts/generate_report.py project_patterns.json project_patterns.md`
   - Store patterns in context for the conversation
4. **Use patterns** for all subsequent requests

Claude will automatically detect whether to use `python` or `python3`:
- If `python3` exists → uses `python3`
- If `python` exists → uses `python`
- Works on all systems!

**What gets extracted automatically:**
- Design tokens (colors, shadows, radii, spacing)
- Folder structure conventions
- Component patterns (TypeScript usage, Props interfaces, exports)
- Naming conventions (PascalCase, kebab-case, etc.)
- Import patterns (path aliases vs relative imports)

### Creating Components: Patterns Applied Automatically

When user requests a component (e.g., "Create a Button component"), Claude automatically:

1. **Checks patterns** - Uses stored analysis from conversation context
2. **Matches all conventions automatically**:
   - Uses the project's naming convention
   - Places in the correct folder
   - Uses TypeScript if that's the standard  
   - Defines Props interface if common
   - Matches export style (default vs named)
   - Uses the preferred import style
3. **Enforces design tokens** - NEVER hardcode values:
   - Colors: Use CSS variables or Tailwind classes from the project
   - Shadows: Use defined shadow tokens
   - Border radius: Use radius tokens
   - Spacing: Follow the spacing scale
4. **Optionally verifies** - Can run compliance check if requested

**User experience:** User says "Create a Button component" → Claude automatically creates it following ALL project patterns. No manual steps needed.

## Critical Rules

### Python Compatibility

**IMPORTANT:** Always detect which Python command is available before running scripts.

Check for Python availability:
```bash
# Check for python3 first (preferred)
if command -v python3 &> /dev/null; then
    PYTHON_CMD="python3"
elif command -v python &> /dev/null; then
    PYTHON_CMD="python"
else
    echo "Error: Python not found. Please install Python 3."
    exit 1
fi
```

Then use `$PYTHON_CMD` to run scripts:
```bash
$PYTHON_CMD scripts/analyze_project.py /path/to/project output.json
```

**Compatibility:**
- ✅ Works with `python3` command
- ✅ Works with `python` command  
- ✅ Automatically detects which is available
- ✅ Requires Python 3.6+

### Design Token Enforcement

**NEVER use hardcoded values**. Always reference the project's design tokens.

❌ **Bad - Hardcoded values**:
```tsx
<div style={{
  boxShadow: '0 4px 6px rgba(0,0,0,0.1)',
  borderRadius: '8px',
  backgroundColor: '#f3f4f6',
  padding: '16px'
}}>
```

✅ **Good - Using design tokens**:
```tsx
// With Tailwind
<div className="shadow-md rounded-lg bg-gray-100 p-4">

// Or with CSS variables
<div style={{
  boxShadow: 'var(--shadow-md)',
  borderRadius: 'var(--radius-lg)',
  backgroundColor: 'var(--color-gray-100)',
  padding: 'var(--spacing-4)'
}}>
```

### Pattern Analysis Before Creation

Always analyze the project BEFORE creating components if patterns are unknown. The analysis extracts:
- All design tokens currently in use
- Component structure patterns
- Naming and organization conventions

This ensures perfect consistency with the existing codebase.

### Compliance Checking

After creating a component, always run the compliance checker. It will:
- Score the component (0-100)
- List critical issues (must fix)
- Provide warnings (should fix)
- Offer suggestions for better consistency

## Available Scripts

All scripts are compatible with both `python` and `python3` commands. Claude will automatically detect which is available on your system.

### `analyze_project.py`
Scans a frontend project and extracts all patterns into a JSON file.

**Python 3 Required:** These scripts require Python 3.6+

**Manual Usage** (if needed):
```bash
# Try python3 first (recommended)
python3 scripts/analyze_project.py <project_path> [output.json]

# Or use python if that's what your system has
python scripts/analyze_project.py <project_path> [output.json]
```

**Claude Usage:** Claude automatically detects and uses the correct command.

**What it extracts**:
- Design tokens (colors, shadows, radii, spacing, fonts)
- Folder structure organization
- Component patterns (TS usage, Props, exports)
- Naming conventions
- Import patterns (aliases vs relative)

### `check_compliance.py`
Verifies a component follows extracted patterns.

**Manual Usage** (if needed):
```bash
# With python3
python3 scripts/check_compliance.py <patterns.json> <component_path>

# Or with python
python scripts/check_compliance.py <patterns.json> <component_path>
```

**Claude Usage:** Claude automatically detects and uses the correct command.

**Output**:
- Compliance score (0-100)
- Issues that must be fixed
- Warnings to address
- Suggestions for improvement

### `generate_report.py`
Converts JSON analysis to readable markdown.

**Manual Usage** (if needed):
```bash
# With python3
python3 scripts/generate_report.py <analysis.json> [output.md]

# Or with python
python scripts/generate_report.py <analysis.json> [output.md]
```

**Claude Usage:** Claude automatically detects and uses the correct command.

## Reference Documentation

For detailed guidance, see:
- **[workflow.md](references/workflow.md)** - Complete step-by-step component creation workflow
- **[design-tokens.md](references/design-tokens.md)** - Comprehensive guide to design tokens and their usage

Read these references when:
- Creating components for the first time in a project
- User asks for detailed examples or best practices
- Need clarification on design token usage
- Want to understand the full workflow

## Example Usage Scenarios

### Scenario 1: New Component in Existing Project

```
User: "Create a ProfileCard component for my React app"

1. Check if project has been analyzed
2. If not: Run analyze_project.py on their codebase
3. Review extracted patterns
4. Create component matching:
   - Naming convention (ProfileCard.tsx or profile-card.tsx)
   - Folder location (components/ or src/components/)
   - TypeScript usage (if project uses TS)
   - Props interface pattern
   - Design tokens for styling
5. Run compliance check
6. Fix any issues found
```

### Scenario 2: Refactoring Existing Component

```
User: "This Button component doesn't match our design system"

1. Run analyzer if not already done
2. Review extracted design tokens
3. Identify hardcoded values in Button
4. Replace with design tokens:
   - Hardcoded colors → CSS variables or Tailwind classes
   - Custom shadows → Shadow tokens
   - Random spacing → Spacing scale values
5. Run compliance check to verify
```

### Scenario 3: Pattern Analysis Only

```
User: "What design patterns does my project use?"

1. Run analyze_project.py
2. Generate readable report
3. Present findings:
   - Design token summary
   - Folder organization
   - Component conventions
   - Naming patterns
```

## Multi-Project Support

This skill is **generic** and works with ANY frontend project:
- React, Vue, Svelte, Angular, vanilla JS
- Tailwind, CSS Modules, styled-components, CSS-in-JS
- TypeScript or JavaScript
- Any folder structure

The analyzer adapts to whatever patterns it finds in the project.

## When to Re-analyze

Re-run the analyzer when:
- Major design system changes occur
- New design tokens are added
- Component patterns evolve
- Starting work after a long break from the project

## Pattern Enforcement Philosophy

This skill enforces **existing patterns**, not opinionated "best practices". It:
- Learns from the actual codebase
- Extracts patterns automatically
- Enforces consistency with what exists
- Adapts to any project structure or style

The goal: **Perfect consistency with the existing codebase**, regardless of the patterns it uses.
