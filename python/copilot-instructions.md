# 🧭 Python Development Assistant Guide

This guide helps you use the normalized Python prompts effectively for personal projects and POC development. Copy this into your actual Python project and adapt it to your specific needs.

Purpose: Coordinate code improvements, testing, and quality checks using the practical Python prompts in this collection.

---
## 🎯 Focus Areas for Personal Projects
1. **Code Quality**: Clean, readable code that works correctly
2. **Basic Testing**: Cover the important functions and edge cases
3. **Type Hints**: Add helpful type annotations for clarity
4. **Performance**: Fix obvious bottlenecks and inefficiencies
5. **Documentation**: Clear README and function documentation
6. **Style**: Consistent formatting with Flake8 and Black

---
## 📁 Simple Project Structure
```
my_project/
  src/                 # Your main code
    my_project/
      __init__.py
      main.py
      utils.py
  tests/               # Test files
    test_main.py
    test_utils.py
  requirements.txt     # Dependencies
  README.md           # Project documentation
  .flake8            # Style configuration
```
Optional: `pyproject.toml`, `.pre-commit-config.yaml`, `docs/`

---
## 🛠️ Quick Code Review Prompt
```
Use the Python Code Review Assistant to review this code:
[paste your code or file]

Focus on:
- Code correctness and potential bugs
- Readability and maintainability
- Basic performance issues
- Missing error handling
- Simple improvements

Provide practical suggestions with examples.
```

Follow-ups:
- "Show mypy error elimination order (highest leverage first)."
- "Generate diff adding only return type hints to public functions in file X." 
- "List unawaited async calls or blocking sync calls inside async funcs." 

---
## 🔡 Adding Type Hints
```
Use the Python Type Hints Assistant to add type annotations:
[paste your function or class]

Start with:
1. Function parameters and return types
2. Class attributes
3. Complex data structures (dicts, lists)

Focus on helpful annotations that catch common bugs.
```

---
## ⚙️ Performance Check
```
Use the Python Async & Concurrency Assistant for async code:
[paste your async code]

Or use the Database & ORM Assistant for database code:
[paste your models or queries]

Look for:
- Slow loops or inefficient algorithms
- Database N+1 query problems
- Blocking operations in async code
- Memory usage issues
```

---
## 🧪 Adding Tests
```
Use the Python Testing Assistant to create tests:
[paste your function or class]

Create tests for:
- Normal operation (happy path)
- Edge cases and error conditions
- Different input types
- Important business logic

Provide pytest examples that are easy to run.
```

---
## 🛡️ Basic Security Check
```
Use the Python Code Review Assistant to check for security issues:
[paste your code]

Look for:
- User input validation
- SQL injection risks
- File path traversal
- Unsafe deserialization
- Missing error handling

Provide safer alternatives with examples.
``` 

---
## 🧾 Better Logging
```
Use the Python Code Helper to improve logging:
[paste your code with print statements or poor error handling]

Replace:
- print() statements with proper logging
- Bare except clauses with specific exceptions
- Silent failures with informative error messages

Show practical logging examples.
```

---
## 🔄 Improvement Workflow
1. **Code Review**: Use Code Review Assistant for overall assessment
2. **Fix Issues**: Use Code Helper to clean up identified problems
3. **Add Tests**: Use Testing Assistant for important functions
4. **Type Hints**: Use Type Hints Assistant for better IDE support
5. **Style**: Use Code Style Assistant for consistent formatting
6. **Documentation**: Use Documentation Assistant for README and docstrings

---
## ✅ Final Check
- [ ] Code runs without errors
- [ ] Tests pass (if you have them)
- [ ] Flake8 style check passes
- [ ] Functions have clear names and docstrings
- [ ] No obvious security issues
- [ ] README explains how to use the project 

---
## 🗜️ Making Changes
```
When asking for code improvements:
- Request specific, small changes
- Ask for before/after examples
- Focus on one issue at a time
- Test changes before applying more
```

---
## 🧠 Getting Better Responses
If suggestions are too vague, ask for:
```
- Specific code examples
- Step-by-step instructions
- Explanation of why the change helps
- Simple examples I can copy and modify
```

---
## 🧩 Example Improvement Session
```
1. Code review: "What can be improved in this file?"
2. Fix issues: "Help me clean up this function"
3. Add tests: "Create tests for this function"
4. Add types: "Add type hints to this code"
5. Document: "Write a docstring for this function"
6. Style: "Check the formatting of this file"
```

---
## 🧪 Project Setup
```
Use the Python Project Setup Assistant to:
- Create a good project structure
- Set up requirements.txt or pyproject.toml
- Configure Flake8, Black, and pytest
- Create a helpful README template

Start with: "Help me set up a new Python project for [describe your project]"
```

---
## 🔐 Before You're Done
- [ ] Does the code do what you intended?
- [ ] Are there tests for the important parts?
- [ ] Is the code readable and well-organized?
- [ ] Does it handle errors gracefully?
- [ ] Is the README up to date?
- [ ] Can someone else understand and use your code? 

---
## ♻️ Using This Guide
Copy this guide into your actual Python project and adapt it to your needs. Replace examples with your specific project details.

Focus on small, practical improvements that make your code better step by step.
