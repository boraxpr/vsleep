#!/usr/bin/env python3
import argparse
import time
from alive_progress import alive_bar


def main():
    parser = argparse.ArgumentParser(description="Sleep with progress bar")
    parser.add_argument("seconds", nargs="?", type=int, help="Total seconds to sleep")
    parser.add_argument("-s", "--sec", type=int, default=0, help="Seconds")
    parser.add_argument("-m", "--min", type=int, default=0, help="Minutes")
    parser.add_argument("-H", "--hour", type=int, default=0, help="Hours")

    args = parser.parse_args()

    total_seconds = (
        args.seconds
        if args.seconds is not None
        else (args.sec + args.min * 60 + args.hour * 3600)
    )

    if total_seconds <= 0:
        parser.error("Please specify a positive number of seconds or time components.")

    try:
        with alive_bar(total_seconds, title="Sleeping") as bar:
            for _ in range(total_seconds):
                time.sleep(1)
                bar()
    except KeyboardInterrupt:
        print("Sleep interrupted")


if __name__ == "__main__":
    main()
