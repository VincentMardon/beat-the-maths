from beat_the_maths.core.services.quiz_engine.answer_result import AnswerResult
from beat_the_maths.core.services.quiz_engine.problems.problem import Problem


def test_corect_answer_result():
    problem = Problem(question="2 + 3 = ? ", solution=5)

    result = AnswerResult(
        problem=problem,
        response="5",
        duration=1.25,
    )

    assert result.is_correct
    assert result.problem == problem
    assert result.response == "5"
    assert result.duration == 1.25


def test_incorrect_answer_result():
    problem = Problem(question="2 + 3 = ? ", solution=5)

    result = AnswerResult(
        problem=problem,
        response="4",
        duration=2.5,
    )

    assert not result.is_correct
