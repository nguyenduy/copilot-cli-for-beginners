# Chapter 4 Mastery Quiz: Agents and Custom Instructions

## Questions and Answers

**1. What is an agent in the context of GitHub Copilot CLI? How does it differ from the default assistant?**
- An agent is a specialized AI persona with built-in standards and instructions for a specific task (e.g., code review, testing). Unlike the default assistant, agents focus on domain-specific expertise and follow custom instructions defined in `.agent.md` files.

---

**2. Name at least three built-in agents and describe what each does.**
- Plan: `/plan` creates step-by-step implementation plans before coding.
- Code-review: `/review` reviews staged/unstaged changes with focused, actionable feedback.
- Init: `/init` generates project configuration files (instructions, agents).
- (Explore and Task are also built-in and invoked automatically for codebase analysis and running commands.)

---

**3. How do you invoke the Plan agent to generate an implementation plan for a new feature?**
- Use `/plan` in interactive mode, e.g., `> /plan Add input validation for book year in the book app`.

---

**4. What is the purpose of the `.agent.md` file? What are its two main sections?**
- It defines a custom agent's instructions and metadata. The two main sections are YAML frontmatter (metadata) and markdown instructions.

---

**5. Where should you place agent files for project-wide use? For personal use?**
- Project-wide: `.github/agents/` in the repo. Personal: `~/.copilot/agents/` in your home directory.

---

**6. What is the required field in the YAML frontmatter of an agent file?**
- `description`

---

**7. Give an example of a minimal agent file for a code reviewer.**
```markdown
---
description: Code reviewer focused on bugs and security issues
---

You are a code reviewer focused on finding bugs and security issues.
```

---

**8. How do you switch between agents in Copilot CLI interactive mode?**
- Use `/agent` to list and select agents.

---

**9. What is the difference between using an agent and using a project instruction file?**
- Agents are specialists you invoke on demand for specific tasks; instruction files apply automatically to every session and encode team/project standards.

---

**10. How do you use an agent in programmatic mode?**
- Use `copilot --agent agent-name` to start a session with a specific agent.

---

**11. What are the benefits of using specialist agents over generic prompts? Give an example scenario.**
- Specialist agents provide more thorough, standards-based, and context-aware output (e.g., a python-reviewer agent adds type hints, docstrings, and error handling automatically when generating code).

---

**12. How can you combine multiple agents to work on a feature?**
- Switch between agents mid-session (e.g., use python-reviewer for design, pytest-helper for tests) to get specialized input at each stage.

---

**13. What naming conventions are recommended for agent files?**
- Lowercase with hyphens, include the domain (e.g., `python-reviewer.agent.md`), avoid generic names like `my-agent`.

---

**14. What is the purpose of the `/init` command?**
- It scans your project and generates tailored configuration/instruction files for Copilot CLI.

---

**15. List three common mistakes when creating or using agents, and how to avoid them.**
- Missing `description` in YAML frontmatter (always include it).
- Placing agent files in the wrong location (use `.github/agents/` or `~/.copilot/agents/`).
- Using `.md` instead of `.agent.md` (always use `.agent.md`).

---

**16. What is the recommended file for project-wide instructions that works across Copilot and other AI tools?**
- `AGENTS.md` in the project root.

---

**17. How do you disable custom instructions for a session?**
- Start Copilot CLI with `--no-custom-instructions`.

---

**18. What is the `tools` property in an agent file’s YAML frontmatter used for?**
- To specify which tools (e.g., read, edit, search, execute) the agent can use.

---

**19. How do you test if your agent is available and loaded in Copilot CLI?**
- Run `/agent` to list all available agents and check if yours appears.

---

**20. What is the difference between an agent and a skill in Copilot CLI?**
- Agents change *who* is acting (the persona/expertise); skills change *what steps* are followed (the process or checklist for a task).
