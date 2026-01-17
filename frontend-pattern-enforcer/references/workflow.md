# Component Creation Workflow

This guide outlines the standard workflow for creating new components that match existing project patterns.

## Step 1: Analyze the Project (First Time Only)

Before creating any components, analyze the project to extract patterns:

```bash
python scripts/analyze_project.py /path/to/project project_patterns.json
python scripts/generate_report.py project_patterns.json
```

This creates:
- `project_patterns.json` - Machine-readable pattern data
- `project_patterns.md` - Human-readable report

## Step 2: Review Extracted Patterns

Open `project_patterns.md` and review:

1. **Design Tokens**: Note the colors, shadows, border-radius values used
2. **Folder Structure**: Understand where components should live
3. **Naming Conventions**: Follow the established naming pattern
4. **Component Patterns**: Match TypeScript usage, Props definition, export style
5. **Import Patterns**: Use the preferred import style (alias vs relative)

## Step 3: Create Component Following Patterns

When creating a new component:

### File Naming
- Use the project's naming convention (PascalCase, kebab-case, etc.)
- Place in the appropriate folder (e.g., `/components`, `/src/components`)

### Component Structure
Match the common patterns:
- Use TypeScript if 70%+ of components use it
- Define Props interface if common
- Use default export if that's the standard
- Include PropTypes or TypeScript types

### Design Tokens
**CRITICAL**: Never hardcode values. Always use existing design tokens:

❌ **Bad:**
```tsx
<div style={{ 
  boxShadow: '0 4px 6px rgba(0,0,0,0.1)',
  borderRadius: '8px',
  backgroundColor: '#f3f4f6'
}}>
```

✅ **Good:**
```tsx
<div className="shadow-md rounded-lg bg-gray-100">
  // Uses project's design tokens
</div>
```

Or with CSS variables:
```tsx
<div style={{
  boxShadow: 'var(--shadow-md)',
  borderRadius: 'var(--radius-lg)',
  backgroundColor: 'var(--color-gray-100)'
}}>
```

### Import Style
Use the project's preferred import pattern:
- If project uses `@/` aliases: `import { Button } from '@/components/ui/button'`
- If project uses relative: `import { Button } from '../ui/button'`

## Step 4: Verify Compliance

After creating the component, check compliance:

```bash
python scripts/check_compliance.py project_patterns.json /path/to/new/Component.tsx
```

This will:
- Score your component (0-100)
- List critical issues (must fix)
- List warnings (should fix)
- Provide suggestions

## Step 5: Fix Issues

Address any issues found:
- **Issues (❌)**: Must fix before shipping
- **Warnings (⚠️)**: Strongly recommended to fix
- **Suggestions (💡)**: Consider for better consistency

## Common Patterns by Framework

### React + Shadcn/ui
```tsx
// ComponentName.tsx
import { cn } from "@/lib/utils"
import { Button } from "@/components/ui/button"

interface ComponentNameProps {
  className?: string
  variant?: "default" | "outline"
}

export default function ComponentName({ 
  className,
  variant = "default" 
}: ComponentNameProps) {
  return (
    <div className={cn("flex items-center gap-4", className)}>
      <Button variant={variant}>Click me</Button>
    </div>
  )
}
```

### React + Tailwind
```tsx
// component-name.tsx
interface ComponentNameProps {
  variant?: 'primary' | 'secondary'
}

export const ComponentName = ({ variant = 'primary' }: ComponentNameProps) => {
  return (
    <div className="rounded-lg shadow-sm p-4">
      {/* Content */}
    </div>
  )
}
```

### Vue 3 + Composition API
```vue
<script setup lang="ts">
interface Props {
  variant?: 'default' | 'outline'
}

const props = withDefaults(defineProps<Props>(), {
  variant: 'default'
})
</script>

<template>
  <div class="component-wrapper">
    <!-- Content -->
  </div>
</template>

<style scoped>
.component-wrapper {
  /* Use design tokens */
  border-radius: var(--radius-lg);
  box-shadow: var(--shadow-md);
}
</style>
```

## Design Token Best Practices

### Colors
Always reference from the project's color system:
- Check `project_patterns.md` for available colors
- Use CSS variables: `var(--color-primary)`
- Or Tailwind classes: `bg-primary text-white`

### Spacing
Use the project's spacing scale:
- Tailwind: `p-4 gap-2 m-8`
- CSS variables: `padding: var(--spacing-4)`

### Shadows
Use predefined shadow tokens:
- Tailwind: `shadow-sm shadow-md shadow-lg`
- CSS variables: `box-shadow: var(--shadow-md)`

### Border Radius
Use consistent radius values:
- Tailwind: `rounded-sm rounded-md rounded-lg`
- CSS variables: `border-radius: var(--radius-md)`

## Tips for Consistency

1. **Before writing any code**, review the pattern analysis
2. **Copy a similar component** as a starting point
3. **Use the project's design system** components when available
4. **Run compliance check** before committing
5. **Keep the analysis updated** - re-run when patterns change

## Updating Pattern Analysis

Re-analyze when:
- Major design system changes
- New components establish different patterns
- After adding new design tokens

```bash
python scripts/analyze_project.py /path/to/project project_patterns.json
python scripts/generate_report.py project_patterns.json
```
