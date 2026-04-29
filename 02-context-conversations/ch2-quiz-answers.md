# Chapter 2 Mastery Quiz: Context and Conversations

## Questions and Answers

**1. What does the `@` symbol do in Copilot CLI prompts?**
- It references files, directories, or images, giving Copilot CLI access to their contents for context-aware responses.

---

**2. Why is providing context important when working with Copilot CLI?**
- Providing context (using `@` references) helps Copilot CLI give more targeted, accurate, and helpful responses, similar to how a colleague helps more when given details.

---

**3. Give an example of referencing multiple files in a single prompt.**
- `> Compare @samples/book-app-project/book_app.py and @samples/book-app-project/books.py for consistency`

---

**4. How do you reference an entire directory for review?**
- Use `@folder/`, e.g., `> Review all files in @samples/book-app-project/ for error handling`

---

**5. What is cross-file intelligence and why is it useful?**
- It's Copilot CLI's ability to analyze relationships, patterns, and issues across multiple files, revealing bugs and architectural issues that single-file analysis would miss.

---

**6. How do you resume your last Copilot CLI session?**
- Run `copilot --continue`

---

**7. How do you resume a specific session by name or ID?**
- Use `copilot --resume` to pick from a list, or `copilot --resume <session-id>` for a specific session.

---

**8. How do you rename a session for easier resuming later?**
- Use `/rename <session-name>` inside an interactive session.

---

**9. What command shows how much context (tokens) you are using?**
- `/context`

---

**10. What does `/clear` do?**
- It wipes the current context, starting a fresh conversation.

---

**11. How do you share your session as a markdown file?**
- Use `/share file ./my-session.md`

---

**12. What is the benefit of multi-turn conversations in Copilot CLI?**
- Each prompt builds on previous work, allowing for progressive enhancement and more effective, context-aware assistance.

---

**13. Give an example of a context-aware conversation that builds on previous prompts.**
- Start by reviewing a class, then ask for type hints, then for error handling, then for tests—all in one session, with each step building on the last.

---

**14. How do you reference all Python files in a folder using a wildcard?**
- `@folder/*.py`, e.g., `@samples/book-app-project/*.py`

---

**15. What is a context window?**
- The amount of text (files, conversation, system prompts) Copilot CLI can consider at once. Managed with `/context`, `/clear`, and `/compact`.

---

**16. How do you free up space in your context window without losing key findings?**
- Use `/compact` to summarize conversation history and free up tokens.

---

**17. What should you do before switching topics in a session?**
- Run `/clear` to remove irrelevant context.

---

**18. How do you grant Copilot CLI access to a directory if you get a permission error?**
- Use `/add-dir /path/to/directory` or start Copilot CLI with `--add-dir /path/to/directory`.

---

**19. What should you do if your context window is getting full?**
- Use `/compact` to summarize and free up space, or `/clear` to start fresh.
