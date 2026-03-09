#!/usr/bin/env python3

import sys


def avg(lst: list[int]) -> float:
    total = 0
    for score in lst:
        total += score
    return total / len(lst)


def main() -> None:
    print("=== Player Score Analytics ===")
    if len(sys.argv) <= 1:
        print(
            "No scores provided, Usage: python3",
            "ft_score_analytics.py <score1> <score2> .."
        )
        return
    mapped: list[int] = []
    try:
        for param in sys.argv[1:]:
            mapped.append(int(param))
    except ValueError as value_error:
        print(f"A ValueError occured while mapping scores:\n{value_error}")
        return

    print(f"Scores processed: {mapped}")
    print(f"Total players: {len(mapped)}")
    print(f"Total score: {sum(mapped)}")
    print(f"Average score: {avg(mapped):.1f}")
    print(f"High score: {max(mapped)}")
    print(f"Low score: {min(mapped)}")
    print(f"Score range: {max(mapped) - min(mapped)}")


if __name__ == "__main__":
    main()
