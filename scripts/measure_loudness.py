#!/usr/bin/env python3
"""Measure loudness of every audio/video file in a folder (measurement only).

Runs ffmpeg's loudnorm filter in analysis mode (print_format=json) and reports
integrated loudness (LUFS), true peak (dBTP) and loudness range (LU) per file.
Nothing is re-encoded, generated or uploaded: output goes to /dev/null and the
only file written is a CSV report.

Requirements: Python 3.9+ (standard library only) and ffmpeg on PATH.

Usage:
    python3 measure_loudness.py FOLDER [--recursive] [--csv PATH]
                                [--target-lufs -14] [--max-true-peak -1]
                                [--tolerance 1.0]
"""
from __future__ import annotations

import argparse
import csv
import json
import shutil
import subprocess
import sys
from pathlib import Path

MEDIA_EXTENSIONS = {
    ".wav", ".mp3", ".m4a", ".aac", ".flac", ".ogg", ".opus", ".aiff", ".aif",
    ".mp4", ".mov", ".mkv", ".webm", ".avi", ".m4v",
}


def find_ffmpeg() -> str:
    path = shutil.which("ffmpeg")
    if not path:
        sys.exit(
            "ERROR: ffmpeg was not found on PATH.\n"
            "Install it first, then run this script again:\n"
            "  macOS:   brew install ffmpeg\n"
            "  Windows: winget install Gyan.FFmpeg  (then open a new terminal)\n"
            "  Linux:   sudo apt install ffmpeg"
        )
    return path


def list_media(folder: Path, recursive: bool) -> list[Path]:
    pattern = "**/*" if recursive else "*"
    return sorted(
        p for p in folder.glob(pattern)
        if p.is_file() and p.suffix.lower() in MEDIA_EXTENSIONS
    )


def extract_json(text: str) -> dict:
    """loudnorm prints its JSON block last on stderr; take the final {...}."""
    end = text.rfind("}")
    start = text.rfind("{", 0, end)
    if start == -1 or end == -1:
        raise ValueError("no loudnorm JSON in ffmpeg output")
    return json.loads(text[start:end + 1])


def measure(ffmpeg: str, path: Path, target: float, max_tp: float) -> dict:
    cmd = [
        ffmpeg, "-hide_banner", "-nostats", "-i", str(path),
        "-vn", "-af",
        f"loudnorm=I={target}:TP={max_tp}:LRA=11:print_format=json",
        "-f", "null", "-",
    ]
    proc = subprocess.run(cmd, capture_output=True, text=True,
                          encoding="utf-8", errors="replace")
    if proc.returncode != 0:
        last = (proc.stderr.strip().splitlines() or ["unknown error"])[-1]
        raise RuntimeError(last)
    data = extract_json(proc.stderr)
    return {
        "integrated_lufs": float(data["input_i"]),
        "true_peak_dbtp": float(data["input_tp"]),
        "lra_lu": float(data["input_lra"]),
    }


def verdict(m: dict, target: float, max_tp: float, tol: float) -> str:
    notes = []
    if abs(m["integrated_lufs"] - target) > tol:
        notes.append(f"loudness off target ({m['integrated_lufs']:+.1f} vs {target:+.1f})")
    if m["true_peak_dbtp"] > max_tp:
        notes.append(f"true peak above {max_tp:+.1f} dBTP")
    return "OK" if not notes else "CHECK: " + "; ".join(notes)


def main() -> int:
    ap = argparse.ArgumentParser(description="Measure loudness (LUFS / dBTP / LRA) of media files with ffmpeg. Measurement only.")
    ap.add_argument("folder", type=Path, help="folder containing audio/video files")
    ap.add_argument("--recursive", action="store_true", help="include subfolders")
    ap.add_argument("--csv", type=Path, default=None, help="CSV path (default: FOLDER/loudness_report.csv)")
    ap.add_argument("--target-lufs", type=float, default=-14.0, help="integrated loudness target (default -14)")
    ap.add_argument("--max-true-peak", type=float, default=-1.0, help="true-peak ceiling in dBTP (default -1)")
    ap.add_argument("--tolerance", type=float, default=1.0, help="allowed LU deviation from target (default 1.0)")
    args = ap.parse_args()

    if sys.version_info < (3, 9):
        sys.exit("ERROR: Python 3.9 or newer is required.")
    folder = args.folder.expanduser().resolve()
    if not folder.is_dir():
        sys.exit(f"ERROR: not a folder: {folder}")

    ffmpeg = find_ffmpeg()
    files = list_media(folder, args.recursive)
    if not files:
        print(f"No audio/video files found in {folder}")
        return 1

    csv_path = (args.csv or folder / "loudness_report.csv").expanduser().resolve()
    rows = []
    print(f"{'file':40} {'LUFS':>7} {'dBTP':>7} {'LRA':>5}  verdict")
    for f in files:
        rel = str(f.relative_to(folder))
        try:
            m = measure(ffmpeg, f, args.target_lufs, args.max_true_peak)
            v = verdict(m, args.target_lufs, args.max_true_peak, args.tolerance)
            print(f"{rel[:40]:40} {m['integrated_lufs']:7.1f} {m['true_peak_dbtp']:7.1f} {m['lra_lu']:5.1f}  {v}")
            rows.append({"file": rel, **m, "verdict": v})
        except Exception as exc:  # report and continue with the next file
            print(f"{rel[:40]:40} {'-':>7} {'-':>7} {'-':>5}  ERROR: {exc}")
            rows.append({"file": rel, "integrated_lufs": "", "true_peak_dbtp": "",
                         "lra_lu": "", "verdict": f"ERROR: {exc}"})

    with open(csv_path, "w", newline="", encoding="utf-8-sig") as fh:
        w = csv.DictWriter(fh, fieldnames=["file", "integrated_lufs", "true_peak_dbtp", "lra_lu", "verdict"])
        w.writeheader()
        w.writerows(rows)
    print(f"\nCSV written: {csv_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
