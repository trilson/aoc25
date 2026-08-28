"""
Advent of Code 2025 - Day 1
https://adventofcode.com/2025/day/1
"""

from pathlib import Path
import math

def parse(input_text: str):
    return input_text.strip().splitlines()


def part1(data) -> int:
    current_location = 50
    count = 0
    for line in data:
        multiplier = -1 if line[0] == 'L' else 1
        current_location += multiplier * int(line[1::])
        current_location = current_location % 100
        if current_location == 0:
            count += 1
    return count

def part2(data) -> int:
    current_location = 50
    count = 0
    for line in data:                
        old_location = current_location
        multiplier = -1 if line[0] == 'L' else 1
        step = multiplier * int(line[1::])
        wraps, current_location = divmod(current_location + step, 100)
        count += abs(wraps)
        if step < 0:
            if current_location == 0:
                count += 1
            if old_location == 0:
                count -= 1
        
    return count


def solve(input_text: str):
    data = parse(input_text)
    print(f"Part 1: {part1(data)}")
    print(f"Part 2: {part2(data)}")


if __name__ == "__main__":
    import sys

    day = Path(__file__).stem  # "day01"
    use_sample = "--sample" in sys.argv

    data_dir = Path(__file__).parent.parent / "data"
    suffix = ".sample.txt" if use_sample else ".txt"
    input_file = data_dir / f"{day}{suffix}"

    if not input_file.exists():
        print(f"Input file not found: {input_file}")
        sys.exit(1)

    solve(input_file.read_text())
