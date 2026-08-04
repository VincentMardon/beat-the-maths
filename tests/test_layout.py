import pytest

from beat_the_maths.ui.layout import centered_row


@pytest.mark.parametrize(
    ("count", "top", "gap", "expected"),
    [
        (0, 220, 20, []),
        (1, 220, 20, [(520, 220, 240, 64)]),
        (
            3,
            420,
            30,
            [
                (250, 420, 240, 64),
                (520, 420, 240, 64),
                (790, 420, 240, 64),
            ],
        ),
        (
            4,
            220,
            20,
            [
                (130, 220, 240, 64),
                (390, 220, 240, 64),
                (650, 220, 240, 64),
                (910, 220, 240, 64),
            ],
        ),
    ],
)
def test_centers_button_row(count, top, gap, expected):
    assert (
        centered_row(
            count,
            center_x=640,
            top=top,
            item_size=(240, 64),
            gap=gap,
        )
        == expected
    )
