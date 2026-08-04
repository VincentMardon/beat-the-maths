type RectTuple = tuple[int, int, int, int]


def centered_row(
    count: int,
    *,
    center_x: int,
    top: int,
    item_size: tuple[int, int],
    gap: int,
) -> list[RectTuple]:
    if count <= 0:
        return []

    width, height = item_size
    total_width = count * width + (count - 1) * gap
    left = center_x - total_width // 2

    return [
        (
            left + index * (width + gap),
            top,
            width,
            height,
        )
        for index in range(count)
    ]
