"""
Advent of Code 2025 - Day 10
https://adventofcode.com/2025/day/10
"""

from z3 import *
from collections import deque
from pathlib import Path


def parse(input_text: str):
    return input_text.strip().splitlines()


def part1(data) -> int:
    puzzle_parts = [x.split() for x in data]
    total = 0
    for puzzle in puzzle_parts:
        stripped = [x[1:-1] for x in puzzle]
        target = int(''.join(map(lambda x: '0' if x == '.' else '1', stripped[0])), 2)
        
        buttons = []
        for button in [list(map(int, x.split(','))) for x in stripped[1:-1]]:
            parsed = list('0' * len(stripped[0]))
            for el in button:
                parsed[el] = '1'
            buttons.append(int(''.join(parsed), 2))

        bfs = deque([(0, 0)])
        while bfs:
            current, cnt = bfs.popleft()
            success = False
            for button in buttons:
                t = current ^ button
                if t == target:
                    success = True
                    break
                else:
                    bfs.append((t, cnt + 1))
            if success:
                total += cnt + 1
                break
    return total

    puzzle_parts = [x.split() for x in data]
    total = 0
    for puzzle in puzzle_parts:
        stripped = [x[1:-1] for x in puzzle]
        target = list(map(int, stripped[-1].split(',')))        
        buttons = [list(map(int, x.split(','))) for x in stripped[1:-1]]


        print('target', target)      
        current = [0] * len(target)
        while True:
            print('current', current)      
            # find max intersecting button
            # first, elements not at target
            rebels = [idx for idx, (c, t) in enumerate(zip(current, target)) if c < t]
            print('rebels', rebels)

            # f + e = 3
            # f + b = 5
            # e + d + c = 4
            # a + b + d = 7



            # do we have any buttons which contain all of the rebels?

            break

        # for each element not at target, find the maximal button
    return total

def part2(data) -> int:
    puzzle_parts = [x.split() for x in data]
    total = 0
    for puzzle in puzzle_parts:
        stripped = [x[1:-1] for x in puzzle]
        target = list(map(int, stripped[-1].split(',')))        
        buttons = [list(map(int, x.split(','))) for x in stripped[1:-1]]

        opt = Optimize()
        valid_btns = [Int(f'b{i}') for i, b in enumerate(buttons)]
        opt.add([btn >= 0 for btn in valid_btns])

        for idx, num in enumerate(target):
            options = [valid_btns[i] for i, b in enumerate(buttons) if idx in b]
            opt.add(Sum(options) == num)

        opt.minimize(Sum(valid_btns))

        if opt.check() == sat:
            model = opt.model()
            total += model.eval(Sum(valid_btns)).as_long()
            
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
