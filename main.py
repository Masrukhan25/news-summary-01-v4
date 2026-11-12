"""Entry program for the Wednesday 11 November 2026 news-summary contest."""

import os

SUMMARY = (
"World news: Wednesday 11 November 2026\n"
"1. Russia and Ukraine agreed in principle to a large-scale prisoner-of-war exchange, the biggest of the war, according to envoy Jared Kushner; no ceasefire.\n"
"2. COP31 opened in Antalya, Turkey, with 102 leaders attending, and UN chief Antonio Guterres warned the world is on a path to destruction.\n"
"3. Russia's ambassador to the U.S., Alexander Darchiev, aged 66, died unexpectedly on 11 November, Russian foreign ministry said late that day.\n"
"4. Russia hit six Ukrainian substations and a market in Chornomorsk, killing 3 and wounding 11, while Ukraine damaged five tanks at Ust-Luga.\n"
"5. NATO jets scrambled after four drones entered Baltic airspace, and a U.S. soldier was held in Britain on suspicion of spying for Russia.\n"
"6. Gadi Eisenkot was tasked with forming Israel's government as the 26th Knesset was sworn in, with 67 lawmakers against 46 for Benjamin Netanyahu.\n"
"7. Seven people were killed in Gaza, including a father and his 13-year-old son; strikes hit southern Lebanon; Saudi Arabia intercepted seven Houthi missiles and drones aimed at Riyadh.\n"
"8. President Trump paused strikes on Iran, and Rubio said no major combat was needed; three Iran-backed operatives were charged over 20 plots including RAF Fairford.\n"
"9. The Nvidia board discussed chief executive Jensen Huang's future, the Wall Street Journal reported, and shares fell 8.6 percent.\n"
"10. The House blocked the impeachment of Pete Hegseth by 211-204, and Democrat Scott Colom won the Mississippi Senate race.\n"
"11. Markets: S&P 500 +1.31% to 7,619.38; Nasdaq +1.60% to 25,466.19; Brent crude settled at $92.76, up 1.39%.\n"
"12. Spain held its first general strike in 14 years, with 4 million workers protesting housing costs.\n"
"13. Poland began two days of mourning for six Krakow mass-shooting victims.\n"
"14. The United Kingdom's top court struck down Trinidad and Tobago's colonial-era ban on gay sex.\n"
"15. Delhi's post-Diwali air averaged 299, with young pupils shifted to hybrid classes."
)


def main():
    n = len(SUMMARY)
    if not (1 <= n <= 2000):
        raise ValueError(f"Summary length {n} is outside 1–2000")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(SUMMARY)


if __name__ == "__main__":
    main()