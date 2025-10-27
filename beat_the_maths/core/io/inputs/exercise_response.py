import time

def input_response(problem) -> str:
    start_time = time.time()
    response = input(problem).strip()
    duration = time.time() - start_time
    return response, duration