# World News Summary — 11 November 2026

This entry is a news-summary program that produces one ranked, 15-item English summary of the world news of Wednesday 11 November 2026 for a contest judged pairwise by readability. Its editorial approach leads with the day's hardest stories first, keeps every claim tied to a named source, orders items by importance, and stays strictly within the target length so the text itself carries the full weight.

## Running

The program is fully deterministic and depends on no third-party libraries. Run it with Python 3:

    python3 main.py

The summary is written as UTF-8 text to `entry.txt` inside the output directory given by the `MAKEFUN_OUTPUT_DIR` environment variable, which defaults to `/output`.