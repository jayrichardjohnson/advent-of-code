#!/usr/bin/env python3 
from dataclasses import dataclass
from pathlib import Path
from typing import Counter, Dict, List, NamedTuple

@dataclass
class Something:
    input_value: List[int] 

    def part1(self) -> int:
        return None

    def part2(self) -> int:
        return None

    @classmethod
    def from_file(cls, file: str):
        inputs = [] 
        return cls(inputs)


if __name__ == "__main__":
    stem: str = Path(__file__).stem
    
    test_file = Path("examples") / ("test_" + stem + ".txt")
    test_something = Something.from_file(test_file)
    assert test_something.part1() == None
    assert test_something.part2() == None

    input_file = Path("inputs") / (stem + ".txt")
    something = Something.from_file(input_file)

    print(f"part1: {something.part1()}")
    print(f"part2: {something.part2()}")
