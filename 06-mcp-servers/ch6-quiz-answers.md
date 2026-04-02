# Chapter 6 Mastery Quiz: MCP Servers

## Questions and Answers

**1. What does MCP stand for, and what does it enable in Copilot CLI?**
- MCP stands for Model Context Protocol. It enables Copilot CLI to connect to external services (like GitHub, filesystem, documentation) for live data access.

---

**2. What is an MCP server? Give three examples.**
- An MCP server is a service Copilot connects to for external data. Examples: GitHub MCP (repo/issues/PRs), Filesystem MCP (local files), Context7 MCP (library documentation).

---

**3. How do you check which MCP servers are enabled?**
- Run `/mcp show` in Copilot CLI.

---

**4. Where are MCP servers configured?**
- User-level: `~/.copilot/mcp-config.json`. Project-level: `.vscode/mcp.json`.

---

**5. What is the built-in MCP server, and what does it provide?**
- The GitHub MCP server is built-in and provides access to repository data, issues, PRs, branches, and commit history.

---

**6. How do you add the filesystem MCP server?**
- Add its config to `~/.copilot/mcp-config.json` and restart Copilot CLI.

---

**7. What is the benefit of using MCP servers in your workflow?**
- MCP servers let Copilot access live, real-world data (e.g., repo history, file system, docs) for more powerful and context-aware workflows.

---

**8. How do you use MCP to list recent commits in your repository?**
- Prompt: `List the last 5 commits in this repository` (uses GitHub MCP).

---

**9. How can you combine multiple MCP servers in a workflow?**
- Use them together in a session (e.g., filesystem MCP for code, GitHub MCP for history, Context7 for docs) to synthesize recommendations.

---

**10. What is the difference between MCP and skills/agents?**
- MCP connects Copilot to external data sources; skills/agents provide instructions and expertise for how Copilot analyzes and generates code.

---

**11. How do you troubleshoot MCP server issues?**
- Use `/mcp show` to check status, validate config files, check authentication, and run server commands manually if needed.

---

**12. What is the purpose of the Context7 MCP server?**
- To provide up-to-date documentation for popular frameworks and libraries.

---

**13. How do you enable a disabled MCP server?**
- Run `/mcp enable <server-name>` in Copilot CLI.

---

**14. What is a multi-server workflow?**
- A workflow that combines data from multiple MCP servers (e.g., code, repo history, docs) in a single session for richer analysis.

---

**15. How do you check if MCP is working in your Copilot CLI session?**
- Run `/mcp show` and try a prompt like `List the recent commits in this repository`.
