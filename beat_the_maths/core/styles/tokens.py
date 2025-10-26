# colors and styles for terminal text formatting using ANSI escape codes

# foreground colors
FG = {
    'black': 30,
    'red': 31,
    'green': 32,
    'yellow': 33,
    'blue': 34,
    'magenta': 35,
    'cyan': 36,
    'white': 37,
    'default': 39,
}

# background colors
BG = {
    'black': 40,
    'red': 41,
    'green': 42,
    'yellow': 43,
    'blue': 44,
    'magenta': 45,
    'cyan': 46,
    'white': 47,
    'default': 49,
}

# text styles
STYLES = {
    'bold': 1,
    'dim': 2,
    'italic': 3,
    'underline': 4,
    'blink': 5,  # don't work in most terminals
    'reverse': 7,
    'hidden': 8,
    'strikethrough': 9,
}

# reset codes
RESETS = {
    'all': 0,
    'bold': 21,
    'dim': 22,
    'italic': 23,
    'underline': 24,
    'blink': 25,
    'reverse': 27,
    'hidden': 28,
    'strikethrough': 29,
}


if __name__ == "__main__":
    for color_name, code in FG.items():
        print(f"\033[{code}m{color_name}\033[0m", end=' ')

    print()  # New line between FG and BG

    for color_name, code in BG.items():
        print(f"\033[{code}m{color_name}\033[0m", end=' ')

    print()  # New line between BG and STYLES

    for style_name, code in STYLES.items():
        print(f"\033[{code}m{style_name}\033[0m", end=' ')