#!/usr/bin/env python3
"""
Check if a new component follows the project's established patterns.
"""

import json
import re
from pathlib import Path
from typing import Dict, List, Tuple

class ComplianceChecker:
    def __init__(self, patterns_file: str):
        """Initialize with previously analyzed patterns."""
        with open(patterns_file, 'r') as f:
            self.patterns = json.load(f)
    
    def check_component(self, component_path: str) -> Dict:
        """Check if component follows established patterns."""
        print(f"\n🔍 Checking component: {component_path}")
        
        issues = []
        warnings = []
        suggestions = []
        
        component_file = Path(component_path)
        if not component_file.exists():
            return {"error": "File not found"}
        
        content = component_file.read_text(encoding='utf-8')
        filename = component_file.stem
        
        # Check naming convention
        naming_issues = self._check_naming(filename)
        issues.extend(naming_issues)
        
        # Check design tokens usage
        token_issues = self._check_design_tokens(content)
        warnings.extend(token_issues)
        
        # Check component structure
        structure_issues = self._check_component_structure(content, component_file.suffix)
        suggestions.extend(structure_issues)
        
        # Check imports
        import_issues = self._check_imports(content)
        suggestions.extend(import_issues)
        
        # Generate report
        report = {
            "file": component_path,
            "compliant": len(issues) == 0,
            "issues": issues,
            "warnings": warnings,
            "suggestions": suggestions,
            "score": self._calculate_score(issues, warnings, suggestions)
        }
        
        self._print_report(report)
        return report
    
    def _check_naming(self, filename: str) -> List[str]:
        """Check if filename follows project naming convention."""
        issues = []
        
        most_common = self.patterns["naming_conventions"].get("most_common_file")
        if not most_common:
            return issues
        
        # Check if filename follows the pattern
        is_kebab = '-' in filename
        is_snake = '_' in filename
        is_pascal = filename[0].isupper() if filename else False
        
        if most_common == "kebab-case" and not is_kebab:
            issues.append(f"File should use kebab-case naming (project standard)")
        elif most_common == "PascalCase" and not is_pascal:
            issues.append(f"File should use PascalCase naming (project standard)")
        elif most_common == "snake_case" and not is_snake:
            issues.append(f"File should use snake_case naming (project standard)")
        
        return issues
    
    def _check_design_tokens(self, content: str) -> List[str]:
        """Check if hardcoded values are used instead of design tokens."""
        warnings = []
        
        # Check for hardcoded colors
        hardcoded_colors = re.findall(r'(?:color|background|bg|border):\s*(#[0-9a-fA-F]{3,8}|rgba?\([^)]+\))', content)
        if hardcoded_colors:
            project_colors = self.patterns["design_tokens"].get("colors", [])
            for color in hardcoded_colors:
                if color not in [c.split(':')[-1].strip() if ':' in c else c for c in project_colors]:
                    warnings.append(f"Hardcoded color '{color}' - consider using design token")
        
        # Check for hardcoded shadows
        hardcoded_shadows = re.findall(r'box-shadow:\s*([^;]+);', content)
        if hardcoded_shadows:
            warnings.append("Custom box-shadow detected - consider using design token")
        
        # Check for hardcoded border radius
        hardcoded_radius = re.findall(r'border-radius:\s*(\d+px)', content)
        if hardcoded_radius:
            project_radii = self.patterns["design_tokens"].get("border_radius", [])
            for radius in hardcoded_radius:
                if radius not in [r.split(':')[-1].strip() if ':' in r else r for r in project_radii]:
                    warnings.append(f"Custom border-radius '{radius}' - consider using design token")
        
        return warnings
    
    def _check_component_structure(self, content: str, file_extension: str) -> List[str]:
        """Check component structure against common patterns."""
        suggestions = []
        
        if not self.patterns["component_patterns"]:
            return suggestions
        
        # Analyze what's common in existing components
        common_patterns = self.patterns["component_patterns"]
        
        # Check TypeScript usage
        ts_usage = sum(1 for p in common_patterns if p.get("has_typescript")) / len(common_patterns)
        if ts_usage > 0.7 and file_extension not in ['.tsx', '.ts']:
            suggestions.append("Most components use TypeScript - consider using .tsx/.ts")
        
        # Check Props interface
        props_usage = sum(1 for p in common_patterns if p.get("has_props_interface")) / len(common_patterns)
        if props_usage > 0.7 and not ('interface Props' in content or 'type Props' in content):
            suggestions.append("Most components define Props interface/type - consider adding one")
        
        # Check export pattern
        default_export = sum(1 for p in common_patterns if p.get("exports_default")) / len(common_patterns)
        if default_export > 0.7 and 'export default' not in content:
            suggestions.append("Most components use default export")
        
        return suggestions
    
    def _check_imports(self, content: str) -> List[str]:
        """Check if imports follow project patterns."""
        suggestions = []
        
        import_patterns = self.patterns.get("import_patterns", {})
        
        # Find imports in this file
        import_lines = re.findall(r'import\s+.*?from\s+[\'"]([^\'"]+)[\'"]', content)
        
        alias_count = sum(1 for imp in import_lines if imp.startswith('@/'))
        relative_count = sum(1 for imp in import_lines if imp.startswith('.'))
        
        # Check project preference
        project_alias = len(import_patterns.get("alias", []))
        project_relative = len(import_patterns.get("relative", []))
        
        if project_alias > project_relative and relative_count > alias_count:
            suggestions.append("Project prefers path aliases (@/) over relative imports")
        elif project_relative > project_alias and alias_count > relative_count:
            suggestions.append("Project prefers relative imports over path aliases")
        
        return suggestions
    
    def _calculate_score(self, issues: List, warnings: List, suggestions: List) -> int:
        """Calculate compliance score (0-100)."""
        score = 100
        score -= len(issues) * 20  # Critical issues
        score -= len(warnings) * 10  # Warnings
        score -= len(suggestions) * 5  # Suggestions
        return max(0, score)
    
    def _print_report(self, report: Dict):
        """Print compliance report."""
        print(f"\n{'='*60}")
        print(f"Compliance Score: {report['score']}/100")
        print(f"{'='*60}")
        
        if report['issues']:
            print("\n❌ ISSUES (Must Fix):")
            for issue in report['issues']:
                print(f"  • {issue}")
        
        if report['warnings']:
            print("\n⚠️  WARNINGS:")
            for warning in report['warnings']:
                print(f"  • {warning}")
        
        if report['suggestions']:
            print("\n💡 SUGGESTIONS:")
            for suggestion in report['suggestions']:
                print(f"  • {suggestion}")
        
        if not report['issues'] and not report['warnings'] and not report['suggestions']:
            print("\n✅ Component follows all project patterns!")
        
        print(f"\n{'='*60}\n")


def main():
    import sys
    
    if len(sys.argv) < 3:
        print("Usage: python check_compliance.py <patterns_file> <component_path>")
        sys.exit(1)
    
    patterns_file = sys.argv[1]
    component_path = sys.argv[2]
    
    checker = ComplianceChecker(patterns_file)
    checker.check_component(component_path)


if __name__ == "__main__":
    main()
