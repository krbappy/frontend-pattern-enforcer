---
name: frontend-pattern-enforcer
description: Analyzes existing frontend projects to extract and enforce design patterns, design tokens (colors, shadows, spacing, border-radius), component structure conventions, naming patterns, and folder organization. Use when working on frontend projects (React, Vue, any framework) where consistency with existing codebase patterns is critical. Analyzes projects before creating components to ensure new code matches established patterns. Use for component creation, refactoring existing components, or when user requests pattern analysis or consistency checks.
---

# Frontend Pattern Enforcer

This skill ensures new frontend components strictly follow existing project patterns by analyzing the codebase and enforcing consistency in design tokens, component structure, naming conventions, and folder organization.

## Core Workflow

### First-Time Setup: Analyze the Project

Before creating any components in a project, analyze it to extract patterns:

1. **Run the analyzer**:
```bash
python scripts/analyze_project.py /path/to/project project_patterns.json
```

2. **Generate readable report**:
```bash
python scripts/generate_report.py project_patterns.json project_patterns.md
```

3. **Review the report** (`project_patterns.md`) to understand:
   - Design tokens (colors, shadows, radii, spacing)
   - Folder structure conventions
   - Component patterns (TypeScript usage, Props interfaces, exports)
   - Naming conventions (PascalCase, kebab-case, etc.)
   - Import patterns (path aliases vs relative imports)

### Creating Components: Follow Extracted Patterns

When creating a new component:

1. **Reference the analysis** - Check `project_patterns.md` before writing code

2. **Match the patterns**:
   - Use the project's naming convention
   - Place in the correct folder
   - Use TypeScript if that's the standard
   - Define Props interface if common
   - Match export style (default vs named)
   - Use the preferred import style

3. **Use design tokens** - NEVER hardcode values:
   - Colors: Use CSS variables or Tailwind classes from the project
   - Shadows: Use defined shadow tokens
   - Border radius: Use radius tokens
   - Spacing: Follow the spacing scale

4. **Verify compliance**:
```bash
python scripts/check_compliance.py project_patterns.json /path/to/Component.tsx
```

5. **Fix any issues** reported by the compliance checker

## Critical Rules

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

### `analyze_project.py`
Scans a frontend project and extracts all patterns into a JSON file.

**Usage**:
```bash
python scripts/analyze_project.py <project_path> [output.json]
```

**What it extracts**:
- Design tokens (colors, shadows, radii, spacing, fonts)
- Folder structure organization
- Component patterns (TS usage, Props, exports)
- Naming conventions
- Import patterns (aliases vs relative)

### `check_compliance.py`
Verifies a component follows extracted patterns.

**Usage**:
```bash
python scripts/check_compliance.py <patterns.json> <component_path>
```

**Output**:
- Compliance score (0-100)
- Issues that must be fixed
- Warnings to address
- Suggestions for improvement

### `generate_report.py`
Converts JSON analysis to readable markdown.

**Usage**:
```bash
python scripts/generate_report.py <analysis.json> [output.md]
```

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
