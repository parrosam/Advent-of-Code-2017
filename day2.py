"""Day 2 of Advent of Code 2017"""

import utils

def get_input():
    """Get input2.txt data as a list of list of int"""
    input_text = utils.get_day_input(2)
    text_line_list = input_text.splitlines()

    line_list = []
    for text_line in text_line_list:
        line = list(map(int, text_line.split('\t')))
        line_list.append(line)

    return line_list

def puzzle_1():
    """Puzzle 1 solution"""
    data = get_input()

    check_sum = 0
    for line in data:
        line_range = get_line_range(line)
        check_sum += line_range

    return check_sum

def get_line_range(line):
    """Returns the difference between the largest and smalles values in a line"""
    smallest = line[0]
    largest = line[0]
    for num in line:
        if num < smallest:
            smallest = num
        elif num > largest:
            largest = num

    return largest - smallest

if __name__ == '__main__':
    print(puzzle_1())
