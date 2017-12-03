"""This script is for day 1 on Advent of Code 2017"""

import sys

def get_file_contents(file_loc):
    """Open file at location provided and return contents"""

    with open(file_loc, 'r') as file_to_read:
        return file_to_read.read()

def prep_input_list():
    """Read input from text file and convert to list of ints"""
    input_file_loc = "data/input1.txt"
    input_text = get_file_contents(input_file_loc)

    return list(map(int, input_text))

def puzzle_1():
    """Puzzle 1"""
    nums = prep_input_list()
    length = len(nums)

    total = 0
    for i in range(length - 1):
        if nums[i] == nums[i+1]:
            total += nums[i]

    if nums[-1] == nums[0]:
        total += nums[length - 1]

    return total

def puzzle_2():
    """Puzzle 2"""
    nums = prep_input_list()
    length = len(nums)

    total = 0
    for i in range(length):
        halfway = (i + length//2) % length
        if nums[i] == nums[halfway]:
            total += nums[i]

    return total

if __name__ == '__main__':
    print(puzzle_2())
