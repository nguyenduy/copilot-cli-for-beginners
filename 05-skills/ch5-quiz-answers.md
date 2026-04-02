# Chapter 5 Mastery Quiz: Skills System

## Questions and Answers

**1. What is a skill in GitHub Copilot CLI? How does it differ from an agent?**
- A skill is a folder of instructions (with SKILL.md) that Copilot loads automatically for specific tasks based on your prompt. Agents change *how* Copilot thinks (persona/expertise); skills teach Copilot *how* to complete specific tasks.

---

**2. Where are skills stored for project-wide and personal use?**
- Project-wide: `.github/skills/` in the repo. Personal: `~/.copilot/skills/` in your home directory.

---

**3. How does Copilot decide which skill to use for a prompt?**
- It matches your prompt to the `description` field in each skill's SKILL.md file and loads relevant skills automatically.

---

**4. How can you invoke a skill directly?**
- Use a slash command with the skill name, e.g., `/code-checklist Check books.py for code quality issues`.

---

**5. What is the required file name for a skill definition?**
- `SKILL.md` (case-sensitive)

---

**6. What are the required YAML frontmatter fields in a SKILL.md file?**
- `name` and `description`

---

**7. Give an example of a skill description that would trigger for security reviews.**
- `description: Use for security reviews, vulnerability scanning, checking for SQL injection, XSS, authentication issues, OWASP Top 10 vulnerabilities, and security best practices.`

---

**8. How do you reload skills after editing or adding a SKILL.md file?**
- Run `/skills reload` in Copilot CLI.

---

**9. How do you list all available skills in your project?**
- Run `/skills list` in Copilot CLI.

---

**10. What is the benefit of using skills for code reviews or test generation?**
- Skills ensure consistent, repeatable application of team standards and best practices, saving time and reducing human error.

---

**11. How do you install a community skill from a GitHub repository?**
- Copy the skill folder into `.github/skills/` (project) or `~/.copilot/skills/` (personal), then reload skills.

---

**12. What is the difference between a skill and a plugin?**
- A skill is a single set of instructions for a task; a plugin can bundle multiple skills, agents, and MCP server configs for installation as a package.

---

**13. What is the most important field for skill auto-discovery?**
- The `description` field in SKILL.md.

---

**14. How do you check if a skill was used in a Copilot response?**
- Ask Copilot: "What skills did you use for that response?"

---

**15. What is the recommended way to structure a skill for a team code review checklist?**
- Use a SKILL.md with a clear name, a description matching how your team asks for reviews, and a markdown checklist of all review points.
