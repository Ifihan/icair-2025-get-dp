# Contributing to Profile Picture Generator

Thank you for your interest in contributing to this project! This boilerplate is designed to help communities and events create customized profile picture generators.

## Ways to Contribute

### 1. Report Bugs

If you find a bug, please create an issue with:
- A clear, descriptive title
- Steps to reproduce the issue
- Expected vs actual behavior
- Screenshots if applicable
- Your environment (OS, Python version, browser)

### 2. Suggest Enhancements

We welcome feature suggestions! Please create an issue describing:
- The problem you're trying to solve
- Your proposed solution
- Any alternative solutions you've considered
- Whether you're willing to implement it

### 3. Submit Pull Requests

We love pull requests! Here's how to contribute code:

## Development Setup

1. **Fork and clone the repository**
   ```bash
   git clone https://github.com/your-username/icair-get-dp.git
   cd icair-get-dp
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   uv sync
   # or
   pip install -e ".[dev]"
   ```

4. **Create a new branch**
   ```bash
   git checkout -b feature/your-feature-name
   # or
   git checkout -b fix/your-bug-fix
   ```

## Coding Guidelines

### Python Code Style

- Follow [PEP 8](https://peps.python.org/pep-0008/) style guide
- Use meaningful variable and function names
- Add docstrings to functions and classes
- Keep functions focused and single-purpose
- Maximum line length: 88 characters (Black formatter default)

### HTML/CSS/JavaScript

- Use consistent indentation (2 spaces)
- Keep styles organized and commented
- Follow existing naming conventions
- Ensure mobile responsiveness
- Test across different browsers

### Comments

- Add comments for customization points
- Mark sections clearly with headers
- Explain "why" not "what" in complex logic
- Keep comments up-to-date with code changes

## Pull Request Process

1. **Update documentation**
   - Update README.md if you add features
   - Update CUSTOMIZATION_CHECKLIST.md if you add customization points
   - Add inline comments for new customization sections

2. **Test your changes**
   - Test with different image formats (PNG, JPG, HEIC)
   - Test with various name lengths (short, medium, long)
   - Test on mobile and desktop
   - Verify social sharing still works

3. **Commit your changes**
   ```bash
   git add .
   git commit -m "Add a clear, descriptive commit message"
   ```

   Commit message format:
   - `feat: Add new feature`
   - `fix: Fix bug description`
   - `docs: Update documentation`
   - `style: Format code`
   - `refactor: Refactor code structure`
   - `test: Add or update tests`

4. **Push to your fork**
   ```bash
   git push origin feature/your-feature-name
   ```

5. **Create a Pull Request**
   - Use a clear, descriptive title
   - Describe what changed and why
   - Reference any related issues
   - Add screenshots for UI changes

## Types of Contributions We're Looking For

### High Priority

- **Bug fixes** - Anything that's broken
- **Performance improvements** - Faster image processing
- **Accessibility improvements** - Better screen reader support, keyboard navigation
- **Cross-browser compatibility** - Ensuring it works everywhere
- **Documentation improvements** - Clearer setup instructions, better examples

### Medium Priority

- **New customization options** - More ways to customize the output
- **Additional image formats** - Support for WebP, AVIF, etc.
- **UI enhancements** - Better user experience
- **Code refactoring** - Cleaner, more maintainable code

### Nice to Have

- **Internationalization** - Support for multiple languages
- **Additional export formats** - PDF, SVG, etc.
- **Advanced text styling** - Multiple fonts, colors, gradients
- **Batch processing** - Generate multiple images at once

## Code Review Process

- All submissions require review before merging
- Maintainers will provide constructive feedback
- Changes may be requested before approval
- Be patient and respectful during the review process

## Community Guidelines

### Be Respectful

- Use welcoming and inclusive language
- Respect differing viewpoints and experiences
- Accept constructive criticism gracefully
- Focus on what's best for the community

### Be Collaborative

- Help others who are contributing
- Share knowledge and best practices
- Review others' pull requests when possible
- Celebrate contributions from everyone

### Be Professional

- Stay on topic in discussions
- Keep feedback constructive and actionable
- Assume good intentions from contributors
- Follow the project's code of conduct

## Getting Help

- **Questions?** Open an issue with the "question" label
- **Stuck?** Ask for help in your pull request
- **Want to chat?** Open a discussion thread

## Recognition

Contributors will be:
- Listed in the project's contributors page
- Mentioned in release notes for significant contributions
- Celebrated in the community

## License

By contributing, you agree that your contributions will be licensed under the MIT License.

## Thank You!

Your contributions make this project better for everyone. Whether you're fixing a typo, adding a feature, or helping with documentation - every contribution matters!

---

**Happy Contributing! 🎉**
