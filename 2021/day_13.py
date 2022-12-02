#!/usr/bin/env python3 
from dataclasses import dataclass, replace
from pathlib import Path
from typing import Counter, Dict, List, NamedTuple

import numpy as np
from numpy.typing import NDArray
from ipdb import set_trace as db
import re
import timeit

class Point(Dict):
    {'x' : int, 'y' : int}

    def get_point(self):
        return self['x'], self['y']

class Fold(NamedTuple):
    axis : str 
    coord : int 


@dataclass
class Something:
    grid : List
    folds : List

    def part1(self) -> int:
        
        fold = self.folds[0] # only the first fold
        coord = fold.coord

        for idx, point in enumerate(self.grid):
            point_val = point[fold.axis]
            if point_val > fold.coord:
                new_value = point_val - 2*(point_val - coord)
                self.grid[idx][fold.axis] = new_value
        
        points = np.zeros((len( self.grid ), 2))
        for idx, point in enumerate(self.grid):
            points[idx] = self.grid[idx].get_point()

        return np.unique(points, axis=0).shape[0]

    def part2(self) -> int:
        return None

    @classmethod
    def from_file(cls, file: str):
        inputs = Path(file).read_text().split('\n')
        grid : List[Point] = []
        folds : List[Folds] = []

        for line in inputs:
            if 'fold' in line: 
                linesplit = line.split('=')
                folds.append(Fold( linesplit[0][-1], int(linesplit[1][0]) ) )
            elif bool(re.search('(\d*),(\d*)', line)):
                x,y = line.split(',')
                grid.append(Point({'x' : int(x), 'y' : int(y)}))
        return cls(grid, folds)


if __name__ == "__main__":
    time_start = timeit.default_timer() 
    
    stem: str = Path(__file__).stem
    
    print(f"Advent of Code: {stem}") 
    test_file = Path("examples") / ("test_" + stem + ".txt")
    test_something = Something.from_file(test_file)
    assert test_something.part1() == 17
    assert test_something.part2() == None

    input_file = Path("inputs") / (stem + ".txt")
    something = Something.from_file(input_file)
    print(f"    part1: {something.part1()}")
    print(f"    part2: {something.part2()}")
    
    print("    Execution time: %.3f s" % (timeit.default_timer() - time_start))
