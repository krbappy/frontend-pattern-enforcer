# Contributing to Frontend Pattern Enforcer

Thank you for your interest in contributing! This document provides guidelines for contributing to the project.

## 🎯 Ways to Contribute

- **Report bugs** - Found an issue? Open a bug report
- **Suggest features** - Have an idea? Create a feature request
- **Improve documentation** - Help make the docs clearer
- **Submit code** - Fix bugs or add features
- **Share feedback** - Tell us how you're using the skill

## 🐛 Reporting Bugs

Before submitting a bug report:
1. Check existing issues to avoid duplicates
2. Use the latest version of the skill
3. Collect relevant information

**Bug Report Template:**
```
**Description**
Clear description of the bug

**To Reproduce**
Steps to reproduce:
1. Run analyzer on project at path X
2. See error Y

**Expected Behavior**
What should have happened

**Actual Behavior**
What actually happened

**Environment**
- OS: [e.g., macOS 14.1]
- Python version: [e.g., 3.11.0]
- Project type: [e.g., React + TypeScript + Tailwind]

**Additional Context**
Any other relevant information
```

## 💡 Suggesting Features

We welcome feature suggestions! Please:
1. Check if the feature is already requested
2. Explain the use case clearly
3. Describe the expected behavior

**Feature Request Template:**
```
**Problem**
What problem would this solve?

**Proposed Solution**
How should it work?

**Alternatives Considered**
Other approaches you've thought about

**Additional Context**
Examples, screenshots, etc.
```

## 🔧 Development Setup

1. **Fork and clone the repository**
   ```bash
   git clone https://github.com/YOUR_USERNAME/frontend-pattern-enforcer.git
   cd frontend-pattern-enforcer
   ```

2. **Create a virtual environment (optional but recommended)**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install development dependencies**
   ```bash
   pip install -r requirements-dev.txt  # If we add one
   ```

4. **Make your changes**
   - Create a new branch: `git checkout -b feature/your-feature-name`
   - Make your changes
   - Test thoroughly

5. **Test your changes**
   ```bash
   # Test the analyzer
   python scripts/analyze_project.py /path/to/test/project test.json
   
   # Test the compliance checker
   python scripts/check_compliance.py test.json /path/to/component.tsx
   
   # Test the report generator
   python scripts/generate_report.py test.json test.md
   ```

## 📝 Code Guidelines

### Python Style
- Follow PEP 8 style guide
- Use meaningful variable names
- Add docstrings to functions
- Keep functions focused and small

**Example:**
```python
def extract_colors(content: str) -> Set[str]:
    """
    Extract color values from CSS/JS content.
    
    Args:
        content: The file content to analyze
        
    Returns:
        Set of unique color values found
    """
    colors = set()
    # Implementation...
    return colors
```

### Documentation
- Update SKILL.md if changing behavior
- Update reference docs if adding features
- Add examples for new functionality
- Keep CHANGELOG.md updated

### Commit Messages
Use clear, descriptive commit messages:
```
feat: Add support for Vue 3 composition API patterns
fix: Handle missing CSS variables gracefully
docs: Update installation instructions
test: Add tests for border-radius extraction
```

Format: `type: description`

Types:
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `test`: Test additions or changes
- `refactor`: Code refactoring
- `chore`: Maintenance tasks

## 🚀 Submitting Pull Requests

1. **Create a branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Make your changes**
   - Write clean, readable code
   - Add tests if applicable
   - Update documentation

3. **Test thoroughly**
   - Test on multiple project types
   - Verify existing functionality still works
   - Check for edge cases

4. **Commit your changes**
   ```bash
   git add .
   git commit -m "feat: Add your feature description"
   ```

5. **Push to your fork**
   ```bash
   git push origin feature/your-feature-name
   ```

6. **Create Pull Request**
   - Go to the original repository
   - Click "New Pull Request"
   - Select your branch
   - Fill in the PR template
   - Submit!

**Pull Request Template:**
```
**Description**
What does this PR do?

**Related Issue**
Fixes #123

**Changes Made**
- Added X
- Fixed Y
- Updated Z

**Testing**
How was this tested?

**Checklist**
- [ ] Code follows style guidelines
- [ ] Documentation updated
- [ ] Tests added/updated
- [ ] CHANGELOG.md updated
- [ ] All tests pass
```

## 🧪 Testing

When adding new features:
1. Test on multiple project types:
   - React + TypeScript + Tailwind
   - Vue + JavaScript + CSS Modules
   - Vanilla JS + SCSS
   - Next.js + Shadcn/ui

2. Test edge cases:
   - Empty projects
   - Projects with no design tokens
   - Very large projects
   - Mixed naming conventions

3. Verify existing functionality:
   - Run analyzer on test projects
   - Check compliance scores are accurate
   - Ensure reports generate correctly

## 📚 Documentation

Good documentation helps everyone:
- **Code comments**: Explain "why", not "what"
- **Docstrings**: Document functions and classes
- **README**: Keep installation steps current
- **Reference docs**: Update for new features
- **Examples**: Add real-world use cases

## 🤝 Code of Conduct

- Be respectful and inclusive
- Welcome newcomers
- Focus on constructive feedback
- Help each other learn

## 📄 License

By contributing, you agree that your contributions will be licensed under the MIT License.

## ❓ Questions?

- Open a GitHub Discussion
- Check existing issues and PRs
- Tag maintainers in your issue/PR

## 🙏 Thank You!

Every contribution, big or small, helps make this project better!

---

**First time contributing to open source?**
- Check out [First Contributions](https://github.com/firstcontributions/first-contributions)
- Don't be afraid to ask questions
- Start with small changes
- Read the code to understand how it works
