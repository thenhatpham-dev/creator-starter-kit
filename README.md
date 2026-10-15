# Creator Starter Kit

A small, text-only Claude Code plugin for YouTube creators, especially faceless
educational channels. It gives Claude Code a clear project memory for your channel,
a disciplined way to choose topics, and a final quality check before you upload.

> Independent project by The Nhat Pham. Not affiliated with or endorsed by Anthropic.
> "Claude Code" is used only to describe the tool this plugin works with.

## Who it is for

- Solo creators and small teams who script, research and package videos with Claude Code.
- Faceless and educational channels that need sourced facts and consistent quality.
- Freelancers who set up Claude Code for creators and want a clean starting template.

## What is inside

| Path | What it does |
| --- | --- |
| `skills/topic-research/SKILL.md` | Six-gate topic checklist: YouTube search check, velocity vs channel median, Google Trends (YouTube Search), unanswered question, primary-source fact gate, no-repeat and channel fit. Ends with a one-screen decision sheet. |
| `skills/pre-upload-qc/SKILL.md` | 12-point pre-upload check (resolution, fps, duration, loudness, AI disclosure, credits, captions, black frames, first 60 seconds, title/thumbnail match, description, metadata) and an upload-pack template. |
| `templates/CLAUDE.md.template` | Fill-in-the-blanks project memory for your channel: promise, audience, voice, what Claude may and may not do, owner-only decisions, folder layout, quality bar, sources policy, monetization guardrails. |
| `scripts/measure_loudness.py` | Optional. Measures integrated loudness (LUFS), true peak (dBTP) and loudness range for every audio/video file in a folder using your local ffmpeg, and writes a CSV. Measurement only. |

The plugin contains no media generation of any kind: no image, video, voice or
music generation, and no calls to AI media services.

## Install

### Try it for one session (no install)

```bash
claude --plugin-dir ./creator-starter-kit
```

### Install from a local folder (Claude Code CLI)

The folder includes a one-plugin marketplace file, so you can add it by path.
In a Claude Code session:

```text
/plugin marketplace add ./creator-starter-kit
/plugin install creator-starter-kit@creator-starter-kit
```

Or from your shell:

```bash
claude plugin marketplace add ./creator-starter-kit
claude plugin install creator-starter-kit@creator-starter-kit
```

If the kit is hosted in a GitHub repository, replace the path with `owner/repo`.

### Claude desktop app

The desktop app's local sessions read the same settings as the CLI, so a plugin
installed at user scope in the terminal is available there too. To install from
the app: in a local session on the **Code** tab, click **+** next to the prompt
box, choose **Plugins**, then **Add plugin**, and pick Creator Starter Kit after
adding its marketplace as above.

### Check it works

Type `/` in a session and look for `/creator-starter-kit:topic-research` and
`/creator-starter-kit:pre-upload-qc`. Claude also loads them on its own when you
ask things like "is this topic worth making?" or "check my video before upload".

## Customize your CLAUDE.md

1. Copy `templates/CLAUDE.md.template` to the root of your channel folder and rename it `CLAUDE.md`.
2. Replace every `<...>` placeholder. Delete lines that do not apply.
3. Be concrete: "1,400 to 1,800 words" works better than "not too long".
4. Keep the "Decisions only the owner makes" section. Topic, title, thumbnail and publish time stay yours.
5. Update the "Current status" section after each video.

## Optional: loudness measurement

Requires Python 3.9+ and ffmpeg on your PATH. Standard library only.

```bash
python3 scripts/measure_loudness.py ./renders
python3 scripts/measure_loudness.py ./renders --recursive --target-lufs -14 --max-true-peak -1
```

It prints LUFS, dBTP and LRA for each file and writes `loudness_report.csv`
(UTF-8 with BOM, so it opens cleanly in Excel). If ffmpeg is missing it stops
with install instructions. It never re-encodes or changes your files.

## Privacy and safety

- No network calls, no telemetry, no analytics.
- No API keys, tokens or accounts required.
- No hooks, no MCP servers, nothing runs in the background.
- The only executable is the optional loudness script, which runs locally when
  you or Claude call it and writes a single CSV file.
- The research skill asks for read-only browsing at human pace, with no scraping
  tools, in line with YouTube's Terms of Service.

## License

MIT. See [LICENSE](LICENSE). Copyright (c) 2026 The Nhat Pham.
