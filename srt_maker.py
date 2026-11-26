"""Turn a narration script (one line per caption) into an .srt subtitle file.

Usage: python3 srt_maker.py narration.txt > captions.srt
"""
import sys

WORDS_PER_SECOND = 2.5


def fmt(seconds):
    ms = int(round(seconds * 1000))
    h, ms = divmod(ms, 3_600_000)
    m, ms = divmod(ms, 60_000)
    s, ms = divmod(ms, 1000)
    return f"{h:02}:{m:02}:{s:02},{ms:03}"


def make_srt(lines):
    out, t = [], 0.0
    for i, line in enumerate((l.strip() for l in lines if l.strip()), 1):
        dur = max(1.0, len(line.split()) / WORDS_PER_SECOND)
        out.append(f"{i}\n{fmt(t)} --> {fmt(t + dur)}\n{line}\n")
        t += dur
    return "\n".join(out)


if __name__ == "__main__":
    with open(sys.argv[1]) as f:
        print(make_srt(f))
