---
name: topic-research
description: Disciplined topic-selection checklist for faceless educational YouTube channels. Use before committing to a new video topic or title, when the user asks "what should I make next", or wants to check whether an idea is saturated, trending, factually solid and on-brand. Produces a one-screen decision sheet; the channel owner makes the final call.
---

# Topic research checklist

Run every gate in order. Stop and report as soon as a gate fails; do not "rescue"
a weak topic by tweaking the title. The output is a decision sheet. The channel
owner decides the topic and the title, never Claude.

## Ground rules

- Browse read-only, at human pace, the way a person would. No scraping tools,
  no bulk downloads, no automated scrolling, no third-party view-count APIs.
- Respect the YouTube Terms of Service and each site's terms.
- Use only the accounts the owner has approved for this channel.
- Record every number you quote with where and when you saw it.
- If `CLAUDE.md` in the project defines the channel promise, niche and audience,
  read it first. Gates 5 and 6 depend on it.

## Gate 1: Search the exact title and topic on YouTube first

Before any other research, paste the planned title, then the core topic phrase,
then one or two keyword variants into YouTube search. For the top 10 to 15 results:

1. List the nearest competitors: title, channel, upload date, views.
2. Is the title saturated? Count near-identical titles from the last 12 months.
   Four or more near-copies is a red flag.
3. Did recent copies win or lose? A copy uploaded in the last 90 days that sits
   below its channel's usual views means the angle is spent.
4. Note the angle each winner took, so the new video can differ, not copy.

Fail if: the exact angle is saturated and recent copies lost.

## Gate 2: Velocity check (is demand rising now?)

For each competitor channel worth checking, open its Videos tab and estimate the
median views of its last 15 uploads. Then compare recent videos on this topic:

- views per day = views / days since upload
- outlier ratio = video views / that channel's median of last 15

Pass if: at least 3 videos on this topic from the last 30 days reached 5x or
more of their own channel's median. One viral video is luck; three is demand.

## Gate 3: Google Trends with the YouTube Search filter

1. Open Google Trends, set the search type to **YouTube Search** (not Web).
2. Compare the topic against one stable benchmark term from the same niche, so
   the scale means something.
3. Look at the last 14 days and the last 12 months.

Pass if: the topic is flat or rising over the last 14 days and not at the tail
of a spike that has already peaked. Write the benchmark term on the sheet.

## Gate 4: Unanswered-question gate

Read the comments on the top 3 competitor videos and related search suggestions.
Write down the specific question viewers still ask that no top video answers well.

Fail if: you cannot write that question in one sentence. Without it the video is
a remake.

## Gate 5: Fact gate

- Use primary sources only: the agency, journal, dataset, court record or
  original paper. Secondary articles are leads, not sources.
- For each key claim, record the source URL and a certainty label:
  **Confirmed** (primary source states it), **Likely** (strong evidence, not
  settled), **Speculative** (hypothesis; must be framed as such on screen).

Fail if: the hook or the title depends on a claim that is only Speculative.

## Gate 6: No-repeat and channel-fit gates

- No-repeat: search the channel's own uploads and planned list. Fail if the same
  question was already covered in the last 6 months, unless the owner wants a
  deliberate sequel.
- Channel fit: does the topic keep the channel promise and serve the stated
  audience and country? Would a subscriber expect it from this channel?
- Policy fit: the video can be made as original work, not repetitive or
  mass-produced content, and any realistic AI visuals can be labeled.

## Output: one-screen decision sheet

Fill this in and show it to the owner. Keep it to one screen.

```text
TOPIC DECISION SHEET            date: ____-__-__   researcher: ______
Working topic:     _____________________________________________
Candidate titles:  1) ______________  2) ______________  (owner picks)

G1 Search check     nearest competitors: ______ / ______ / ______
                    near-copies (12 mo): __   recent copies: won / lost
G2 Velocity         videos >=5x median in 30 days: __ (need >=3)
                    best: "______" __ views/day, __x its channel median
G3 Trends (YT)      benchmark: ______   14-day: rising / flat / falling
G4 Unanswered Q     "_____________________________________________?"
G5 Facts            key claims: __ Confirmed, __ Likely, __ Speculative
                    primary sources: ______, ______
G6 Fit              no repeat: yes/no   promise fit: yes/no   policy: yes/no

Our angle (how this differs from the winners): ____________________
Verdict:  GO / REWORK / DROP     reason: ___________________________
Owner decision: ___________   (topic, title, thumbnail, publish time)
```

If any gate failed, the verdict is REWORK or DROP, and the sheet says which gate
and why. Offer at most two alternative angles, then stop and wait for the owner.
