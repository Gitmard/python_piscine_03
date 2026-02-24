#!/usr/bin/env python3

import sys


def lst_mapi(lst: list[any], fn: callable) -> list[any]:
    mapped = []
    for el in lst:
        mapped.append(fn(el))
    return mapped


def avg(lst: list[int]):
    total = 0
    for score in lst:
        total += score
    return total / len(lst)


def main():
    print("=== Player Score Analytics ===")

    if len(sys.argv) <= 1:
        print(
            "No scores provided, Usage: python3",
            "ft_score_analytics.py <score1> <score2> .."
        )
        return

    mapped: list[int] = []
    try:
        mapped = lst_mapi(sys.argv[1:], int)
    except ValueError as value_error:
        print(f"A ValueError occured while mapping scores:\n{value_error}")
        return

    print(f"Scores processed: {mapped}")
    print(f"Total players: {len(mapped)}")
    print(f"Total score: {sum(mapped)}")
    print(f"Average score: {avg(mapped)}")
    print(f"High score: {max(mapped)}")
    print(f"Low score: {min(mapped)}")
    print(f"Score range: {max(mapped) - min(mapped)}")


if __name__ == "__main__":
    main()
