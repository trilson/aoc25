"""
Advent of Code 2025 - Day 5
https://adventofcode.com/2025/day/5
"""

from pathlib import Path


def parse(input_text: str):
    parsed = [set.splitlines() for set in input_text.strip().split("\n\n")]
    ranges = [list(map(int, row.split('-'))) for row in parsed[0]]
    ingredients = [int(i) for i in parsed[1]]
    return (ranges, ingredients)


def part1(data) -> int:
    ranges, ingredients = data
    compressed = get_compressed(ranges)
    
    count = 0
    for i in ingredients:
        for rg in compressed:
            if i >= rg[0] and i <= rg[1]:
                count += 1
    return count

def get_compressed(ranges):
    compressed = []
    for rg in sorted(ranges, key = lambda x: x[0]):
        if compressed and rg[0] <= compressed[-1][1]:
            compressed[-1][1] = max(compressed[-1][1], rg[1])
        else:
            compressed.append(rg)
    return compressed

def part2(data) -> int:
    return sum([1 + r[1] - r[0] for r in get_compressed(data[0])])

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
