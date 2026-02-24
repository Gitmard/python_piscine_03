#!/usr/bin/env python3

import math


def parse_coordinates(string: str) -> tuple[int, int, int]:
    parsed_coordinates: list[int] = []

    for coordinate in string.split(","):
        parsed_coordinates.append(int(coordinate))
    return tuple(parsed_coordinates)


def vec3_dist(v1: tuple[int, int, int], v2: tuple[int, int, int]):
    (x1, y1, z1) = v1
    (x2, y2, z2) = v2

    return math.sqrt(
        ((x2 - x1)**2) +
        ((y2 - y1)**2) +
        ((z2 - z1)**2)
    )


def ft_round(n: float):
    return int(n * 100) / 100


def main():
    print("=== Game Coordinate System ===\n")

    pos_0 = (0, 0, 0)
    pos = (10, 20, 5)
    print(f"Position created: {pos}")
    print(
        f"Distance between {pos_0} and {pos}:",
        f"{ft_round(vec3_dist(pos_0, pos))}"
    )

    to_parse = "3,4,0"
    print(f"\nParsing coordinates: \"{to_parse}\"")
    pos = parse_coordinates(to_parse)
    print(f"Parsed position: {pos}")
    print(
        f"Distance between {pos_0} and {pos}:",
        f"{ft_round(vec3_dist(pos_0, pos))}"
    )

    to_parse = "abc,def,ghi"
    print(f"\nParsing invalid coordinates: \"{to_parse}\"")
    try:
        pos = parse_coordinates(to_parse)
    except ValueError as value_error:
        print(
            f"Error parsing coordinates: {value_error}",
            f"Error details - Type: {value_error.__class__.__name__}, " +
            f"Args: {value_error.args}",
            sep="\n"
        )

    print("\nUnpacking demonstration:")
    (x, y, z) = pos
    print(f"Player at x={x}, y={y}, z={z}")
    print(f"Coordinates: X={x}, Y={y}, Z={z}")


if __name__ == "__main__":
    main()
