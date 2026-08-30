"""
Advent of Code 2025 - Day 9
https://adventofcode.com/2025/day/9
"""

import math
import itertools
from shapely.geometry import Polygon
from pathlib import Path


def parse(input_text: str):
    return input_text.strip().splitlines()


def part1(data) -> int:
    corners = [tuple(map(int, x.split(','))) for x in data]
    return max([area(x) for x in itertools.combinations(corners, 2)])

def area(pair):
    return (abs(pair[0][0] - pair[1][0]) + 1) * (abs(pair[0][1] - pair[1][1]) + 1)

def part2(data) -> int:
    corners = [tuple(map(int, x.split(','))) for x in data]
    outer_poly = Polygon(corners)

    return max([area(x) for x in itertools.combinations(corners, 2) if poly_contains(outer_poly, x)])
    
def poly_contains(outer: Polygon, inner_coords) -> bool:
    x1, y1 = inner_coords[0]
    x2, y2 = inner_coords[1]

    rect_poly = Polygon([
        (x1, y1), 
        (x2, y1),
        (x2, y2), 
        (x1, y2)
    ])

    return outer.contains(rect_poly)

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
