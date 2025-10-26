from ...utils.format_text import format_text
from ...styles.tokens import STYLES,FG

from ....data.texts.title import TITLE, INTRO

# Function to print formated title
def print_title() -> None:  
    styled_title = format_text(TITLE, STYLES['bold'], FG['cyan'])
    print(styled_title)
    print(INTRO)