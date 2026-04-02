# Chapter 7 Mastery Quiz: Putting It All Together

## Questions and Answers

**1. What is the main benefit of combining agents, skills, and MCP in a workflow?**
- It enables unified, end-to-end workflows that leverage specialized expertise, repeatable best practices, and live data for maximum productivity.

---

**2. Describe the "Idea to Merged PR" workflow using Copilot CLI. List the main steps.**
- Gather context, plan with `/plan`, design with agents, implement, generate tests, review with `/review`, create PR, and document.

---

**3. How do you switch between agents during a session?**
- Use `/agent` to select a different agent at any time.

---

**4. What is the purpose of a pre-commit hook in the context of Copilot CLI?**
- To automatically run reviews (e.g., security checks) on staged files before committing, blocking commits with critical issues.

---

**5. How can you automate code review on every commit?**
- Set up a pre-commit hook script that runs Copilot CLI in programmatic mode for each staged file.

---

**6. What is the "Integration Pattern" for power users?**
- Gather context (MCP), analyze/plan (agents), execute (skills/manual), complete (MCP) — combining all tools in a single workflow.

---

**7. How do you keep sessions focused and easy to resume?**
- Use `/rename` to label sessions and `/exit` to end them cleanly.

---

**8. What is the difference between agents, skills, and custom instructions?**
- Agents: explicit personas you activate; Skills: auto-triggered task instructions; Custom instructions: always-on project/team guidance.

---

**9. How can you share reusable workflows with your team?**
- Encode them in custom instructions, prompt files, agents, and skills within the repository.

---

**10. What is a multi-server workflow and why is it powerful?**
- A workflow that combines data from multiple MCP servers (e.g., code, repo history, docs) for richer, more effective analysis and automation.

---

**11. How do you generate a comprehensive PR description using Copilot CLI?**
- Use programmatic mode with a prompt that includes branch and commit info, e.g., `copilot -p "Generate a PR description for: ..."`

---

**12. What is the recommended first step before analyzing or fixing a bug?**
- Gather context (e.g., get issue details, reference relevant files) before analysis or implementation.

---

**13. How do you ensure your workflow is reproducible for new team members?**
- Document and encode workflows in the repo using agents, skills, instructions, and prompt files.

---

**14. What is the value of using `/plan` before implementing a feature?**
- It helps you think through the approach, catch design issues early, and create a clear roadmap before coding.

---

**15. What is the final success criteria for mastering the course?**
- You can explain how agents, skills, and MCP work together and when to use each for maximum productivity.
