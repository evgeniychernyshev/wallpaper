from app.lib import calculate_rolls_count, calculate_canvas_in_roll, calculate_perimeter, calculate_canvas_count

roll_l = 10
roll_w = 1.06
room_l = 10
room_w = 10
ceiling_h = 2.75
perimeter = 0


def test_calculate_rolls_count_with_rest():
    expected = 13
    actual = calculate_rolls_count(roll_l, roll_w, room_l, room_w, ceiling_h)

    assert actual == expected


def test_calculate_rolls_count():
    expected = 20
    actual = calculate_rolls_count(10, 1, 15, 15, 3)

    assert actual == expected

def test_calculate_perimeter():
    expected = 40
    actual = calculate_perimeter(room_l, room_w)
    global perimeter
    perimeter = actual

    assert actual == expected


def test_calculate_canvas_count_with_rest():
    expected = 38
    actual = calculate_canvas_count(perimeter, roll_w)

    assert actual == expected


def test_calculate_canvas_count():
    expected = 40
    actual = calculate_canvas_count(40, 1)

    assert actual == expected


def test_calculate_canvas_in_roll():
    expected = 3
    actual = calculate_canvas_in_roll(roll_l, ceiling_h)

    assert actual == expected
