"""
Advent of Code 2025 - Day 7
https://adventofcode.com/2025/day/7
"""

from functools import cache
from pathlib import Path


def parse(input_text: str):
    data = input_text.strip().splitlines()
    S = (-1, -1)
    splitters = {}
    for i, row in enumerate(data):
        for j, el in enumerate(row):
            if el == 'S':
                S = (i, j)
            elif el == '^':
                if j not in splitters:
                    splitters[j] = list()
                splitters[j].append(i)
    return (S, splitters)


def part1(data) -> int:
    S, splitters = data                
    path = [S]
    splitters_visited = set()

    while path:
        position = path.pop()
        if (position[1] in splitters):
            next_splitter = [s for s in splitters[position[1]] if s > position[0]]

            if next_splitter and (next_splitter[0], position[1]) not in splitters_visited:
                path.append((next_splitter[0], position[1] + 1))
                path.append((next_splitter[0], position[1] - 1))
                splitters_visited.add((next_splitter[0], position[1]))

    return len(splitters_visited)

def part2(data) -> int:    
    S, splitters = data
    
    @cache
    def qs(position) -> int:
        if (position[1] not in splitters):
            return 1
        
        nxt = [s for s in splitters[position[1]] if s > position[0]]
        return 1 if not nxt else qs((nxt[0], position[1] + 1)) + qs((nxt[0], position[1] - 1))

    return qs(S)


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
