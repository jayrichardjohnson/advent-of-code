#!/usr/bin/env python3 

from pathlib import Path
from typing import List
import numpy as np
from scipy import stats

def part1(X): 

    X_mode = stats.mode(X)
    gamma = X_mode[0][0]
    epsilon = 1 - gamma
    power = to_binary(gamma) * to_binary(epsilon)
    return power


def part2(X):


    return 'not done'



def to_binary(x):
    # take vector of binary digits and convert to real number (decimal)
    return np.dot(x, np.flip(2**np.arange(x.size), 0))



if __name__ == "__main__":
    stem: str = Path(__file__).stem
    input_file = Path("data") / (stem + ".txt")
    input: List[str] = input_file.read_text().splitlines()

    # convert list of binary strings to NxM numpy array 
    # rows are binary numbers
    # columns are the digits to each binary position
    # get maximum binary number length 
    len_max = 0
    for line in input:
        len_max = max(len_max, len(line))

    n_steps = len(input)
    X = np.zeros([n_steps, len_max], dtype=int)
    for ind_row in np.arange(n_steps):
        line = input[ind_row]
        for ind_col in np.arange(len(line)):
            if line[ind_col] == '1':
                X[ind_row, ind_col] = 1
        

    print(part1(X), part2(X))
