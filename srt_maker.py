"""Turn a narration script (one line per caption) into an .srt subtitle file.

Usage: python3 srt_maker.py narration.txt [--wps 2.5] > captions.srt
"""
import argparse

WORDS_PER_SECOND = 2.5


def fmt(seconds):
    ms = int(round(seconds * 1000))
    h, ms = divmod(ms, 3_600_000)
    m, ms = divmod(ms, 60_000)
    s, ms = divmod(ms, 1000)
    return f"{h:02}:{m:02}:{s:02},{ms:03}"


def make_srt(lines, wps=WORDS_PER_SECOND):
    out, t = [], 0.0
    for i, line in enumerate((l.strip() for l in lines if l.strip()), 1):
        dur = max(1.0, len(line.split()) / wps)
        out.append(f"{i}\n{fmt(t)} --> {fmt(t + dur)}\n{line}\n")
        t += dur
    return "\n".join(out)


if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("script")
    p.add_argument("--wps", type=float, default=WORDS_PER_SECOND,
                   help="speaking speed in words per second (default 2.5)")
    args = p.parse_args()
    with open(args.script) as f:
        print(make_srt(f, args.wps))
