# channel-toolkit-demo

Tiny tools for faceless YouTube channels. Demo repo for a Claude Code Projects tutorial.

- `srt_maker.py`: turns a narration script into an .srt caption file.

## Usage

```
python3 srt_maker.py sample_narration.txt > captions.srt
```

Each non-empty line becomes one caption, timed at about 2.5 words per second. The first captions in `captions.srt` look like:

```
1
00:00:00,000 --> 00:00:04,000
Everything you just saw was made in one free tool.

2
00:00:04,000 --> 00:00:06,800
No camera, no face, no credits bought.
```

Optional: once the `--wps` flag lands, you can set the speaking speed, e.g. `--wps 3`.
