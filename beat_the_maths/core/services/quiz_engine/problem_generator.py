import random
import operator as op

from typing import Tuple

difficulty_levels = {
    1: 10,  # numbers between 1 and 10
    2: 100,  # numbers between 1 and 100
    3: 1000  # numbers between 1 and 1000 (etc.)
}

OPS = {
    1: (op.add, '+'),
    2: (op.sub, '-'),
    3: (op.mul, 'x'),
    4: (op.floordiv, '÷'),
}

def _rand_in_level(level: int) -> int:
    hi = difficulty_levels.get(level, 10)
    return random.randint(1, hi)

def problem_generator(difficulty_level: int = 1, exercise_type: int = 1) -> Tuple[str, int]:
    """
    Generate a simple math problem based on difficulty and type.
    :param difficulty: Difficulty level (1, 2, or 3)
    :param exercice_type: Type of exercise (1: addition, 2: subtraction, 3: multiplication, 4: division)
    :return: A tuple containing the problem as a string and the solution as an number.
    """
    
    a=_rand_in_level(difficulty_level)
    b=_rand_in_level(difficulty_level)

    func, sign = OPS.get(exercise_type, OPS[1])

    if func is op.sub and a < b:
        a, b = b, a  # Ensure no negative results for subtraction
    elif func is op.floordiv:
        while b == 0:
            b = _rand_in_level(difficulty_level)  # Avoid division by zero
        q = _rand_in_level(difficulty_level)
        a = b * q  # Ensure a is a multiple of b for clean division

    question = f"{a} {sign} {b} = ? "
    answer = func(a, b)

    return question, answer


# considering classing this into a ProblemGenerator class if more features are added later (eg. equations, fractions, scientist notation, etc).
if __name__ == "__main__":
    for (lvl, etype) in [(1,1),(2,2),(3,3),(2,4),(1,99)]:
        q, ans = problem_generator(lvl, etype)
        print(q, ans)
