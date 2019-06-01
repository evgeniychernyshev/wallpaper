# calculating total count of wallpaper rolls
def calculate_rolls_count(roll_l, roll_w, room_l, room_w, ceiling_h):
    room_perimeter = calculate_perimeter(room_l, room_w)
    canvas_count = calculate_canvas_count(room_perimeter, roll_w)
    canvas_in_roll = calculate_canvas_in_roll(roll_l, ceiling_h)
    rolls_count_total = canvas_count / canvas_in_roll
    rest = canvas_count % canvas_in_roll
    if rest > 0:
        return int(canvas_count // canvas_in_roll + 1)

    return int(rolls_count_total)


def calculate_perimeter(room_l, room_w):
    return (room_l + room_w) * 2


# calculating total count of wallpaper canvases for room
def calculate_canvas_count(perimeter, roll_w):
    count = perimeter / roll_w
    rest = perimeter % roll_w
    if rest > 0:
        return int(perimeter // roll_w + 1)  # round canvases count

    return int(count)


# calculating count of canvases in 1 roll
def calculate_canvas_in_roll(roll_l, ceiling_h):
    fund = 0.1  # adding 10cm to ceiling height as reserve
    return int(roll_l // (ceiling_h + fund))

