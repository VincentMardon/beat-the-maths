import time


def input_response(problem: str, exercise_number: int) -> tuple[str, float]:
    start_time = time.time()
    response = input(f"{exercise_number}. How much is {problem}").strip()
    duration = time.time() - start_time
    return response, duration
