---
name: pre-upload-qc
description: 12-point pre-upload quality check for a finished YouTube video, plus an upload-pack template (title, description, chapters, tags, pinned credit comment). Use when a video is rendered and about to be uploaded, or when the user asks to check loudness, captions, AI-content disclosure, credits or metadata before publishing.
---

# Pre-upload QC

Run all 12 checks against the final render, not a draft. Report each as PASS,
FIX or N/A with a one-line reason. Do not mark anything PASS that you did not
actually check. Claude never uploads or publishes; the owner does that.

## Measuring the file

If ffmpeg is installed, these read-only commands answer checks 1 to 4 and 8:

```bash
# Resolution, fps, duration
ffprobe -v error -select_streams v:0 -show_entries stream=width,height,r_frame_rate \
  -show_entries format=duration -of default=nw=1 "final.mp4"

# Loudness for every file in a folder (optional helper bundled with this plugin)
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/measure_loudness.py" ./renders

# Black frames and frozen frames
ffmpeg -hide_banner -nostats -i "final.mp4" -vf "blackdetect=d=0.5:pix_th=0.10,freezedetect=n=-60dB:d=2" -an -f null - 2>&1 | grep -E "black_|freeze_"
```

The loudness helper only measures. It writes a CSV report and changes nothing.
If ffmpeg is missing, say so and ask the owner to check those points by eye
and ear instead of guessing.

## The 12 checks

1. **Resolution**: matches the plan in `CLAUDE.md` (e.g. 3840x2160 or 1920x1080),
   no letterboxing unless intended.
2. **Frame rate**: constant and as planned (e.g. 24, 25, 30 or 60 fps).
3. **Duration**: within the planned range; no silent tail or dead air at the end.
4. **Loudness**: integrated loudness about -14 LUFS (within 1 LU) and true peak
   at or below -1 dBTP, the common YouTube delivery target. Very quiet audio is
   not turned up by YouTube, so -20 LUFS will sound weak.
5. **AI visuals labeled**: if any realistic person, place or event was made or
   altered with AI, the owner must tick YouTube's "altered or synthetic content"
   disclosure in Studio. Also label AI visuals on screen or in the description
   when a viewer could mistake them for real footage.
6. **Source credits**: every real photo, clip, chart and quoted source is listed
   with its creator and licence (or "public domain", "courtesy of ..."), and the
   licence allows this use.
7. **Captions**: an SRT or VTT file exists, matches the final cut, and names,
   numbers and technical terms are spelled correctly.
8. **No black frames or freezes**: the detect command above reports none outside
   intended fades or holds.
9. **Opening delivers the promise within 60 seconds**: the viewer learns what the
   title promised, or clearly sees it coming, in the first minute.
10. **Title and thumbnail match the content**: everything the title or thumbnail
    implies actually appears in the video. No bait.
11. **Description complete**: summary, chapters starting at 00:00 (at least three,
    each 10 s or longer), sources and credits, AI-use note if relevant.
12. **No misleading metadata**: tags, title and description describe this video
    only; no unrelated trending terms, no fake claims of "official" or "leaked".

## Report format

```text
PRE-UPLOAD QC   file: ______________   date: ____-__-__
 1 Resolution        PASS/FIX  ______
 2 Frame rate        PASS/FIX  ______
 3 Duration          PASS/FIX  ______
 4 Loudness          PASS/FIX  __ LUFS, __ dBTP
 5 AI disclosure     PASS/FIX/N/A  ______
 6 Credits           PASS/FIX  ______
 7 Captions          PASS/FIX  ______
 8 Black/freeze      PASS/FIX  ______
 9 First 60 s        PASS/FIX  ______
10 Title/thumb match PASS/FIX  ______
11 Description       PASS/FIX  ______
12 Metadata          PASS/FIX  ______
Ready to upload: YES / NO (fix items: __)
```

## Upload-pack template

Prepare this as a text file next to the video. The owner chooses the final title,
thumbnail and publish time; offer options, not decisions.

```text
UPLOAD PACK  ·  video: ______________

TITLE OPTIONS (owner picks one, keep under ~70 characters)
1. ______________________________
2. ______________________________

DESCRIPTION
<Two-sentence summary that matches the title's promise.>

Chapters
00:00 ______
__:__ ______
__:__ ______

Sources
- ______ (primary source, link)
- ______

Credits
- Footage/images: ______ (licence)
- Music: ______ (licence)
- AI use: <e.g. "Some illustrations are AI-generated and labeled on screen." or "None.">

TAGS (5 to 10, specific to this video)
______, ______, ______

PINNED COMMENT
Sources and image credits are in the description. <One question that invites
discussion of the topic.>

STUDIO CHECKBOXES (owner ticks)
[ ] Altered or synthetic content: yes / no
[ ] Captions file uploaded
[ ] Made for kids: yes / no
Publish time: ________ (owner decides)
```
