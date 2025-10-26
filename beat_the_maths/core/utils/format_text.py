from ..styles.tokens import RESETS

# Function to format text with ANSI escape codes
def format_text(text: str, *codes: int) -> str:
    sgr = f"\033[{';'.join(map(str, codes))}m"
    eol = f"\033[{RESETS['all']}m"
    return f"{sgr}{text}{eol}"
