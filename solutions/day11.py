"""
Advent of Code 2025 - Day 11
https://adventofcode.com/2025/day/11
"""

from functools import cache
from pathlib import Path


def parse(input_text: str):
    return input_text.strip().splitlines()


def part1(data) -> int:
    connections = {x: y.split() for x, y in (z.split(":") for z in data)}

    def num_ways(from_device, to_device) -> int:
        if from_device == to_device:
            return 1

        if from_device in connections:
            return sum([num_ways(x, to_device) for x in connections[from_device]])

        return 0

    return num_ways("you", "out")


def part2(data) -> int:
    connections = {x: y.split() for x, y in (z.split(":") for z in data)}

    @cache
    def num_ways(from_device, to_device) -> int:
        if from_device == to_device:
            return 1

        if from_device in connections:
            return sum([num_ways(x, to_device) for x in connections[from_device]])

        return 0

    return (
        num_ways("svr", "fft") * num_ways("fft", "dac") * num_ways("dac", "out")
    ) + (num_ways("svr", "dac") * num_ways("dac", "fft") * num_ways("fft", "out"))


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
