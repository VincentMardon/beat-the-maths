from typing import Tuple

from ..outputs.game import print_invalid_input_msg

from ....data.texts.parameters import DIFFICULTY_LEVEL, EXERCISE_TYPE

# Function to get user input for difficulty level and exercise type
def input_params() -> Tuple[int, int]:
    while True:
        etype_list = [1, 2, 3, 4]
        try:
            etype = int(input(EXERCISE_TYPE).strip())
            if etype in etype_list:
                break
            else:
                raise ValueError
        except ValueError:
            print_invalid_input_msg(max=len(etype_list))
        
    while True:
        level_list = [1, 2, 3]
        try:
            level = int(input(DIFFICULTY_LEVEL).strip())
            if level in level_list:
                break
            else:
                raise ValueError
        except ValueError:
            print_invalid_input_msg(max=len(level_list))

    return etype, level
