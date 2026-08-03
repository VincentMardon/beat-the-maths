import time

from .io.inputs.exercise_response import input_response
from .io.inputs.parameters import input_params
from .io.outputs.game import print_failure_msg, print_success_msg
from .io.outputs.title import print_title
from .services.quiz_engine.game_session import GameSession
from .services.quiz_engine.problem_generator import problem_generator

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
    session = GameSession(config=config)

    print()  # Blank line for better readability

    while not session.is_complete:
        problem = problem_generator(
            difficulty=session.config.difficulty,
            operation=session.config.operation,
        )

        response, duration = input_response(
            problem.question,
            session.next_question_number,
        )

        result = session.record_answer(
            problem=problem,
            response=response,
            duration=duration,
        )

        if result.is_correct:
            print_success_msg(result.duration)
            print()  # Blank line for better readability
        else:
            print_failure_msg(result.problem.solution, result.duration)
            print()  # Blank line for better readability

    print(f"You finish the game with {session.score} points.")

    time.sleep(2)

    print("Thank you so much for playing my game!")

    time.sleep(5)
