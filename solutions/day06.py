"""
Advent of Code 2025 - Day 6
https://adventofcode.com/2025/day/6
"""

import math
from pathlib import Path


def parse(input_text: str):
    return input_text.strip().splitlines()


def part1(data) -> int:
    puzzle = [r.split() for r in data]

    inputs = puzzle[0:-1]
    operator = puzzle[-1]

    total = 0
    for i in range(0, len(puzzle[0])):
        result = 0
        elements = [int(j) for j in [x[i] for x in inputs]]

        match operator[i]:
            case '+': result = sum(elements)
            case '*': result = math.prod(elements)
            
        total += result
    return total

def part2(data) -> int:
    inputs = data[0:-1]
    operators = data[-1]

    operator = operators[0]
    total = 0

    numbers = []
    for idx in range(0, len(inputs[0])):
        number = ''.join([x[idx] for x in inputs]).strip()
        if number.strip():
            numbers.append(int(number))
            continue
        
        match operator:
            case '+': total += sum(numbers)
            case '*': total += math.prod(numbers)
        numbers = []
        operator = operators[idx + 1]
    
    match operator:
        case '+': total += sum(numbers)
        case '*': total += math.prod(numbers)       
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
