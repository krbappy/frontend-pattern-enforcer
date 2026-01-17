# Changelog

All notable changes to the Frontend Pattern Enforcer skill will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2025-01-17

### Added
- Initial release of Frontend Pattern Enforcer skill
- Project analyzer (`analyze_project.py`) that extracts:
  - Design tokens (colors, shadows, border-radius, spacing, fonts, z-index)
  - Folder structure patterns
  - Component structure conventions
  - Naming conventions (PascalCase, kebab-case, snake_case)
  - Import patterns (path aliases vs relative imports)
- Compliance checker (`check_compliance.py`) that scores components 0-100
- Report generator (`generate_report.py`) for readable markdown output
- Comprehensive workflow documentation in `references/workflow.md`
- Design tokens guide in `references/design-tokens.md`
- Support for any frontend framework (React, Vue, Svelte, Angular, etc.)
- Support for any CSS approach (Tailwind, CSS Modules, styled-components, etc.)
- Generic, project-agnostic pattern extraction and enforcement

### Features
- Automatic design token extraction from CSS, SCSS, Tailwind config
- Component pattern recognition (TypeScript usage, Props interfaces, exports)
- Naming convention detection and enforcement
- Import style analysis and recommendations
- Compliance scoring with actionable feedback
- Detailed pattern reports with statistics

## [Unreleased]

### Planned
- Support for extracting patterns from Figma designs
- Integration with popular design systems (Material UI, Chakra UI, etc.)
- Auto-fix capability for common compliance issues
- CI/CD integration for automated pattern checking
- VS Code extension for real-time compliance feedback
- Pattern diff tool for comparing project versions
- Team collaboration features for shared pattern libraries

---

## Version Guide

- **Major version (X.0.0)**: Breaking changes that require user action
- **Minor version (0.X.0)**: New features, backward compatible
- **Patch version (0.0.X)**: Bug fixes, documentation updates
