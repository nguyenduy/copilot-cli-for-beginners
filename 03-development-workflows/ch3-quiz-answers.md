# Chapter 3 Mastery Quiz: Development Workflows

## Questions and Answers

**1. List the five main workflows covered in this chapter.**
- Code Review
- Refactoring
- Debugging
- Test Generation
- Git Integration

---

**2. What symbol do you use to reference a file or directory in a Copilot CLI prompt?**
- B) @

---

**3. What is the advantage of using the `/review` command instead of a free-form prompt for code review?**
- `/review` invokes a specialized code-review agent that provides focused, actionable feedback on staged/unstaged changes, with higher signal-to-noise than a generic prompt.

---

**4. When reviewing code for input validation, what should you include in your prompt to get focused feedback?**
- Specify the concern (e.g., input validation) and list categories to check, such as missing validation, error handling gaps, and edge cases.

---

**5. How does Copilot CLI help with cross-file or project-wide reviews?**
- By referencing an entire directory with `@`, Copilot CLI can scan and review all files in the project at once.

---

**6. What is the difference between staged and unstaged changes in git? How do you view each?**
- Staged changes are files marked for the next commit (`git diff --staged`), while unstaged changes are modified but not yet staged (`git diff`).

---

**7. Give an example prompt to refactor a function using Copilot CLI.**
- `@samples/book-app-project/book_app.py The command handling uses if/elif chains. Refactor it to use a dictionary dispatch pattern.`

---

**8. Why is it recommended to generate tests before refactoring code?**
- Generating tests first ensures you can verify that the refactor preserves existing behavior and catches regressions.

---

**9. How can you ask Copilot CLI to separate concerns or improve error handling across multiple files?**
- Reference multiple files with `@` and describe the cross-cutting concern, e.g., `@file1.py @file2.py These files have inconsistent error handling. Suggest a unified approach using custom exceptions.`

---

**10. What are some best practices for writing prompts when generating tests with Copilot CLI?**
- Specify the framework (e.g., pytest), list functions or scenarios, and include edge cases and error conditions.

---

**11. Describe the “Test Explosion” effect when using Copilot CLI for test generation.**
- Copilot CLI can generate many comprehensive tests (15+), including edge cases, far beyond the typical 2-3 manually written tests.

---

**12. How can you run all tests in the sample book app project using pytest?**
- `cd samples/book-app-project && python -m pytest tests/`

---

**13. What information should you provide when debugging with Copilot CLI for best results?**
- Describe the symptom, the expected behavior, and reference the relevant file(s).

---

**14. How can Copilot CLI help you understand and fix a stack trace error?**
- Paste the stack trace and reference the file; Copilot CLI will map the error to the code and suggest a fix.

---

**15. What is a security vulnerability Copilot CLI can help you find in code? Give an example.**
- Example: SQL Injection. Prompt: `Find all security vulnerabilities in this Python user service.`

---

**16. How do you generate a conventional commit message using Copilot CLI and git?**
- Stage your changes, then run: `copilot -p "Generate a conventional commit message for: $(git diff --staged)"`

---

**17. What does the `/delegate` command do? When would you use it?**
- `/delegate` hands off a well-defined task to the Copilot coding agent, which works in the background (e.g., for long-running or well-scoped tasks).

---

**18. How can you use Copilot CLI to generate a pull request description?**
- Use a prompt like: `copilot -p "Generate a pull request description for these changes: $(git log main..HEAD --oneline) ..."`

---

**19. What is the purpose of the `/diff` command?**
- `/diff` shows all changes made during your current session, allowing you to review before committing.

---

**20. What is the recommended workflow for fixing a bug, from understanding the issue to committing the fix? List the steps.**
- 1. Understand the bug and analyze the likely cause
- 2. Get detailed analysis
- 3. Implement the fix
- 4. Generate tests
- 5. Commit

---

**21. What are common mistakes when using Copilot CLI for code review or test generation? How can you avoid them?**
- Using vague prompts or not specifying the framework. Avoid by being specific and clear in your prompts.

---

**22. How can you ensure Copilot CLI generates tests using the correct framework?**
- Specify the framework in your prompt, e.g., "Generate tests using pytest (not unittest)".

---

**23. What is the benefit of referencing both a data file and a code file in your prompt?**
- Copilot CLI can understand the full context, such as error handling for corrupted data files.

---

**24. What is the “Bug Detective” pattern, and how does Copilot CLI help with it?**
- Describe a user-reported symptom and reference the file; Copilot CLI traces the root cause and may find related bugs.

---

**25. What is the value of using specific, detailed prompts versus vague ones? Give an example of each.**
- Specific prompts yield focused, actionable results (e.g., "Review for input validation and edge cases"), while vague prompts ("Review this code") give generic feedback.
