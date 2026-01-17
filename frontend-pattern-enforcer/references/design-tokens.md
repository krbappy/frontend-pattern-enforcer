# Design Tokens Reference

Design tokens are the design decisions (colors, spacing, typography, etc.) expressed as data. This guide explains how to extract, use, and maintain design tokens in your project.

## What Are Design Tokens?

Design tokens are named entities that store visual design attributes like:
- Colors
- Typography (font families, sizes, weights)
- Spacing (margins, paddings, gaps)
- Shadows
- Border radius
- Z-index layers
- Transitions/animations

## Token Formats

### CSS Variables (Most Common)
```css
:root {
  /* Colors */
  --color-primary: #3b82f6;
  --color-secondary: #8b5cf6;
  --color-gray-100: #f3f4f6;
  
  /* Shadows */
  --shadow-sm: 0 1px 2px 0 rgb(0 0 0 / 0.05);
  --shadow-md: 0 4px 6px -1px rgb(0 0 0 / 0.1);
  
  /* Border Radius */
  --radius-sm: 0.125rem;
  --radius-md: 0.375rem;
  --radius-lg: 0.5rem;
  
  /* Spacing */
  --spacing-1: 0.25rem;
  --spacing-2: 0.5rem;
  --spacing-4: 1rem;
}
```

### Tailwind Config
```js
// tailwind.config.js
module.exports = {
  theme: {
    extend: {
      colors: {
        primary: '#3b82f6',
        secondary: '#8b5cf6',
      },
      boxShadow: {
        'custom': '0 4px 6px -1px rgb(0 0 0 / 0.1)',
      },
      borderRadius: {
        'custom': '0.5rem',
      }
    }
  }
}
```

### JavaScript/TypeScript Tokens
```ts
// tokens.ts
export const tokens = {
  colors: {
    primary: '#3b82f6',
    secondary: '#8b5cf6',
  },
  shadows: {
    sm: '0 1px 2px 0 rgb(0 0 0 / 0.05)',
    md: '0 4px 6px -1px rgb(0 0 0 / 0.1)',
  },
  radius: {
    sm: '0.125rem',
    md: '0.375rem',
    lg: '0.5rem',
  }
} as const;
```

## Using Design Tokens

### In React Components with Tailwind
```tsx
// ✅ Good - Uses Tailwind classes (which reference tokens)
function Card() {
  return (
    <div className="rounded-lg shadow-md bg-gray-100 p-4">
      <h2 className="text-primary">Title</h2>
    </div>
  )
}

// ❌ Bad - Hardcoded values
function Card() {
  return (
    <div style={{
      borderRadius: '8px',
      boxShadow: '0 4px 6px rgba(0,0,0,0.1)',
      backgroundColor: '#f3f4f6',
      padding: '16px'
    }}>
      <h2 style={{ color: '#3b82f6' }}>Title</h2>
    </div>
  )
}
```

### In React with CSS Variables
```tsx
// ✅ Good - References CSS variables
function Card() {
  return (
    <div style={{
      borderRadius: 'var(--radius-lg)',
      boxShadow: 'var(--shadow-md)',
      backgroundColor: 'var(--color-gray-100)',
      padding: 'var(--spacing-4)'
    }}>
      <h2 style={{ color: 'var(--color-primary)' }}>Title</h2>
    </div>
  )
}

// ❌ Bad - Hardcoded values
function Card() {
  return (
    <div style={{
      borderRadius: '8px',
      boxShadow: '0 4px 6px rgba(0,0,0,0.1)',
      backgroundColor: '#f3f4f6',
      padding: '16px'
    }}>
      <h2 style={{ color: '#3b82f6' }}>Title</h2>
    </div>
  )
}
```

### In Vue Components
```vue
<template>
  <div class="card">
    <h2>Title</h2>
  </div>
</template>

<style scoped>
/* ✅ Good - Uses CSS variables */
.card {
  border-radius: var(--radius-lg);
  box-shadow: var(--shadow-md);
  background-color: var(--color-gray-100);
  padding: var(--spacing-4);
}

/* ❌ Bad - Hardcoded values */
.card {
  border-radius: 8px;
  box-shadow: 0 4px 6px rgba(0,0,0,0.1);
  background-color: #f3f4f6;
  padding: 16px;
}
</style>
```

## Common Token Categories

### 1. Colors

**Semantic Colors** (Preferred):
```css
--color-primary: #3b82f6;
--color-secondary: #8b5cf6;
--color-success: #10b981;
--color-warning: #f59e0b;
--color-error: #ef4444;
--color-text: #111827;
--color-text-muted: #6b7280;
--color-background: #ffffff;
--color-surface: #f9fafb;
```

**Gray Scale**:
```css
--color-gray-50: #f9fafb;
--color-gray-100: #f3f4f6;
--color-gray-200: #e5e7eb;
--color-gray-300: #d1d5db;
/* ... up to gray-900 */
```

### 2. Spacing

