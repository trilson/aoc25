"""
Advent of Code 2025 - Day 4
https://adventofcode.com/2025/day/4
"""

from pathlib import Path


def parse(input_text: str):
    return [list(row) for row in input_text.strip().splitlines()]

def part1(data) -> int:
    count = 0
    for r, row in enumerate(data):
        for c, el in enumerate(row):
            if el == '@' and count_surrounding(data, r, c) < 4: 
                count += 1
    return count

def count_surrounding(data, r, c) -> int:
    count = 0
    for (r, c) in [(r+1, c+1), (r+1, c), (r+1, c-1), (r-1, c+1), (r-1, c), (r-1, c-1), (r, c-1), (r, c+1)]:
        if r >= 0 and r < len(data) and c >= 0 and c < len(data[0]) and data[r][c] == '@':
            count += 1
    return count

def part2(data) -> int:
    total = 0    
    while True:
        count = 0
        for r, row in enumerate(data):
            for c, el in enumerate(row):
                if el == '@' and count_surrounding(data, r, c) < 4: 
                    count += 1
                    data[r][c] = '.'
        total += count
        if count == 0:
            break

    return total


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
