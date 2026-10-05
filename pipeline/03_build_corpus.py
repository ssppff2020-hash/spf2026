#!/usr/bin/env python3
"""C1 pipeline · step 3 — normalise every harvested artefact into one corpus.

Maps each artefact (HTML cache text, live-recovered pages, PDF text) onto a
stable slug, a week bucket, a Chinese title and a declared **output path**, then
writes `<work>/source/<slug>.txt` plus `manifest.json`.

The manifest is the single source of truth for the whole pipeline: step 4 reads
it to know what to translate and where to put it, step 5 reads it to know what to
check and against which source. Keep it in sync and everything else follows.

    python 03_build_corpus.py [--work <dir>]     # default: materials/_work

Re-runnable: edit MAP/OUTPUT below or drop new files into the cache and re-run.
Course-agnostic apart from the MAP tables, which are per-course by nature.
"""
import argparse
import json
import pathlib

# slug -> (source file, week, english title, chinese title)
MAP = [
    ("course-overview", "extracted/index.txt", 0,
     "CS146S Course Overview & Syllabus", "CS146S 课程总览与教学大纲"),

    ("prompt-engineering-overview", "extracted/pages/prompt-engineering-overview.txt", 1,
     "What Is Prompt Engineering?", "什么是提示工程"),
    ("prompt-engineering-guide", "extracted/pages/prompt-engineering-guide.txt", 1,
     "Prompt Engineering Guide: Techniques", "提示工程指南：核心技术"),
    ("how-openai-uses-codex", "extracted_pdf/how-openai-uses-codex.txt", 1,
     "How OpenAI Uses Codex", "OpenAI 如何使用 Codex"),

    ("mcp-introduction", "extracted/pages/mcp-introduction.txt", 2,
     "Model Context Protocol: An Introduction", "模型上下文协议（MCP）简介"),
    ("mcp-server-authentication", "extracted/pages/mcp-server-authentication.txt", 2,
     "Remote MCP Server Authentication", "远程 MCP 服务器认证"),
    ("mcp-registry-preview", "extracted/pages/mcp-registry-preview.txt", 2,
     "MCP Registry Preview", "MCP 注册表预览"),
    ("mcp-food-for-thought", "extracted/pages/mcp-food-for-thought.txt", 2,
     "APIs Don't Make Good MCP Tools", "API 并不是好的 MCP 工具"),

    ("specs-are-the-new-source-code", "extracted/pages/specs-are-the-new-source-code.txt", 3,
     "Specs Are the New Source Code", "规格是新的源代码"),
    ("how-long-contexts-fail", "extracted/pages/how-long-contexts-fail.txt", 3,
     "How Long Contexts Fail", "长上下文为何失效"),
    ("devin-coding-agents-101", "extracted/pages/devin-coding-agents-101.txt", 3,
     "Devin: Coding Agents 101", "Devin：编程智能体入门 101"),
    ("writing-effective-tools-for-agents", "extracted/pages/writing-effective-tools-for-agents.txt", 3,
     "Writing Effective Tools for Agents", "为智能体编写有效的工具"),

    ("how-anthropic-uses-claude-code", "extracted_pdf/how-anthropic-uses-claude-code.txt", 4,
     "How Anthropic Uses Claude Code", "Anthropic 如何使用 Claude Code"),
    # NOTE: the offline cache's copy of this reading is the Claude Code docs
    # *Overview* page, not the best-practices article — the pack's crawler
    # followed a redirect to the docs home. The real article was re-fetched in
    # step 1 to live/best-practices.txt; see C1/AI日志/2026-10-05-05.
    ("claude-code-best-practices", "live/best-practices.txt", 4,
     "Best practices for Claude Code", "Claude Code 最佳实践"),
    ("good-context-good-code", "extracted/pages/good-context-good-code.txt", 4,
     "Good Context, Good Code", "好上下文，好代码"),

    ("warp-vs-claude-code", "extracted/pages/warp-vs-claude-code.txt", 5,
     "Warp vs Claude Code", "Warp 与 Claude Code 对比"),
    ("how-warp-uses-warp", "live/warp-notion.txt", 5,
     "How Warp Uses Warp to Build Warp", "Warp 如何用 Warp 构建 Warp"),

    ("sast-vs-dast", "extracted/pages/sast-vs-dast.txt", 6,
     "SAST vs DAST", "SAST 与 DAST：静态与动态应用安全测试"),
    ("copilot-prompt-injection-rce", "extracted/pages/copilot-prompt-injection-rce.txt", 6,
     "GitHub Copilot Remote Code Execution via Prompt Injection",
     "通过提示注入实现 GitHub Copilot 远程代码执行"),
    ("finding-vulnerabilities-claude-codex", "extracted/pages/finding-vulnerabilities-claude-codex.txt", 6,
     "Finding Vulnerabilities in Modern Web Apps with Claude Code and Codex",
     "用 Claude Code 与 Codex 发现现代 Web 应用漏洞"),
    ("agentic-ai-threats", "extracted/pages/agentic-ai-threats.txt", 6,
     "AI Agents Are Here. So Are the Threats.", "AI 智能体来了，威胁也来了"),
    ("owasp-top-ten", "extracted/pages/owasp-top-ten.txt", 6,
     "OWASP Top Ten", "OWASP Top 10：十大 Web 应用安全风险"),
    ("context-rot", "extracted/pages/context-rot.txt", 6,
     "Context Rot: How Increasing Input Tokens Impacts LLM Performance",
     "上下文腐化：输入 token 增长如何影响大语言模型表现"),

    ("code-reviews-just-do-it", "extracted/pages/code-reviews-just-do-it.txt", 7,
     "Code Reviews: Just Do It", "代码评审：去做就对了"),
    ("how-to-review-code-effectively", "extracted/pages/how-to-review-code-effectively.txt", 7,
     "How to Review Code Effectively", "如何高效地评审代码"),
    ("ai-assisted-code-review-assessment", "extracted_pdf/ai-assisted-code-review-assessment.txt", 7,
     "AI-Assisted Assessment of Coding Practices in Modern Code Review",
     "现代代码评审中 AI 辅助的编码实践评估"),
    ("ai-code-review-best-practices", "extracted/pages/ai-code-review-best-practices.txt", 7,
     "AI Code Review Implementation Best Practices", "AI 代码评审落地最佳实践"),
    ("code-review-essentials", "extracted/pages/code-review-essentials.txt", 7,
     "Code Review Essentials for Software Teams", "软件团队的代码评审要点"),
    ("lessons-from-ai-code-reviews", "live/lessons-transcript.txt", 7,
     "Lessons from Millions of AI Code Reviews (talk transcript)",
     "数百万次 AI 代码评审的经验（演讲字幕）"),

    ("sre-introduction", "extracted/pages/sre-introduction.txt", 9,
     "Introduction to Site Reliability Engineering", "站点可靠性工程（SRE）导论"),
    ("observability-basics", "extracted/pages/observability-basics.txt", 9,
     "Observability Basics You Should Know", "你应该知道的可观测性基础"),
    ("kubernetes-troubleshooting-ai", "extracted/pages/kubernetes-troubleshooting-ai.txt", 9,
     "Kubernetes Troubleshooting with AI", "用 AI 排查 Kubernetes 故障"),
    ("benefits-agentic-ai-oncall", "extracted/pages/benefits-agentic-ai-oncall.txt", 9,
     "Benefits of Agentic AI in On-Call Engineering", "智能体 AI 在值班工程中的价值"),
    ("multi-agent-systems-ai-native", "extracted/pages/multi-agent-systems-ai-native.txt", 9,
     "Role of Multi-Agent Systems in AI-Native Engineering",
     "多智能体系统在 AI 原生工程中的作用"),
]

