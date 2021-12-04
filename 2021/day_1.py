#!/usr/bin/env python3 

from pathlib import Path
from typing import List
import numpy as np

def part1(depths): 
    # read in the data and convert to a numpy array
    return count_increase(depths)


def part2(depths, smooth_factor=3):
    z_smooth = np.convolve(depths, np.ones(smooth_factor), mode='valid')
    return count_increase(z_smooth)


def count_increase(z):
    # define counting function
    # count_increase = lambda z : (np.diff(z) > 0).sum()
    return (np.diff(z) > 0).sum()


if __name__ == "__main__":
    stem: str = Path(__file__).stem
    input_file = Path("data") / (stem + ".txt")
    input: List[str] = input_file.read_text().splitlines()
    depths = np.asarray(input, dtype=int)
    print(part1(depths), part2(depths))
