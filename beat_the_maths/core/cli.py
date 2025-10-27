from .services.quiz_engine.problem_generator import problem_generator

from .io.inputs.parameters import input_params
from .io.inputs.exercise_response import input_response
from .io.outputs.title import print_title
from .io.outputs.game import print_success_msg, print_failure_msg

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
    etype, level = input_params()

    print()  # Blank line for better readability

    problem, solution = problem_generator(difficulty_level=level, exercise_type=etype)

    response, duration = input_response(problem)

    print()  # Blank line for better readability

    if response.isdigit() and int(response) == solution:
        print_success_msg(duration)
    else:
        print_failure_msg(solution, duration)

    print()  # Blank line at the end for better readability
