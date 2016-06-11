#!/usr/bin/env python3


''' right.py -- displays a right justified string '''


# main function to use
def right_justify(what_to_do):
    length = 70
    num_spaces = length - len(str(what_to_do))
    output_string = ' ' * num_spaces + str(what_to_do)
    return output_string


# test the output
out = right_justify('test')
print(out)

