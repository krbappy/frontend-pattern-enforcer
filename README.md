# Frontend Pattern Enforcer Skill

A generic skill that analyzes any frontend project to extract and enforce design patterns, ensuring perfect consistency with your existing codebase.

## What It Does

This skill:
- **Analyzes** your frontend project automatically
- **Extracts** design tokens (colors, shadows, spacing, border-radius, etc.)
- **Identifies** component patterns, naming conventions, and folder structure
- **Enforces** consistency when creating new components
- **Checks** compliance of new code against project patterns

## Works With Any Project

- ✅ React, Vue, Svelte, Angular, vanilla JS
- ✅ Tailwind, CSS Modules, Shadcn, Material UI, Chakra UI
- ✅ TypeScript or JavaScript
- ✅ Any folder structure or naming convention

The skill adapts to YOUR project's patterns, not the other way around!

## How to Use

### 1. Install the Skill

Upload the `frontend-pattern-enforcer.skill` file to Claude.ai:
- Go to Settings → Skills
- Click "Upload Skill"
- Select `frontend-pattern-enforcer.skill`

### 2. First Time: Analyze Your Project

When starting work on a frontend project:

**Tell Claude:** "Analyze my project patterns"

Claude will:
1. Run the analyzer on your project files
2. Extract all design tokens and patterns
3. Generate a readable report
4. Store the analysis for future use

### 3. Create Components

When creating new components:

**Tell Claude:** "Create a ProfileCard component following our project patterns"

Claude will:
1. Check the previously extracted patterns
2. Match naming conventions
3. Use correct folder structure
4. Apply design tokens (no hardcoded values!)
5. Follow component structure patterns
6. Run compliance check
7. Fix any issues found

### 4. Check Existing Components

For refactoring or verification:

**Tell Claude:** "Does this Button component follow our patterns?"

Claude will:
1. Analyze the component
2. Compare against project patterns
3. Report any inconsistencies
4. Suggest fixes

## Example Conversations

### Pattern Analysis
```
You: "Analyze the design patterns in my React project"
Claude: [Runs analyzer, generates report showing all colors, shadows, spacing, component patterns, etc.]
```

### Creating Components
```
You: "Create a UserCard component"
Claude: [Creates component matching project's naming, structure, and design tokens]
```

### Refactoring
```
You: "This modal uses hardcoded colors. Fix it to match our design system"
Claude: [Replaces hardcoded values with design tokens from project]
```

### Compliance Check
```
You: "Check if this component follows our patterns"
Claude: [Runs compliance checker, provides score and recommendations]
```

## Key Features

### 1. Design Token Extraction
Automatically finds:
- Colors (hex, rgb, hsl, CSS variables)
- Box shadows
- Border radius values
- Spacing scales
- Typography tokens
- Z-index layers

### 2. Pattern Recognition
Identifies:
- Folder organization (components/, pages/, utils/, etc.)
- Naming conventions (PascalCase, kebab-case, snake_case)
- Component structure (TypeScript, Props interfaces, exports)
- Import patterns (path aliases vs relative)

### 3. Compliance Checking
Scores components on:
- Naming convention compliance
- Design token usage (no hardcoded values)
- Component structure consistency
- Import style matching

### 4. Project Agnostic
Works with:
- Any JavaScript framework
- Any CSS approach
- Any project structure
- Any design system

## What Gets Analyzed

The skill scans your project and extracts:

### Design Tokens
```css
/* Colors */
--color-primary: #3b82f6
--color-gray-100: #f3f4f6

/* Shadows */
--shadow-md: 0 4px 6px -1px rgb(0 0 0 / 0.1)

/* Radius */
--radius-lg: 0.5rem

/* Spacing */
--spacing-4: 1rem
```

### Component Patterns
- TypeScript usage percentage
- Props interface patterns
- Default vs named exports
- Hook usage patterns

### File Organization
- Component folder locations
- Utility folder structure
- Asset organization
- Configuration patterns

### Naming Conventions
- File naming (PascalCase vs kebab-case)
- Component naming
- Variable naming patterns

## Benefits

✅ **Perfect Consistency** - New code automatically matches existing patterns
✅ **No Hardcoded Values** - Enforces design token usage
✅ **Framework Agnostic** - Works with any frontend stack
✅ **Automated Checks** - Compliance scoring before you commit
✅ **Pattern Learning** - Adapts to your specific codebase

## Advanced Usage

### Re-analyze After Changes
When your design system evolves:
```
"Re-analyze the project patterns to pick up the new design tokens"
```

### Batch Refactoring
For multiple components:
```
"Refactor all components in /components/cards to use design tokens"
```

### Pattern Comparison
Between projects:
```
"Compare the patterns between my main app and dashboard project"
```

## Technical Details

### Scripts Included

1. **analyze_project.py** - Scans codebase and extracts patterns
2. **check_compliance.py** - Verifies component compliance
3. **generate_report.py** - Creates readable pattern reports

### Reference Docs Included

1. **workflow.md** - Complete step-by-step guide
2. **design-tokens.md** - Comprehensive token usage guide

## FAQ

**Q: Will this work with my design system?**
A: Yes! It works with Shadcn, Material UI, Chakra, Tailwind, or any custom design system.

**Q: What if I don't have design tokens?**
A: The skill will extract whatever patterns exist - even if they're just hardcoded values, it will identify them as patterns.

**Q: Can I use this across multiple projects?**
A: Absolutely! Each project analysis is separate. The skill adapts to each project's unique patterns.

**Q: Does it work with Vue/Svelte/Angular?**
A: Yes! The skill is framework-agnostic and works with any frontend codebase.

**Q: What if my project has no consistent patterns?**
A: The skill will identify what patterns DO exist and can help you establish consistency going forward.

## Support

If you encounter issues or have questions:
1. Check the generated `project_patterns.md` report
2. Review the compliance checker output
3. Refer to the reference documentation in the skill

## Version

Version: 1.0.0
Created: January 2026

---

Enjoy perfect pattern consistency in your frontend projects! 🎨✨
