"""
Advent of Code 2025 - Day 8
https://adventofcode.com/2025/day/8
"""

import math
from math import sqrt
import itertools
import networkx as nx
from pathlib import Path


def parse(input_text: str):
    return input_text.strip().splitlines()


def part1(data) -> int:
    locations = [tuple(map(int, x.split(','))) for x in data]

    G = nx.Graph()
    G.add_nodes_from([tuple(map(int, x.split(','))) for x in data])

    # Brute force - iterate over all combinations
    pairs = itertools.combinations(G, 2)
    shortest = sorted(pairs, key = lambda x: euclidean(x))
    
    for i in range(0, 1000):
        G.add_edge(shortest[i][0], shortest[i][1])
    
    return math.prod([len(x) for x in sorted(nx.connected_components(G), key = lambda x: -len(x))[0:3]])

def euclidean(pair):
    return sqrt((pair[0][0] - pair[1][0])**2 + (pair[0][1] - pair[1][1])**2 + (pair[0][2] - pair[1][2])**2)

def part2(data) -> int:
    locations = [tuple(map(int, x.split(','))) for x in data]
    num_locations = len(locations)

    G = nx.Graph()
    G.add_nodes_from([tuple(map(int, x.split(','))) for x in data])

    # Brute force - iterate over all combinations?
    pairs = itertools.combinations(G, 2)
    shortest = sorted(pairs, key = lambda x: euclidean(x))
    
    # Should we use nx.is_connected() instead?
    for pair in shortest:
        if not nx.has_path(G, pair[0], pair[1]):
            G.add_edge(pair[0], pair[1])
            num_locations -= 1

            if num_locations == 1:
                return pair[0][0] * pair[1][0]


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
