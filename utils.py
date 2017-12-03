"""Utility functions and code for use"""

def get_file_contents(file_loc):
    """Open file at location provided and return contents"""

    with open(file_loc, 'r') as file_to_read:
        return file_to_read.read()

def get_day_input(day):
    """Open input for day assuming format of input{day}.txt"""
    file_name = "data/input{0}.txt".format(day)
    return get_file_contents(file_name)
