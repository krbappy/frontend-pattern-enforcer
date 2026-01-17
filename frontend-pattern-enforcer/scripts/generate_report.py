#!/usr/bin/env python3
"""
Generate a readable markdown report from project analysis.
"""

import json
import sys
from pathlib import Path
from datetime import datetime

def generate_markdown_report(analysis_file: str, output_file: str = None):
    """Convert JSON analysis to readable markdown."""
    
    with open(analysis_file, 'r') as f:
        data = json.load(f)
    
    if output_file is None:
        output_file = analysis_file.replace('.json', '.md')
    
    md_content = []
    
    # Header
    md_content.append(f"# Frontend Project Pattern Analysis")
    md_content.append(f"\n**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    md_content.append("---\n")
    
    # Design Tokens
    md_content.append("## 🎨 Design Tokens\n")
    
    tokens = data.get("design_tokens", {})
    
    if tokens.get("colors"):
        md_content.append("### Colors")
        md_content.append("```css")
        for color in tokens["colors"][:15]:  # Limit to first 15
            md_content.append(color)
        if len(tokens["colors"]) > 15:
            md_content.append(f"... and {len(tokens['colors']) - 15} more")
        md_content.append("```\n")
    
    if tokens.get("shadows"):
        md_content.append("### Box Shadows")
        md_content.append("```css")
        for shadow in tokens["shadows"][:10]:
            md_content.append(shadow)
        if len(tokens["shadows"]) > 10:
            md_content.append(f"... and {len(tokens['shadows']) - 10} more")
        md_content.append("```\n")
    
    if tokens.get("border_radius"):
        md_content.append("### Border Radius")
        md_content.append("```css")
        for radius in tokens["border_radius"][:10]:
            md_content.append(radius)
        if len(tokens["border_radius"]) > 10:
            md_content.append(f"... and {len(tokens['border_radius']) - 10} more")
        md_content.append("```\n")
    
    if tokens.get("spacing"):
        md_content.append("### Spacing")
        md_content.append("```css")
        for space in tokens["spacing"][:10]:
            md_content.append(space)
        if len(tokens["spacing"]) > 10:
            md_content.append(f"... and {len(tokens['spacing']) - 10} more")
        md_content.append("```\n")
    
    # Folder Structure
    md_content.append("## 📁 Folder Structure\n")
    
    structure = data.get("folder_structure", {})
    if structure:
        for folder_type, paths in structure.items():
            md_content.append(f"### {folder_type.title()}")
            for path in paths[:5]:  # Show first 5
                md_content.append(f"- `{path}`")
            if len(paths) > 5:
                md_content.append(f"- ... and {len(paths) - 5} more")
            md_content.append("")
    else:
        md_content.append("*No specific folder patterns detected*\n")
    
    # Component Patterns
    md_content.append("## 🧩 Component Patterns\n")
    
    patterns = data.get("component_patterns", [])
    if patterns:
        # Calculate statistics
        total = len(patterns)
        ts_count = sum(1 for p in patterns if p.get("has_typescript"))
        props_count = sum(1 for p in patterns if p.get("has_props_interface"))
        hooks_count = sum(1 for p in patterns if p.get("uses_hooks"))
        default_export = sum(1 for p in patterns if p.get("exports_default"))
        
        md_content.append(f"Analyzed {total} components:\n")
        md_content.append(f"- **TypeScript usage:** {ts_count}/{total} ({ts_count/total*100:.0f}%)")
        md_content.append(f"- **Props interface defined:** {props_count}/{total} ({props_count/total*100:.0f}%)")
        md_content.append(f"- **Using React hooks:** {hooks_count}/{total} ({hooks_count/total*100:.0f}%)")
        md_content.append(f"- **Default exports:** {default_export}/{total} ({default_export/total*100:.0f}%)")
        md_content.append("")
    else:
        md_content.append("*No component patterns analyzed*\n")
    
    # Naming Conventions
    md_content.append("## 📝 Naming Conventions\n")
    
    naming = data.get("naming_conventions", {})
    most_common = naming.get("most_common_file")
    if most_common:
        md_content.append(f"**Preferred file naming:** `{most_common}`\n")
    else:
        md_content.append("*No clear naming pattern detected*\n")
    
    # Import Patterns
    md_content.append("## 📦 Import Patterns\n")
    
    imports = data.get("import_patterns", {})
    alias_count = len(imports.get("alias", []))
    relative_count = len(imports.get("relative", []))
    absolute_count = len(imports.get("absolute", []))
    
    total_imports = alias_count + relative_count + absolute_count
    
    if total_imports > 0:
        md_content.append(f"- **Path aliases (@/):** {alias_count} ({alias_count/total_imports*100:.0f}%)")
        md_content.append(f"- **Relative imports (./):** {relative_count} ({relative_count/total_imports*100:.0f}%)")
        md_content.append(f"- **Absolute imports:** {absolute_count} ({absolute_count/total_imports*100:.0f}%)")
        md_content.append("")
        
        if alias_count > relative_count:
            md_content.append("**Recommendation:** Project prefers path aliases (@/)\n")
        elif relative_count > alias_count:
            md_content.append("**Recommendation:** Project prefers relative imports\n")
    else:
        md_content.append("*No import patterns detected*\n")
    
    # Write to file
    content = "\n".join(md_content)
    
    with open(output_file, 'w') as f:
        f.write(content)
    
    print(f"✅ Markdown report generated: {output_file}")
    return output_file


def main():
    if len(sys.argv) < 2:
        print("Usage: python generate_report.py <analysis.json> [output.md]")
        sys.exit(1)
    
    analysis_file = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else None
    
    generate_markdown_report(analysis_file, output_file)


if __name__ == "__main__":
    main()