# slug -> where the finished translation must land. Declaring it here makes the
# manifest the single source of truth for BOTH directions of the pipeline, so
# step 5 can pair source<->translation by path instead of by fuzzy title match.
# Kept in sync with the translation batches described in C1/AI日志/.
OUTPUT = {
    "course-overview": "week00-课程总览/01-CS146S课程总览与教学大纲.md",
    "prompt-engineering-overview": "week01-LLM与提示工程/01-什么是提示工程.md",
    "how-openai-uses-codex": "week01-LLM与提示工程/02-OpenAI如何使用Codex.md",
    "prompt-engineering-guide": "week01-LLM与提示工程/03-提示工程指南-核心技术.md",
    "mcp-introduction": "week02-编程智能体与MCP/01-模型上下文协议MCP简介.md",
    "mcp-server-authentication": "week02-编程智能体与MCP/02-远程MCP服务器认证.md",
    "mcp-registry-preview": "week02-编程智能体与MCP/03-MCP注册表预览.md",
    "mcp-food-for-thought": "week02-编程智能体与MCP/04-API并不是好的MCP工具.md",
    "specs-are-the-new-source-code": "week03-AI-IDE与上下文工程/01-规格是新的源代码.md",
    "how-long-contexts-fail": "week03-AI-IDE与上下文工程/02-长上下文为何失效.md",
    "devin-coding-agents-101": "week03-AI-IDE与上下文工程/03-Devin编程智能体入门101.md",
    "writing-effective-tools-for-agents": "week03-AI-IDE与上下文工程/04-为智能体编写有效的工具.md",
    "how-anthropic-uses-claude-code": "week04-Claude-Code与智能体编码/01-Anthropic如何使用Claude-Code.md",
    "claude-code-best-practices": "week04-Claude-Code与智能体编码/02-Claude-Code最佳实践.md",
    "warp-vs-claude-code": "week05-Warp与AI终端/01-Warp与Claude-Code对比.md",
    "how-warp-uses-warp": "week05-Warp与AI终端/02-Warp如何用Warp构建Warp.md",
    "sast-vs-dast": "week06-AI安全与漏洞检测/01-SAST与DAST.md",
    "copilot-prompt-injection-rce": "week06-AI安全与漏洞检测/02-通过提示注入实现Copilot远程代码执行.md",
    "finding-vulnerabilities-claude-codex": "week06-AI安全与漏洞检测/03-用Claude-Code与Codex发现现代Web应用漏洞.md",
    "agentic-ai-threats": "week06-AI安全与漏洞检测/04-AI智能体来了威胁也来了.md",
    "owasp-top-ten": "week06-AI安全与漏洞检测/05-OWASP-Top-10.md",
    "context-rot": "week06-AI安全与漏洞检测/06-上下文腐化.md",
    "code-reviews-just-do-it": "week07-AI代码评审/01-代码评审去做就对了.md",
    "how-to-review-code-effectively": "week07-AI代码评审/02-如何高效地评审代码.md",
    "ai-assisted-code-review-assessment": "week07-AI代码评审/03-现代代码评审中AI辅助的编码实践评估.md",
    "ai-code-review-best-practices": "week07-AI代码评审/04-AI代码评审最佳实践.md",
    "code-review-essentials": "week07-AI代码评审/05-软件团队的代码评审要点.md",
    "lessons-from-ai-code-reviews": "week07-AI代码评审/06-数百万次AI代码评审的经验.md",
    "sre-introduction": "week09-SRE与可观测性/01-站点可靠性工程SRE导论.md",
    "observability-basics": "week09-SRE与可观测性/02-你应该知道的可观测性基础.md",
    "kubernetes-troubleshooting-ai": "week09-SRE与可观测性/03-用AI排查Kubernetes故障.md",
    "benefits-agentic-ai-oncall": "week09-SRE与可观测性/04-智能体AI在值班工程中的价值.md",
    "multi-agent-systems-ai-native": "week09-SRE与可观测性/05-多智能体系统在AI原生工程中的作用.md",
}

