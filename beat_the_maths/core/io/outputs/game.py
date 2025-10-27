from typing import Optional

from ...utils.format_text import format_text
from ...styles.tokens import STYLES, FG

# Function to print an invalid input message
def print_invalid_input_msg(max: Optional[int] = None):
    additional_msg = f" (1-{max})" if max is not None else ""
    msg=format_text(f"Invalid input. Please enter a valid number{additional_msg}.", STYLES['bold'], FG['red'])
    print(msg)

# Function to print results of exercise
def print_success_msg(duration: float):
    print(format_text(f"✅ Correct! You beat the maths in {duration:.2f}s!", STYLES['bold'], FG['green']))

def print_failure_msg(solution: int, duration: float):
    print(format_text(f"❌ Wrong! The correct answer was {solution}. You took {duration:.2f}s.", STYLES['bold'], FG['red']))
