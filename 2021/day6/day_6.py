from dataclasses import dataclass
from pathlib import Path
from typing import Counter, Dict, List, NamedTuple

@dataclass
class FishSimulator:
    initial_timers: List[int] 
    timer_counts: List[int]
    age: int = 0

    @property
    def n_fish(self):
        return sum(self.timer_counts)

    def age_days(self, days: int, reset_index: int = 6):
        timer_counts = self.timer_counts
        # reset if you want a time in the past
        if self.age > days:
            self.age = 0
            timer_counts = self.count_ages(self.initial_timers)

        while self.age < days:
            spawned = timer_counts[0]
            timer_counts.append(timer_counts.pop(0))
            timer_counts[reset_index] += spawned 
            self.age += 1
        self.timer_counts = timer_counts

    @classmethod
    def from_file(cls, file: str, max_age: int = 9):
        line = Path(file).read_text().strip()
        ages = [int(x) for x in line.split(",")]
        cohort = cls.count_ages(ages, max_age) 
        return cls(ages, cohort)
    
    @classmethod
    def count_ages(cls, ages: List[int], max_age: int = 9):
        return [ages.count(x) for x in range(max_age)]


if __name__ == "__main__":
    simulator = FishSimulator.from_file("example.txt")
    simulator.age_days(18)
    assert simulator.n_fish == 26

    simulator.age_days(256)
    assert simulator.n_fish == 26984457539

    simulator.age_days(80)
    assert simulator.n_fish == 5934

    simulator = FishSimulator.from_file("input.txt")

    simulator.age_days(80)
    print(f"part1: {simulator.n_fish}")  # 391888

    simulator.age_days(256)
    print(f"part2: {simulator.n_fish}")  # 1754597645339
