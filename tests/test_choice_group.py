from unittest.mock import Mock

from beat_the_maths.ui.components.button import Button
from beat_the_maths.ui.components.choice_group import ChoiceGroup


def create_button(*, clicked: bool = False) -> Mock:
    button = Mock(spec=Button)
    button.handle_event.return_value = clicked
    return button


def test_selects_clicked_button():
    event = object()
    addition_button = create_button()
    subtraction_button = create_button(clicked=True)

    group = ChoiceGroup(
        {
            "addition": addition_button,
            "subtraction": subtraction_button,
        }
    )

    assert group.handle_event(event) is True
    assert group.selected == "subtraction"


def test_second_click_replaces_previous_selection():
    event = object()
    addition_button = create_button(clicked=True)
    subtraction_button = create_button()

    group = ChoiceGroup(
        {"addition": addition_button, "subtraction": subtraction_button}
    )

    group.handle_event(event)

    addition_button.handle_event.return_value = False
    subtraction_button.handle_event.return_value = True

    group.handle_event(event)

    assert group.selected == "subtraction"


def test_ignored_event_keeps_current_selection():
    event = object()
    addition_button = create_button(clicked=True)
    subtraction_button = create_button()

    group = ChoiceGroup(
        {
            "addition": addition_button,
            "subtraction": subtraction_button,
        }
    )

    group.handle_event(event)

    addition_button.handle_event.return_value = False

    assert group.handle_event(event) is False
    assert group.selected == "addition"


def test_draw_marks_only_selected_button():
    surface = object()
    addition_button = create_button()
    subtraction_button = create_button()

    group = ChoiceGroup(
        {
            "addition": addition_button,
            "subtraction": subtraction_button,
        }
    )
    group.selected = "subtraction"

    group.draw(surface)

    addition_button.draw.assert_called_once_with(
        surface,
        selected=False,
    )
    subtraction_button.draw.assert_called_once_with(
        surface,
        selected=True,
    )
