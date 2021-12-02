#!/usr/bin/env python3 

from pathlib import Path
from typing import List

def part1(input): 


    return 'not done'


def part2(input):


    return 'not done'


if __name__ == "__main__":
    stem: str = Path(__file__).stem
    input_file = Path("data") / (stem + ".txt")
    input: List[str] = input_file.read_text().splitlines()

    print(part1(input), part2(input))
