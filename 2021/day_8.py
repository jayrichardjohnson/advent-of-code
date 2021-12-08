#!/usr/bin/env python3 
from dataclasses import dataclass
from pathlib import Path
from typing import Counter, Dict, List, NamedTuple

## algorithm
# 
# 1. find 2 letter digit -> 1, 'cf'
# 2. find 3 letter digit -> 7, 'acf'
# 3. find 4 letter digit -> 4, 'bcdf'
# 4. find 7 letter digit -> 8, 'abcdefg'
# 5.  a. find 6 letter digits: (0, 6, 9)
#     b. compare each with letters of 1
#     c. contains both letters of 1? -> (0,9)
#     d. only contains 1 letter of 1? -> 6
# 6.  a. find 5 letter digits: (2, 3, 5)
#     b. compare with letters of 6
#     c. if all 5 letters are a subset of the letters of 6 -> 5
#     d. the letter that is in 6 but not in 5 -> 'e'
# 7.  Find remaining 5 letter digits (2,3)
#     a. if it has 'e' -> 2
#     b. if it does not have 'e' -> 3
# 8. Find remaining 6 letter digits: (0,9)
#     a. if it has 'e' -> 0
#     b. if it does not have 'e' -> 9
    

class Signal(NamedTuple):
    inputs: List[str]
    outputs: List[str]

class Digit:
    n_segments: int


class Map:
    base_map = {'abcefg' : 0, 
                'cf'     : 1, 
                'acdeg'  : 2, 
                'acdfg'  : 3, 
                'bcdf'   : 4, 
                'abdfg'  : 5, 
                'abdefg' : 6,
                'acf'    : 7, 
                'abcdefg': 8,
                'abcdfg' : 9}

    
@dataclass
class DigitDeduction:
    lines: List[Signal] 

    def part1(self) -> int:
        known_digits = 0 
        for line in self.lines:
            segment_length = [len(x) for x in line.outputs]
            known_digits += segment_length.count(2) # signal 1 uses 2 segments 
            known_digits += segment_length.count(3) # signal 7 uses 3 segments
            known_digits += segment_length.count(4) # signal 4 uses 4 segments
            known_digits += segment_length.count(7) # signal 8 uses 7 segments
        return known_digits 

    def part2(self) -> int:
        output_values = []
        for line in self.lines:
            lettermap = [None] * 10                
            charmap = [None] * 10
            for idx, input in enumerate(line.inputs):
                if len(input) == 2:
                    lettermap[idx] = 1
                    charmap[1] = input
                elif len(input) == 3:
                    lettermap[idx] = 7
                    charmap[7] = input
                elif len(input) == 4:
                    lettermap[idx] = 4
                    charmap[4] = input
                elif len(input) == 7:
                    lettermap[idx] = 8
                    charmap[8] = input
            # find number 6
            for idx, input in enumerate(line.inputs):
                if len(input) == 6 and not all([letter in list(input) for letter in list(charmap[1])]):
                    lettermap[idx] = 6
                    charmap[6] = input
            
            # find number 5 and letter e
            for idx, input in enumerate(line.inputs):
                if len(input) == 5 and all([letter in list(charmap[6]) for letter in list(input)]):
                    lettermap[idx] = 5
                    charmap[5] = input
                    _e = charmap[6]
                    for letter in list(input):
                        _e = _e.replace(letter, "")
                    assert(len(_e) == 1)
    
            for idx, input in enumerate(line.inputs):
                if len(input) == 5 and input not in charmap:
                    if _e in input:
                        lettermap[idx] = 2
                        charmap[2] = input
                    else:
                        lettermap[idx] = 3
                        charmap[3] = input
                elif len(input) == 6 and input not in charmap:
                    if _e in input:
                        lettermap[idx] = 0
                        charmap[0] = input
                    else:
                        lettermap[idx] = 9
                        charmap[9] = input
            assert(all([ x is not None for x in lettermap]))
            assert(all([ x is not None for x in charmap]))
            
    
            entry_value = []
            for digit in line.outputs:
                for idx, signal_pattern in enumerate(charmap):
                    if len(digit) == len(signal_pattern) and sorted(digit) == sorted(signal_pattern): 
                        entry_value.append(str(idx))
                        break
            output_values.append(int("".join(entry_value))) 
         
        return sum(output_values)

    @classmethod
    def from_file(cls, file: str):
        lines: List[str] = file.read_text().splitlines()
        inputs = []
        for line in lines:
            ins, outs = line.split(' | ')
            inputs.append(Signal( ins.split(), outs.split() ))
        
        return cls(inputs)


if __name__ == "__main__":
    stem: str = Path(__file__).stem
    
    test_file = Path("examples") / ("test_" + stem + ".txt")
    test_something = DigitDeduction.from_file(test_file)
    assert test_something.part1() == 26
    assert test_something.part2() == 61229

    input_file = Path("inputs") / (stem + ".txt")
    something = DigitDeduction.from_file(input_file)

    print(f"part1: {something.part1()}")
    print(f"part2: {something.part2()}")
