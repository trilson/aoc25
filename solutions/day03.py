"""
Advent of Code 2025 - Day 3
https://adventofcode.com/2025/day/3
"""

from functools import cache
from pathlib import Path
import math
import itertools

def parse(input_text: str):
    return input_text.strip().splitlines()


def part1(data) -> int:
    result = 0
    for bank in data:   
        max_fwd = []
        max_rwd = []
        mf = -math.inf
        mr = -math.inf
        
        batteries = list(map(int, bank))
        len_bat = len(batteries)

        for i, _bat in enumerate(map(int, bank)):
            mf = max(batteries[i], mf)
            max_fwd.append(mf)

            mr = max(batteries[len_bat - i - 1], mr)
            max_rwd.append(mr)
        
        max_candidate = 0
        for i in range(0, len_bat - 1):
            candidate = (max_fwd[i] * 10) + max_rwd[len_bat - i - 2]
            max_candidate = max(candidate, max_candidate)
        result += max_candidate

    return result

def part2(data) -> int:
    result = 0
    for bank in data:
        result += int(find_max(bank, 12))
    return result


@cache
def find_max(bank, remaining) -> str:
    if remaining == 0:
        return ''
        
    cur_max = ''
    limit = len(bank) - remaining + 1
    
    for i in range(0, limit):        
        cur_max = max(cur_max, bank[i] + find_max(bank[i+1:], remaining - 1))
    
    return cur_max

def part2_alt(data) -> int:
    result = 0
    for bank in data:
        stack = []
        for i, ch in enumerate(bank):
            while stack and ch > stack[-1] and (len(stack) - 1 + len(bank) - i) >= 12:
                stack.pop()
            if len(stack) < 12:
                stack.append(ch)

        result += int(''.join(stack))
    return result

def solve(input_text: str):
    data = parse(input_text)
    print(f"Part 1: {part1(data)}")
    print(f"Part 2: {part2(data)}")
    print(f"Part 2_alt: {part2_alt(data)}")

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
