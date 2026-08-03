import pytest

from beat_the_maths.core.services.quiz_engine.problems.problem import Problem


@pytest.mark.parametrize("response", ["5", "05"])
def test_accepts_correct_answer(response):
    problem = Problem(question="2 + 3 = ? ", solution=5)

    assert problem.is_correct(response)


@pytest.mark.parametrize("response", ["4", "-5", "+5", "five", ""])
def test_rejects_incorrect_or_invalid_answer(response):
    problem = Problem(question="2 + 3 = ? ", solution=5)

    assert not problem.is_correct(response)
