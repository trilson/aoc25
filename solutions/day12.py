"""
Advent of Code 2025 - Day 12
https://adventofcode.com/2025/day/12
"""

from functools import cache
from pathlib import Path


def parse(input_text: str):
    groups = input_text.strip().split("\n\n")

    presents = []
    targets = []
    for group in groups:
        if "x" in group:
            targets = group.splitlines()
        elif ":" in group:
            presents.append(group.splitlines()[1:])

    return (presents, targets)


def part1(data) -> int:
    presents, targets = data

    count = 0
    for grid in targets:
        grid_size, config_pt = grid.split(": ")

        config = tuple(map(int, config_pt.split()))
        cols, rows = map(int, grid_size.split("x"))

        if (cols // 3) * (rows // 3) >= sum(config):
            count += 1

    return count


def part2(data) -> int:
    pass


def solve(input_text: str):
    data = parse(input_text)
    print(f"Part 1: {part1(data)}")
    print(f"Part 2: {part2(data)}")


if __name__ == "__main__":
    import sys

    day = Path(__file__).stem  # e.g. "day01"
    use_sample = "--sample" in sys.argv

    data_dir = Path(__file__).parent.parent / "data"
    suffix = ".sample.txt" if use_sample else ".txt"
    input_file = data_dir / f"{day}{suffix}"

    if not input_file.exists():
        print(f"Input file not found: {input_file}")
        sys.exit(1)

    solve(input_file.read_text())
