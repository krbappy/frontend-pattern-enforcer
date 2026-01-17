#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Analyze a frontend project to extract design patterns, design tokens, and conventions.
Works with React, Vue, or any frontend project structure.

Compatible with both 'python' and 'python3' commands.
Requires Python 3.6 or higher.
"""

import sys
import os

# Ensure we're using Python 3
if sys.version_info[0] < 3:
    print("Error: This script requires Python 3.6 or higher")
    print(f"Current version: Python {sys.version_info[0]}.{sys.version_info[1]}")
    print("\nPlease run with: python3 scripts/analyze_project.py")
    sys.exit(1)

if sys.version_info[0] == 3 and sys.version_info[1] < 6:
    print("Error: This script requires Python 3.6 or higher")
    print(f"Current version: Python {sys.version_info[0]}.{sys.version_info[1]}")
    sys.exit(1)

import os
import re
import json
from pathlib import Path
from collections import defaultdict
from typing import Dict, List, Set, Tuple

class FrontendAnalyzer:
    def __init__(self, project_path: str):
        self.project_path = Path(project_path)
        self.patterns = {
            "design_tokens": {
                "colors": set(),
                "shadows": set(),
                "border_radius": set(),
                "spacing": set(),
                "font_families": set(),
                "font_sizes": set(),
                "z_index": set(),
            },
            "folder_structure": {},
            "component_patterns": [],
            "naming_conventions": {
                "files": [],
                "components": [],
                "variables": []
            },
            "import_patterns": [],
            "css_patterns": []
        }
    
    def analyze(self) -> Dict:
        """Run full analysis on the project."""
        print(f"🔍 Analyzing project at: {self.project_path}")
        
        self._analyze_folder_structure()
        self._extract_design_tokens()
        self._analyze_component_patterns()
        self._analyze_naming_conventions()
        self._analyze_import_patterns()
        
        return self._generate_report()
    
    def _analyze_folder_structure(self):
        """Analyze folder organization patterns."""
        print("📁 Analyzing folder structure...")
        
        common_patterns = {
            "components": [],
            "pages": [],
            "utils": [],
            "hooks": [],
            "styles": [],
            "lib": [],
            "services": [],
            "contexts": [],
            "types": []
        }
        
        for root, dirs, files in os.walk(self.project_path):
            rel_path = os.path.relpath(root, self.project_path)
            
            # Skip node_modules, .git, dist, build
            if any(skip in rel_path for skip in ['node_modules', '.git', 'dist', 'build', '.next']):
                continue
            
            for pattern_name in common_patterns.keys():
                if pattern_name in rel_path.lower():
                    common_patterns[pattern_name].append(rel_path)
        
        self.patterns["folder_structure"] = {
            k: v for k, v in common_patterns.items() if v
        }
    
    def _extract_design_tokens(self):
        """Extract design tokens from CSS, Tailwind config, or style files."""
        print("🎨 Extracting design tokens...")
        
        # Patterns to search for
        css_var_pattern = r'--[\w-]+:\s*([^;]+);'
        color_pattern = r'(?:color|background|bg|border-color|fill|stroke):\s*(#[0-9a-fA-F]{3,8}|rgba?\([^)]+\)|hsl\([^)]+\))'
        shadow_pattern = r'(?:box-shadow|shadow):\s*([^;]+);'
        radius_pattern = r'(?:border-radius|rounded):\s*([^;]+);'
        spacing_pattern = r'(?:padding|margin|gap):\s*([^;]+);'
        
        # Search in various file types
        extensions = ['.css', '.scss', '.ts', '.tsx', '.js', '.jsx', '.config.js', '.config.ts']
        
        for ext in extensions:
            for file_path in self.project_path.rglob(f'*{ext}'):
                if 'node_modules' in str(file_path):
                    continue
                
                try:
                    content = file_path.read_text(encoding='utf-8')
                    
                    # Extract CSS variables
                    for match in re.finditer(css_var_pattern, content):
                        value = match.group(1).strip()
                        self._categorize_css_var(match.group(0), value)
                    
                    # Extract colors
                    for match in re.finditer(color_pattern, content):
                        self.patterns["design_tokens"]["colors"].add(match.group(1))
                    
                    # Extract shadows
                    for match in re.finditer(shadow_pattern, content):
                        self.patterns["design_tokens"]["shadows"].add(match.group(1))
                    
                    # Extract border radius
                    for match in re.finditer(radius_pattern, content):
                        self.patterns["design_tokens"]["border_radius"].add(match.group(1))
                    
                    # Extract spacing
                    for match in re.finditer(spacing_pattern, content):
                        self.patterns["design_tokens"]["spacing"].add(match.group(1))
                    
                except Exception as e:
                    continue
    
    def _categorize_css_var(self, var_name: str, value: str):
        """Categorize CSS variable by type."""
        var_lower = var_name.lower()
        
        if any(keyword in var_lower for keyword in ['color', 'bg', 'background', 'border', 'text']):
            self.patterns["design_tokens"]["colors"].add(f"{var_name}: {value}")
        elif 'shadow' in var_lower:
            self.patterns["design_tokens"]["shadows"].add(f"{var_name}: {value}")
        elif 'radius' in var_lower:
            self.patterns["design_tokens"]["border_radius"].add(f"{var_name}: {value}")
        elif any(keyword in var_lower for keyword in ['spacing', 'gap', 'padding', 'margin']):
            self.patterns["design_tokens"]["spacing"].add(f"{var_name}: {value}")
        elif 'font-family' in var_lower:
            self.patterns["design_tokens"]["font_families"].add(f"{var_name}: {value}")
        elif 'font-size' in var_lower:
            self.patterns["design_tokens"]["font_sizes"].add(f"{var_name}: {value}")
        elif 'z-index' in var_lower:
            self.patterns["design_tokens"]["z_index"].add(f"{var_name}: {value}")
    
    def _analyze_component_patterns(self):
        """Analyze component structure patterns."""
        print("🧩 Analyzing component patterns...")
        
        component_files = []
        for ext in ['.tsx', '.jsx', '.vue']:
            component_files.extend(self.project_path.rglob(f'*{ext}'))
        
        for file_path in component_files[:10]:  # Sample first 10 components
            if 'node_modules' in str(file_path):
                continue
            
            try:
                content = file_path.read_text(encoding='utf-8')
                
                # Detect patterns
                pattern = {
                    "file": str(file_path.relative_to(self.project_path)),
                    "has_typescript": file_path.suffix in ['.tsx', '.ts'],
                    "has_props_interface": 'interface Props' in content or 'type Props' in content,
                    "uses_hooks": any(hook in content for hook in ['useState', 'useEffect', 'useCallback', 'useMemo']),
                    "uses_children": 'children' in content,
                    "exports_default": 'export default' in content,
                    "exports_named": 'export {' in content or 'export const' in content,
                }
                
                self.patterns["component_patterns"].append(pattern)
            except Exception:
                continue
    
    def _analyze_naming_conventions(self):
        """Analyze naming conventions for files, components, variables."""
        print("📝 Analyzing naming conventions...")
        
        for file_path in self.project_path.rglob('*'):
            if file_path.is_file() and not any(skip in str(file_path) for skip in ['node_modules', '.git']):
                filename = file_path.stem
                
                # File naming patterns
                if '-' in filename:
                    self.patterns["naming_conventions"]["files"].append("kebab-case")
                elif '_' in filename:
                    self.patterns["naming_conventions"]["files"].append("snake_case")
                elif filename[0].isupper():
                    self.patterns["naming_conventions"]["files"].append("PascalCase")
                elif filename[0].islower() and filename[1:].islower():
                    self.patterns["naming_conventions"]["files"].append("lowercase")
    
    def _analyze_import_patterns(self):
        """Analyze import statement patterns."""
        print("📦 Analyzing import patterns...")
        
        import_patterns = {
            "absolute": [],
            "relative": [],
            "alias": []
        }
        
        for ext in ['.ts', '.tsx', '.js', '.jsx']:
            for file_path in list(self.project_path.rglob(f'*{ext}'))[:20]:
                if 'node_modules' in str(file_path):
                    continue
                
                try:
                    content = file_path.read_text(encoding='utf-8')
                    
                    # Find import statements
                    import_lines = re.findall(r'import\s+.*?from\s+[\'"]([^\'"]+)[\'"]', content)
                    
                    for imp in import_lines:
                        if imp.startswith('@/'):
                            import_patterns["alias"].append(imp)
                        elif imp.startswith('.'):
                            import_patterns["relative"].append(imp)
                        else:
                            import_patterns["absolute"].append(imp)
                except Exception:
                    continue
        
        self.patterns["import_patterns"] = import_patterns
    
    def _generate_report(self) -> Dict:
        """Generate final analysis report."""
        print("\n✅ Analysis complete!")
        
        # Convert sets to lists for JSON serialization
        for category in self.patterns["design_tokens"]:
            self.patterns["design_tokens"][category] = sorted(list(self.patterns["design_tokens"][category]))
        
        # Calculate most common naming convention
        file_naming = self.patterns["naming_conventions"]["files"]
        if file_naming:
            most_common = max(set(file_naming), key=file_naming.count)
            self.patterns["naming_conventions"]["most_common_file"] = most_common
        
        return self.patterns
    
    def save_report(self, output_path: str):
        """Save analysis report to file."""
        report = self.analyze()
        
        with open(output_path, 'w') as f:
            json.dump(report, f, indent=2)
        
        print(f"📄 Report saved to: {output_path}")
        return report


def main():
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python analyze_project.py <project_path> [output_path]")
        sys.exit(1)
    
    project_path = sys.argv[1]
    output_path = sys.argv[2] if len(sys.argv) > 2 else "project_analysis.json"
    
    analyzer = FrontendAnalyzer(project_path)
    analyzer.save_report(output_path)


if __name__ == "__main__":
    main()
