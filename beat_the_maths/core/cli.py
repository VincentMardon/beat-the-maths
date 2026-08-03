import time

from .io.inputs.exercise_response import input_response
from .io.inputs.parameters import input_params
from .io.outputs.game import print_failure_msg, print_success_msg
from .io.outputs.title import print_title
from .services.quiz_engine.quiz_engine import QuizEngine

# colorama is optional, but helps with Windows terminal compatibility.
# Considering moves this import inside a setup.py file or a main guard.
# See "Raccourcis claviers émoticones" ChatGPT conversation for more details.
try:
    from colorama import just_fix_windows_console

    just_fix_windows_console()
except ImportError:
    print("colorama not installed, proceeding without it.")
    pass


def main():
    print_title()

    # Get user preferences for difficulty level and exercise type
    config = input_params()
    engine = QuizEngine(config=config)

    print()  # Blank line for better readability

    while not engine.session.is_complete:
        problem = engine.next_problem()

        response, duration = input_response(
            problem.question,
            engine.session.next_question_number,
        )

        result = engine.submit_answer(
            response=response,
            duration=duration,
        )

        if result.is_correct:
            print_success_msg(result.duration)
            print()  # Blank line for better readability
        else:
            print_failure_msg(result.problem.solution, result.duration)
            print()  # Blank line for better readability

    print(f"You finish the game with {engine.session.score} points.")

    time.sleep(2)

    print("Thank you so much for playing my game!")

    time.sleep(5)
