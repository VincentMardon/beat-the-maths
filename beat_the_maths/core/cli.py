import time

from .services.quiz_engine.problem_generator import problem_generator

from .io.inputs.parameters import input_params
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

    start_time = time.time()
    response = input(problem).strip()
    duration = time.time() - start_time

    print()  # Blank line for better readability

    if response.isdigit() and int(response) == solution:
        print_success_msg(duration)
    else:
        print_failure_msg(solution, duration)

    print()  # Blank line at the end for better readability

# Future improvements:
# - Implement a scoring system based on speed and accuracy.
# - Consider packaging the application for easier distribution (e.g., PyInstaller).
# - Add more types of problems (e.g., equations, fractions).
# - Implement a loop to allow multiple problems in one session.
# - Save high scores to a file or database.
# - Add sound effects for correct/wrong answers (optional).
# - Improve input validation (handle non-numeric inputs gracefully).
# - Add a help option to explain the game rules and controls.
# - Consider using a GUI library for a more interactive experience (optional).
# - Add unit tests for the problem generation logic.
# - Refactor code into classes if more features are added later.
# - Add localization support for different languages (optional).
# - Implement a leaderboard to track top scores (optional).
# - Add a timer countdown for each question to increase difficulty (optional).
# - Consider using a configuration file for settings (e.g., default difficulty).
# - Add animations or visual effects for a more engaging experience (optional).
# - Implement user profiles to track individual progress (optional).
# - Add a feature to review past problems and solutions (optional).