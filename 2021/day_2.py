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
    # define vector with (x, z, aim)
    r = (0, 0, 0) 
    for line in input:
        direction, step, *rest = line.split(" ")
        r = sub_movement_aim(r, direction, step)        
#        if direction == 'up':
#            r[2] -= int(step)
#        elif direction == 'down':
#            r[2] += int(step)
#        elif direction == 'forward':
#            r[0] += int(step)
#            r[1] += int(step) * aim
#
    return r[0] * r[1]

def sub_movement(r, direction, step):
    return {
        'forward' : (r[0] + int(step), r[1]),
        'up' : (r[0], r[1] - int(step)),
        'down' : (r[0], r[1] + int(step))
    }.get(direction, r)

def sub_movement_aim(r, direction, step):
    return {
            'forward' : (r[0] + int(step), r[1] + int(step) * r[2], r[2]),
            'up' : (r[0], r[1], r[2] - int(step)), 
            'down' : (r[0], r[1], r[2] + int(step))
            }.get(direction, r)

if __name__ == "__main__":
    stem: str = Path(__file__).stem
    input_file = Path("data") / (stem + ".txt")
    input: List[str] = input_file.read_text().splitlines()

    print(f"Part 1: {part1(input)}\nPart 2: {part2(input)}")