# Items known to be unobtainable in this environment, with the reason.
GAPS = [
    {"slug": "good-context-good-code", "url": "https://blog.stockapp.com/good-context-good-code/",
     "reason": "Ghost 站点需访问码，且域名 DNS 解析失败，环境中无法获取正文"},
    {"slug": "peeking-under-the-hood-of-claude-code",
     "url": "https://medium.com/@outsightai/peeking-under-the-hood-of-claude-code-70f5a94a9a62",
     "reason": "Medium 屏蔽自动抓取，且 medium.com:443 在本环境网络层不可达"},
]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--work", default=str(pathlib.Path(__file__).resolve().parent.parent
                                          / ".." / "materials" / "_work"),
                    help="directory holding extracted/ and live/ (default: materials/_work)")
    args = ap.parse_args()
    work = pathlib.Path(args.work).resolve()
    out = work / "source"
    if not work.is_dir():
        raise SystemExit(f"work dir not found: {work}\n"
                         f"pass --work <dir> pointing at the folder with extracted/ and live/")

    out.mkdir(parents=True, exist_ok=True)
    manifest = []
    for slug, rel, week, en, zh in MAP:
        src = work / rel
        if not src.exists():
            print(f"!! missing source: {rel}")
            continue
        text = src.read_text(encoding="utf-8", errors="replace")
        (out / f"{slug}.txt").write_text(text, encoding="utf-8")
        manifest.append({
            "slug": slug, "week": week, "en_title": en, "zh_title": zh,
            "source_file": rel.replace("\\", "/"),
            "output": OUTPUT.get(slug, ""),
            "chars": len(text), "words": len(text.split()),
            "status": "gap" if len(text) < 500 else "ok",
        })

    payload = {"challenge": "C1", "course": "CS146S The Modern Software Developer (Stanford, Fall 2025)",
               "source_site": "https://themodernsoftware.dev/",
               "items": manifest, "known_gaps": GAPS}
    (out / "manifest.json").write_text(
        json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")

    ok = [m for m in manifest if m["status"] == "ok"]
    print(f"items={len(manifest)} translatable={len(ok)} "
          f"chars={sum(m['chars'] for m in ok):,} words={sum(m['words'] for m in ok):,}")
    print(f"gaps={len(GAPS)}")


if __name__ == "__main__":
    main()
