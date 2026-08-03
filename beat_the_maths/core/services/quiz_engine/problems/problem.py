from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class Problem:
    question: str
    solution: int

    def is_correct(self, response: str) -> bool:
        return response.isdigit() and int(response) == self.solution
