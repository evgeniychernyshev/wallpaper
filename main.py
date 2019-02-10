from lib import calculate_rolls_count

roll_length = float(input('Enter roll length (m): '))
roll_width = float(input('Enter roll width (m): '))
room_length = float(input('Enter room length (m): '))
room_width = float(input('Enter room width (m): '))
ceiling_height = float(input('Enter ceiling height (m): '))
rolls_count = calculate_rolls_count(roll_length, roll_width, room_length, room_width, ceiling_height)
print('You need', rolls_count, 'rolls. We recommend buy 1-2 rolls more.')
