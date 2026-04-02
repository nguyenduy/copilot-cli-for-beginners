# Chapter 1 Mastery Quiz: First Steps & Modes

## Questions and Answers

**1. What are the three main interaction modes in GitHub Copilot CLI?**
- Interactive, Plan, and Programmatic modes.

---

**2. How do you start an interactive Copilot CLI session?**
- Run `copilot` in your terminal.

---

**3. Give an example of a prompt you could use in interactive mode to review a file for code quality.**
- `> Review @samples/book-app-project/book_app.py for code quality issues and suggest improvements`

---

**4. What does the `@` symbol do in Copilot CLI prompts?**
- It references a file or directory, giving Copilot CLI access to its contents for context-aware responses.

---

**5. How do you exit an interactive Copilot CLI session?**
- Type `/exit`.

---

**6. What is the purpose of Plan mode? How do you invoke it?**
- Plan mode helps you create a step-by-step plan before coding. Invoke it with `/plan` or by pressing Shift+Tab in an interactive session.

---

**7. What is Programmatic mode best for? How do you use it?**
- It's best for automation, scripts, and single-shot commands. Use it with `copilot -p "<your prompt>"`.

---

**8. List three essential slash commands and what they do.**
- `/help`: Show all available commands
- `/clear`: Clear conversation and start fresh
- `/exit`: End the session

---

**9. What is the difference between Interactive and Programmatic mode?**
- Interactive mode maintains context across multiple prompts (like a conversation). Programmatic mode is single-shot: input → output, no memory of previous prompts.

---

**10. How do you get Copilot CLI to explain what a file does?**
- Use a prompt like `> Explain what @samples/book-app-project/books.py does in simple terms`.

---

**11. What is the recommended mode for exploring and iterating on a new feature?**
- Interactive mode.

---

**12. How do you automate reviewing all Python files in a directory using Copilot CLI?**
- Use a shell loop with programmatic mode, e.g., `for file in samples/book-app-project/*.py; do copilot --allow-all -p "Quick code quality review of @$file - critical issues only"; done`

---

**13. What is the purpose of the `/plan` command?**
- To generate a step-by-step implementation plan before coding.

---

**14. What does `/clear` do? When should you use it?**
- It clears the conversation context. Use it when switching topics or starting a new task.

---

**15. What is the key insight about how Copilot CLI works?**
- It's conversational: you can ask questions in plain English, and context builds naturally through the session.
