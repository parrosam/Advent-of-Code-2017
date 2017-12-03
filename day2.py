"""Day 2 of Advent of Code 2017"""

import itertools
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

def puzzle_1(data):
    """Puzzle 1 solution"""
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

def puzzle_2(data):
    """Puzzle 2 solution"""
    total = 0
    for line in data:
        total += find_clean_division(line)

    return total

def find_clean_division(line):
    """Find tuple that has clean division"""
    combinations = itertools.combinations(line, 2)
    pairs = [combination for combination in combinations
             if combination[0] % combination[1] == 0
             or combination[1] % combination[0] == 0]

    pair = pairs[0]
    if pair[0] > pair[1]:
        return pair[0] // pair[1]
    else:
        return pair[1] // pair[0]

if __name__ == '__main__':
    DAY_2_INPUT = get_input()
    print(puzzle_1(DAY_2_INPUT))
    print(puzzle_2(DAY_2_INPUT))
