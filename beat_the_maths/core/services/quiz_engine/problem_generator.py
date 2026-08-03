import operator as op
import random

from .problems.problem import Problem
from .quiz_config import Difficulty, Operation

OPS = {
    Operation.ADDITION: (op.add, "+"),
    Operation.SUBTRACTION: (op.sub, "-"),
    Operation.MULTIPLICATION: (op.mul, "x"),
    Operation.DIVISION: (op.floordiv, "÷"),
}


def _rand_in_difficulty(difficulty: Difficulty) -> int:
    return random.randint(1, difficulty.maximum_operand)


def problem_generator(
    difficulty: Difficulty = Difficulty.EASY, operation: Operation = Operation.ADDITION
) -> Problem:
    """
    Generate a simple math problem based on difficulty and operation.
    :return: The generated problem.
    """

    a = _rand_in_difficulty(difficulty)
    b = _rand_in_difficulty(difficulty)

    func, sign = OPS[operation]

    if operation is Operation.SUBTRACTION and a < b:
        a, b = b, a  # Ensure no negative results for subtraction
    elif operation is Operation.DIVISION:
        q = _rand_in_difficulty(difficulty)
        a = b * q  # Ensure a is a multiple of b for clean division

    question = f"{a} {sign} {b} = ? "
    solution = func(a, b)

    return Problem(question=question, solution=solution)
