#!/usr/bin/env python3 
from dataclasses import dataclass
from pathlib import Path
from typing import Counter, Dict, List, NamedTuple
import timeit
from ipdb import set_trace as db

@dataclass
class Brackets(List):
    opened : List[str]
    first_illegal : str = None

    def checkchar(self, character: str):
        corrupt = False
        if self.isopenchar(character):
            self.opened.append(character)
        elif self.isclosedchar(character):
            if self.getmatching(character) is self.opened[-1]:
                self.opened = self.opened[:-1]
            else:
                self.first_illegal = character
                corrupt = True
        return corrupt

    def isopenchar(self, character):
        return character in "([{<"
    
    def isclosedchar(self, character):
        return character in ")]}>"
    
    def getmatching(self, character):
        matching_chars = {'(' : ')', 
                          '{' : '}', 
                          '[' : ']', 
                          '<' : '>', 
                          '>' : '<', 
                          ']' : '[',
                          '}' : '{',
                          ')' : '('}
        return matching_chars[character]

    def incomplete_score(self) -> int:
        errors = {')' : 1, ']' : 2, '}' : 3, '>' : 4}
        char_points = []        
#        for character in reversed(self.opened):
#            closing_char = self.getmatching(character)
#           char_points.append(errors[closing_char])
        char_points = [errors[self.getmatching(character)] for character in reversed(self.opened)]  
        total_score = 0 
        for value in char_points:
            total_score = total_score * 5 + value
        
        return total_score

    @staticmethod
    def errorscore(last_illegals):
        errors = {'>' : 25137, 
                  '}' : 1197, 
                  ']' : 57, 
                  ')' : 3}
        return sum( [errors[ character ] for character in last_illegals] )

@dataclass
class SyntaxScore:
    chunks : List[int] 
    
    def part1(self) -> int:
        last_illegals = [] 
        for line in self.chunks:
            checker = Brackets([])
            for character in line:
                corrupt = checker.checkchar(character)                        
                if corrupt: 
                    last_illegals.append(character)
                    break
        return checker.errorscore(last_illegals)

    def part2(self) -> int:
        incomplete_scores = []
        for line in self.chunks:
            checker = Brackets([])
            for character in line:
                corrupt = checker.checkchar(character)
                if corrupt:
                    break
            if not corrupt:
                incomplete_scores.append(checker.incomplete_score())
        incomplete_scores.sort()
        middle_idx = int( ( len(incomplete_scores)-1) / 2)
        return incomplete_scores[middle_idx]

    @classmethod
    def from_file(cls, file: str):
        inputs = Path(file).read_text().split()
        return cls(inputs)


if __name__ == "__main__":
    time_start = timeit.default_timer() 
    stem: str = Path(__file__).stem
    
    print(f"Advent of Code: {stem}") 
    test_file = Path("examples") / ("test_" + stem + ".txt")
    test_something = SyntaxScore.from_file(test_file)
    assert test_something.part1() == 26397 
    assert test_something.part2() == 288957 

    input_file = Path("inputs") / (stem + ".txt")
    something = SyntaxScore.from_file(input_file)
    print(f"    part1: {something.part1()}")
    print(f"    part2: {something.part2()}")
    
    print("    Execution time: %.3f s" % (timeit.default_timer() - time_start))
