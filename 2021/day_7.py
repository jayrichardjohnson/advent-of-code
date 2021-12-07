#!/usr/bin/env python3 
from dataclasses import dataclass
from pathlib import Path
from typing import Counter, Dict, List, NamedTuple

import numpy as np
from numpy.typing import NDArray

@dataclass
class Crabs:
    x : NDArray[np.int_] 

    def part1(self) -> int:
        return min([np.sum(np.abs(self.x - position)) for position in range(self.x.max())])

    def part2(self) -> int:
        # triangular number calculation tri_sum(n) = n*(n+1) / 2
        fuel_cost = [] 
        for position in range(self.x.max()):
            travel_distance = np.abs(self.x - position)
            fuel_cost.append(int(np.sum( travel_distance * (travel_distance + 1) / 2)))
              
        return min(fuel_cost) 


    @classmethod
    def from_file(cls, file: str):

        line = Path(file).read_text().strip()
        x = np.array([int(y) for y in line.split(",")], dtype=int)
        return cls(x)


if __name__ == "__main__":
    stem: str = Path(__file__).stem
    
    test_file = Path("examples") / ("test_" + stem + ".txt")
    test_something = Crabs.from_file(test_file)
    assert test_something.part1() == 37
    assert test_something.part2() == 168

    input_file = Path("inputs") / (stem + ".txt")
    something = Crabs.from_file(input_file)

    print(f"part1: {something.part1()}")
    print(f"part2: {something.part2()}")
