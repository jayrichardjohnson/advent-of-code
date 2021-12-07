from dataclasses import dataclass
from pathlib import Path
from typing import Counter, Dict, List, NamedTuple

import re
import numpy as np
from numpy.typing import NDArray
# import numpy as np

class Point(NamedTuple):
    x: int
    y: int

class Segment(NamedTuple):
    start: Point
    end: Point

@dataclass
class Map:
    segments: List[Segment] 
    grid: NDArray[np.int_]

    def part1(self) -> int:
         
        return (self.grid > 1).sum() 

    def part2(self) -> int:

        return (self.grid > 1).sum()
    
    def make_grid(self) -> NDArray[np.int_]:
        


        return
    
    @classmethod
    def from_file(cls, file: str):
        lines = file.read_text().splitlines() 
        segments: List[Segment] = []
        x_max, y_max = 0, 0
        for idx, line in enumerate(lines): 
            x1, y1, x2, y2 = [int(x) for x in re.split(',| -> ', line)]
            x_max, y_max = (max((x_max,x1, x2)), max((y_max, y1, y2)))
            segment = Segment(Point(x1, y1), Point(x2, y2))
            segments.append(segment)
         
        grid = np.zeros( (x_max + 1, y_max + 1), dtype=int)
        
        return cls(segments, x_max, y_max)


if __name__ == "__main__":
    stem: str = Path(__file__).stem
    
#    test_file = Path("examples") / ("test_" + stem + ".txt")
#    test_something = Something.from_file(test_file)
#    assert test_something.part1() == None
#    assert test_something.part2() == None

    input_file = Path("inputs") / (stem + ".txt")
    something = Map.from_file(input_file)

    print(f"part1: {something.part1()}")
    print(f"part2: {something.part2()}")
