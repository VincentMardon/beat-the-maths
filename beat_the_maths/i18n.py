from enum import StrEnum, auto


class Language(StrEnum):
    FRENCH = "fr"
    ENGLISH = "en"


class Text(StrEnum):
    TITLE_SUBTITLE = auto()
    TITLE_PLAY = auto()
    TITLE_SETTINGS = auto()

    SETTINGS_TITLE = auto()
    SETTINGS_LANGUAGE = auto()
    SETTINGS_BACK = auto()

    CONFIGURATION_TITLE = auto()
    OPERATION_PROMPT = auto()
    DIFFICULTY_PROMPT = auto()
    OPERATION_ADDITION = auto()
    OPERATION_SUBTRACTION = auto()
    OPERATION_MULTIPLICATION = auto()
    OPERATION_DIVISION = auto()
    DIFFICULTY_EASY = auto()
    DIFFICULTY_MEDIUM = auto()
    DIFFICULTY_HARD = auto()
    CONFIGURATION_READY = auto()
    CONFIGURATION_INCOMPLETE = auto()
    START = auto()
    BACK_TO_TITLE = auto()

    QUIZ_PROGRESS = auto()
    ANSWER_PLACEHOLDER = auto()
    ANSWER_PROMPT = auto()
    ANSWER_CORRECT = auto()
    ANSWER_INCORRECT = auto()
    QUIT = auto()

    RESULTS_TITLE = auto()
    RESULTS_REPLAY = auto()
    RESULTS_BACK_TO_TITLE = auto()


type Catalog = dict[Text, str]

CATALOGS: dict[Language, Catalog] = {
    Language.FRENCH: {
        Text.TITLE_SUBTITLE: ("Le serious game qui soigne tes douleurs en maths."),
        Text.TITLE_PLAY: "Entrée : jouer",
        Text.TITLE_SETTINGS: "S : paramètres",
        Text.SETTINGS_TITLE: "PARAMÈTRES",
        Text.SETTINGS_LANGUAGE: "Choisis une langue",
        Text.SETTINGS_BACK: "Retour arrière : écran titre",
        Text.CONFIGURATION_TITLE: "CONFIGURE TA PARTIE",
        Text.OPERATION_PROMPT: "Choisis une opération",
        Text.DIFFICULTY_PROMPT: "Choisis une difficulté",
        Text.OPERATION_ADDITION: "Addition",
        Text.OPERATION_SUBTRACTION: "Soustraction",
        Text.OPERATION_MULTIPLICATION: "Multiplication",
        Text.OPERATION_DIVISION: "Division",
        Text.DIFFICULTY_EASY: "Facile",
        Text.DIFFICULTY_MEDIUM: "Moyenne",
        Text.DIFFICULTY_HARD: "Difficile",
        Text.CONFIGURATION_READY: "Configuration prête !",
        Text.CONFIGURATION_INCOMPLETE: ("Sélectionne une opération et une difficulté"),
        Text.START: "Commencer",
        Text.BACK_TO_TITLE: (
            "Retour arrière : revenir au titre    •    Échap : quitter"
        ),
        Text.QUIZ_PROGRESS: "Question {current} / {total}",
        Text.ANSWER_PLACEHOLDER: "Ta réponse",
        Text.ANSWER_PROMPT: "Écris ta réponse puis appuie sur Entrée",
        Text.ANSWER_CORRECT: "Correct ! {duration:.2f} s",
        Text.ANSWER_INCORRECT: ("Raté ! La réponse était {solution}."),
        Text.QUIT: "Échap : quitter",
        Text.RESULTS_TITLE: "PARTIE TERMINÉE",
        Text.RESULTS_REPLAY: "Entrée : rejouer",
        Text.RESULTS_BACK_TO_TITLE: (
            "Retour arrière : écran titre    •    Échap : quitter"
        ),
    },
    Language.ENGLISH: {
        Text.TITLE_SUBTITLE: ("The serious game to heal your maths pain."),
        Text.TITLE_PLAY: "Enter: play",
        Text.TITLE_SETTINGS: "S: settings",
        Text.SETTINGS_TITLE: "SETTINGS",
        Text.SETTINGS_LANGUAGE: "Choose a language",
        Text.SETTINGS_BACK: "Backspace: title screen",
        Text.CONFIGURATION_TITLE: "SET UP YOUR GAME",
        Text.OPERATION_PROMPT: "Choose an operation",
        Text.DIFFICULTY_PROMPT: "Choose a difficulty",
        Text.OPERATION_ADDITION: "Addition",
        Text.OPERATION_SUBTRACTION: "Subtraction",
        Text.OPERATION_MULTIPLICATION: "Multiplication",
        Text.OPERATION_DIVISION: "Division",
        Text.DIFFICULTY_EASY: "Easy",
        Text.DIFFICULTY_MEDIUM: "Medium",
        Text.DIFFICULTY_HARD: "Hard",
        Text.CONFIGURATION_READY: "Configuration ready!",
        Text.CONFIGURATION_INCOMPLETE: ("Select an operation and a difficulty"),
        Text.START: "Start",
        Text.BACK_TO_TITLE: ("Backspace: return to title    •    Esc: quit"),
        Text.QUIZ_PROGRESS: "Question {current} / {total}",
        Text.ANSWER_PLACEHOLDER: "Your answer",
        Text.ANSWER_PROMPT: "Enter your answer, then press Enter",
        Text.ANSWER_CORRECT: "Correct! {duration:.2f} s",
        Text.ANSWER_INCORRECT: ("Wrong! The answer was {solution}."),
        Text.QUIT: "Esc: quit",
        Text.RESULTS_TITLE: "QUIZ COMPLETE",
        Text.RESULTS_REPLAY: "Enter: play again",
        Text.RESULTS_BACK_TO_TITLE: ("Backspace: title screen    •    Esc: quit"),
    },
}


def translate(
    language: Language,
    text: Text,
    **values: object,
) -> str:
    return CATALOGS[language][text].format(**values)
