from ....data.texts.title import INTRO, TITLE
from ...styles.tokens import FG, STYLES
from ...utils.format_text import format_text


# Function to print formated title
def print_title() -> None:
    styled_title = format_text(TITLE, STYLES["bold"], FG["cyan"])
    print(styled_title)
    print(INTRO)
