# Advent of Code 2025

Solutions for [Advent of Code 2025](https://adventofcode.com/2025) written in Python.

## Project Structure

```
aoc25/
├── solutions/
│   ├── template.py    # Copy this for each new day
│   ├── day01.py
│   └── ...
├── data/
│   ├── day01.txt      # Actual puzzle input (gitignored)
│   ├── day01.sample.txt  # Sample input from the problem (committed)
│   └── ...
├── pyproject.toml
└── README.md
```

Input file naming:
- `day01.txt` — your personal puzzle input (gitignored)
- `day01.sample.txt` — the sample from the problem description (committed)

## Setup

Install [uv](https://docs.astral.sh/uv/getting-started/installation/) then:

```bash
uv sync
```

## Running Solutions

```bash
# Run with actual input
uv run solutions/day01.py

# Run with sample input
uv run solutions/day01.py --sample
```

## Adding a New Day

1. Copy the template:
   ```bash
   cp solutions/template.py solutions/day02.py
   ```
2. Add your puzzle input to `data/day02.txt`
3. Optionally add the sample input to `data/day02.sample.txt`
4. Implement `parse()`, `part1()`, and `part2()` in the new file

## Notes

- Actual puzzle inputs (`data/day*.txt`) are excluded from version control per [AoC's content policy](https://adventofcode.com/about).
- Sample inputs (`data/day*.sample.txt`) are safe to commit.
