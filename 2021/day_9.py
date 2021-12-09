from dataclasses import dataclass
from pathlib import Path
from typing import List

import timeit
import numpy as np
from scipy import ndimage

@dataclass
class LavaTubes:
    grid : List[int] 
    
    def part1(self) -> int:
        # create new grid with inf on the boundaries (self.grid.shape + 2)
        grid = np.ones((np.shape(self.grid)[0] + 2, np.shape(self.grid)[1] + 2), dtype=int) * (np.max(self.grid) + 1)
        grid[1:-1,1:-1] = self.grid
        lava_tubes = ((grid < np.roll(grid, 1,0)) & 
                (grid < np.roll(grid, -1, 0)) &
                (grid < np.roll(grid, 1, 1)) &
                (grid < np.roll(grid, -1, 1)) )

        risk_level = (grid[lava_tubes] + 1).sum() 
        return risk_level

    def part2(self) -> int:
        # label 9s as 0 and everything less than 9 as 1
        basins = (np.array(self.grid) < 9).astype(int)
        # find connected features, label defaults to finding connected 
        # areas less at N,S,E,W and automatically excludes diagonals, which is what we want
        labeled_basins, n_basins = ndimage.label(basins)
        # sum the number of points for each label
        basin_sizes = [ ( labeled_basins == x ).sum() for x in range(1, n_basins + 1)] 
        # return the producted of the three largest values 
        return (np.sort(basin_sizes)[-3:]).prod() 

    @classmethod
    def from_file(cls, file: str):
        grid = []
        with open(file) as f:
            for line in f:
                line = list(line.split()[0])
                grid.append([int(idx) for idx in line])
        return cls(grid)



if __name__ == "__main__":
    time_start = timeit.default_timer() 
    stem: str = Path(__file__).stem
    print(f"Advent of Code: {stem}") 
    test_file = Path("examples") / ("test_" + stem + ".txt")
    test_risklevel = LavaTubes.from_file(test_file)
    assert test_risklevel.part1() == 15
    assert test_risklevel.part2() == 1134

    input_file = Path("inputs") / (stem + ".txt")
    risklevel = LavaTubes.from_file(input_file)
    print(f"    part1: {risklevel.part1()}")
    print(f"    part2: {risklevel.part2()}")
    time_end = timeit.default_timer() 
    print("    Execution time: %.3f s" % (time_end - time_start))