Use a consistent scale (often 4px or 8px based):
```css
--spacing-0: 0;
--spacing-1: 0.25rem;  /* 4px */
--spacing-2: 0.5rem;   /* 8px */
--spacing-3: 0.75rem;  /* 12px */
--spacing-4: 1rem;     /* 16px */
--spacing-5: 1.25rem;  /* 20px */
--spacing-6: 1.5rem;   /* 24px */
--spacing-8: 2rem;     /* 32px */
--spacing-10: 2.5rem;  /* 40px */
--spacing-12: 3rem;    /* 48px */
```

### 3. Typography

```css
/* Font Families */
--font-sans: ui-sans-serif, system-ui, sans-serif;
--font-serif: ui-serif, Georgia, serif;
--font-mono: ui-monospace, monospace;

/* Font Sizes */
--text-xs: 0.75rem;    /* 12px */
--text-sm: 0.875rem;   /* 14px */
--text-base: 1rem;     /* 16px */
--text-lg: 1.125rem;   /* 18px */
--text-xl: 1.25rem;    /* 20px */
--text-2xl: 1.5rem;    /* 24px */
--text-3xl: 1.875rem;  /* 30px */

/* Font Weights */
--font-normal: 400;
--font-medium: 500;
--font-semibold: 600;
--font-bold: 700;
```

### 4. Shadows

```css
--shadow-none: none;
--shadow-sm: 0 1px 2px 0 rgb(0 0 0 / 0.05);
--shadow-md: 0 4px 6px -1px rgb(0 0 0 / 0.1);
--shadow-lg: 0 10px 15px -3px rgb(0 0 0 / 0.1);
--shadow-xl: 0 20px 25px -5px rgb(0 0 0 / 0.1);
--shadow-2xl: 0 25px 50px -12px rgb(0 0 0 / 0.25);
--shadow-inner: inset 0 2px 4px 0 rgb(0 0 0 / 0.05);
```

### 5. Border Radius

```css
--radius-none: 0;
--radius-sm: 0.125rem;   /* 2px */
--radius-md: 0.375rem;   /* 6px */
--radius-lg: 0.5rem;     /* 8px */
--radius-xl: 0.75rem;    /* 12px */
--radius-2xl: 1rem;      /* 16px */
--radius-full: 9999px;   /* Fully rounded */
```

### 6. Z-Index Layers

```css
--z-dropdown: 1000;
--z-sticky: 1020;
--z-fixed: 1030;
--z-modal-backdrop: 1040;
--z-modal: 1050;
--z-popover: 1060;
--z-tooltip: 1070;
```

## Token Extraction from Project

The `analyze_project.py` script automatically extracts tokens by:

1. Scanning CSS/SCSS files for CSS variables
2. Reading Tailwind config files
3. Finding hardcoded values in components
4. Identifying color patterns
5. Extracting shadow definitions
6. Finding border-radius values

## When to Create New Tokens

**Do create new tokens when**:
- The value will be reused across components
- It represents a design decision (not an arbitrary value)
- It fits into the existing token system

**Don't create tokens for**:
- One-off values specific to a single use case
- Values that don't represent a design pattern

## Maintaining Token Consistency

### 1. Regular Audits
Run the analyzer periodically:
```bash
python scripts/analyze_project.py /path/to/project
```

### 2. Code Review Checklist
- [ ] No hardcoded colors (except for gradients requiring specific values)
- [ ] Spacing uses token scale
- [ ] Shadows reference token values
- [ ] Border radius from token set
- [ ] Typography uses font tokens

### 3. Documentation
Keep a `design-tokens.md` in your project documenting:
- Available tokens
- When to use each token
- How to add new tokens

## Common Mistakes to Avoid

### ❌ Mixing Systems
```tsx
// Bad - mixing Tailwind classes with inline hardcoded values
<div className="p-4" style={{ margin: '15px' }}>
```

### ❌ Inconsistent Spacing
```tsx
// Bad - not following spacing scale
<div className="p-3" style={{ gap: '13px' }}>
```

### ❌ Random Color Values
```tsx
// Bad - arbitrary color not in the system
<div style={{ backgroundColor: '#e8f4f8' }}>
```

### ✅ Correct Usage
```tsx
// Good - consistent token usage
<div className="p-4 gap-4 bg-blue-50">
```

## Framework-Specific Best Practices

### Shadcn/ui Projects
Shadcn uses CSS variables defined in `globals.css`:
```css
@layer base {
  :root {
    --background: 0 0% 100%;
    --foreground: 222.2 84% 4.9%;
    --primary: 221.2 83.2% 53.3%;
    /* ... */
  }
}
```

Use the `cn()` utility for combining classes:
```tsx
import { cn } from "@/lib/utils"

<div className={cn("rounded-md p-4", className)}>
```

### Material UI Projects
Use theme tokens:
```tsx
import { useTheme } from '@mui/material/styles';

const theme = useTheme();
<Box sx={{ 
  borderRadius: theme.shape.borderRadius,
  boxShadow: theme.shadows[2]
}}>
```

### Chakra UI Projects
Use theme tokens via props:
```tsx
<Box 
  borderRadius="md" 
  boxShadow="md" 
  bg="gray.100" 
  p={4}
>
```
