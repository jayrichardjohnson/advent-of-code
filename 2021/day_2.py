#!/usr/bin/env python3 

from pathlib import Path
from typing import List

def part1(input): 
    r = (0, 0)
    for line in input:
        direction, step, *rest = line.split(" ")
        r = sub_movement(r, direction, step) 
    return r[0] * r[1]

def part2(input):
    aim, z, x = 0, 0, 0
    for line in input:
        direction, step, *rest = line.split(" ")
        
        if direction == 'up':
            aim -= int(step)
        elif direction == 'down':
            aim += int(step)
        elif direction == 'forward':
            x += int(step)
            z += int(step) * aim

    return x * z

def sub_movement(r, direction, step):
    return {
        'forward' : (r[0] + int(step), r[1]),
        'up' : (r[0], r[1] - int(step)),
        'down' : (r[0], r[1] + int(step))
    }.get(direction, r)

if __name__ == "__main__":
    stem: str = Path(__file__).stem
    input_file = Path("data") / (stem + ".txt")
    input: List[str] = input_file.read_text().splitlines()

    print(part1(input), part2(input))
