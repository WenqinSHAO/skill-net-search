"""Convert a Claude Code session JSONL transcript into readable markdown.

Usage:
    python projects/nvidia-academia-ecosystem/scripts/dump_transcript.py \
        ~/.claude/projects/-home-wenqin-net-search/0f695a4d-f400-4900-8d95-8215958b4fd0.jsonl \
        -o projects/nvidia-academia-ecosystem/TRANSCRIPT.md
"""

import json, sys, argparse, os, glob, re
from datetime import datetime


def load_transcript(path):
    messages = []
    with open(path) as f:
        for line in f:
            try:
                obj = json.loads(line)
            except json.JSONDecodeError:
                continue
            if obj.get("type") in ("user", "assistant"):
                msg = obj.get("message", {})
                content = msg.get("content", "")
                if isinstance(content, list):
                    # tool_use blocks have nested content
                    parts = []
                    for block in content:
                        if isinstance(block, dict):
                            if block.get("type") == "text":
                                parts.append(block.get("text", ""))
                            elif block.get("type") == "tool_use":
                                parts.append(f"[Tool: {block.get('name','')}]")
                            elif block.get("type") == "tool_result":
                                parts.append("[Tool result]")
                        else:
                            parts.append(str(block))
                    content = "\n".join(parts)
                if content and content.strip():
                    messages.append({
                        "role": obj["type"],
                        "ts": obj.get("timestamp", ""),
                        "content": content.strip(),
                    })
    return messages


def render_markdown(messages):
    lines = []
    lines.append("# NVIDIA Academia-Ecosystem Report — Conversation Transcript\n")
    lines.append(f"Generated {datetime.now().strftime('%Y-%m-%d %H:%M')}\n")
    lines.append("---\n")

    for i, m in enumerate(messages, 1):
        role = "**Shiye (Claude)**" if m["role"] == "assistant" else "**My lord (User)**"
        lines.append(f"### [{i}] {role}\n")
        # truncate very long tool results for readability
        body = m["content"]
        if len(body) > 8000:
            body = body[:8000] + "\n\n[... content truncated for readability ...]\n"
        lines.append(body)
        lines.append("\n---\n")

    return "\n".join(lines)


def render_html(messages, title="Transcript"):
    rows = []
    for i, m in enumerate(messages, 1):
        role = "Shiye" if m["role"] == "assistant" else "User"
        css_class = "assistant" if m["role"] == "assistant" else "user"
        body = m["content"].replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
        body = re.sub(r'```(\w+)?\n(.*?)```', r'<pre><code>\2</code></pre>', body, flags=re.DOTALL)
        body = re.sub(r'`([^`]+)`', r'<code>\1</code>', body)
        body = body.replace("\n\n", "</p><p>").replace("\n", "<br>")
        body = f"<p>{body}</p>"
        rows.append(f'<div class="msg {css_class}"><div class="msg-head">[{i}] {role}</div>{body}</div>')

    return f"""<!DOCTYPE html>
<html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title>
<style>
body{{font-family:system-ui,-apple-system,sans-serif;max-width:900px;margin:0 auto;padding:20px;background:#f9f9f9;color:#222;line-height:1.6}}
h1{{border-bottom:2px solid #76B900;padding-bottom:8px}}
.msg{{margin:16px 0;padding:14px 18px;border-radius:8px;border-left:4px solid #ccc}}
.user{{background:#e8f5e9;border-left-color:#76B900}}
.assistant{{background:#fff;border-left-color:#1A1A1A}}
.msg-head{{font-weight:700;font-size:13px;color:#555;margin-bottom:6px}}
code{{background:#eee;padding:1px 4px;border-radius:3px;font-size:13px}}
pre{{background:#1A1A1A;color:#76B900;padding:12px 16px;border-radius:6px;overflow-x:auto}}
pre code{{background:transparent;padding:0}}
</style></head><body>
<h1>{title}</h1>
<p>Generated {datetime.now().strftime('%Y-%m-%d %H:%M')} &mdash; {len(messages)} messages</p>
{"".join(rows)}
</body></html>"""


def main():
    parser = argparse.ArgumentParser(description="Dump Claude Code transcript to readable format")
    parser.add_argument("path", help="Path to .jsonl transcript file")
    parser.add_argument("-o", "--output", help="Output file path (.md or .html)", default=None)
    parser.add_argument("--format", choices=["md", "html"], default="md", help="Output format")
    args = parser.parse_args()

    if args.output:
        if args.output.endswith(".html"):
            fmt = "html"
        elif args.output.endswith(".md"):
            fmt = "md"
        else:
            fmt = args.format
    else:
        fmt = args.format

    messages = load_transcript(args.path)
    print(f"Loaded {len(messages)} messages", file=sys.stderr)

    if fmt == "html":
        title = os.path.basename(args.path).replace(".jsonl", "")
        output = render_html(messages, title=title)
    else:
        output = render_markdown(messages)

    if args.output:
        with open(args.output, "w") as f:
            f.write(output)
        print(f"Written {len(output)} chars to {args.output}", file=sys.stderr)
    else:
        print(output)


if __name__ == "__main__":
    main()
