"""Day 3 of Advent of Code 2017"""

import math
import utils

def get_input():
    """Read input number and convert to int"""
    file_text = utils.get_day_input(3)
    return int(file_text)

def puzzle_1(num):
    """Puzzle 1 solution"""
    nearest_smaller_sqroot = int(math.sqrt(num - 1))
    square_area = math.pow(nearest_smaller_sqroot,2)

    is_even = nearest_smaller_sqroot % 2 == 0
    min_dist = (nearest_smaller_sqroot // 2) + (1 if not is_even else 0)
    max_dist = nearest_smaller_sqroot + (1 if not is_even else 0)

    start = max_dist - (1 if not is_even else 0)

    # I don't like this approach but I got tired of trying to fix
    # one off errors and edge cases...
    distances = [x for x in range(start, min_dist, -1)] + [x for x in range(min_dist, max_dist)] + [x for x in range(max_dist, min_dist, -1)] + [x for x in range(min_dist, start + 1)]

    extra_squares = num - square_area
    return distances[int(extra_squares - 1)]


if __name__ == '__main__':
    print(puzzle_1(get_input()))
