"""
Advent of Code 2025 - Day 2
https://adventofcode.com/2025/day/2
"""

from pathlib import Path
import math
import itertools

def parse(input_text: str):
    return input_text.strip().split(',')


def part1(data) -> int:
    sum = 0
    for pair in data:
        split = pair.split('-')
        fr = int(split[0])
        to = int(split[1])

        for order in range(fr, to + 1):
            len_order = int(math.log10(order) + 1)
            if len_order % 2 == 1: continue
            
            front, back = divmod(order, math.pow(10, len_order / 2))
            if front == back:
                sum += order
    return sum


def part2(data) -> int:
    sum = 0
    for pair in data:
        split = pair.split('-')
        fr, to = map(int, pair.split('-'))

        for order in range(fr, to + 1):
            ord_str = str(order)
            for candidate in range(1, 1 + len(ord_str) // 2):
                chunks = itertools.batched(ord_str, candidate)
                if len(set(chunks)) <= 1:
                    sum += order
                    break

    return sum

def part2_alt(data) -> int:
    sum = 0
    for pair in data:
        split = pair.split('-')
        fr, to = map(int, pair.split('-'))
        for order in range(fr, to + 1):
            ord_str = str(order)
            ord_can = (ord_str + ord_str)[1:-1]
            if ord_str in ord_can:
                sum += order
    return sum

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
