#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This programm checks if the lines are properly nested or not.
"""
__author__ = "Ybrayym A and Piero M"

# PIERO helped out at the end!!!

import sys


brackets = {
    ')': '(',
    ']': '[',
    '}': '{',
    '>': '<',
    '*)': '(*'
}


def is_nested(line):
    """is_nested function checks weather properly nested or not"""
    stack = []
    count = 0
    while line:
        token = line[0]
        if line.startswith("(*"):
            token = '(*'
        if line.startswith('*)'):
            token = '*)'
        count += 1
        if token in brackets.values():
            # this is an opening bracket
            stack.append(token)
        elif token in brackets.keys():
            # this is a closing bracket
            expected_opener = brackets[token]
            actual_opener = stack.pop()
            if expected_opener != actual_opener:
                return "NO " + str(count)
        line = line[len(token):]

    # over with loop

    if stack: # checks if stack is not empty
        return 'NO ' + str(count)
    else:
        return 'YES'

    # BAD CODE MAANNN!!!!
    # count = 1
    # isClosing = False
    # for idx, char in enumerate(line):
    #     if isClosing:
    #         isClosing = False
    #         continue
    #     if len(validator) and char == '*' and validator[-1] == '(':
    #         validator[-1] = '(*'
    #         count -= 1
    #     elif char in checks.values():
    #         validator.append(char)
    #     if len(validator) and char == '*' and line[idx+1] == ')':
    #         validator.pop()
    #         isClosing = True
    #     elif char in checks.keys():
    #         if len(validator) and checks[char] == validator[-1]:
    #             validator.pop()
    #         elif not len(validator) and idx + 1 == len(line):
    #             return 'YES'
    #         else:
    #             print(validator)
    #             return 'NO ' + str(count)
    #     count += 1
    # print(validator)
    # if validator == []:
    #     return 'YES'
    # return 'NO ' + str(len(line))


def main(args):
    """Open the input file and call `is_nested()` for each line"""
    # Results: print to console and also write to output file
    with open('input.txt', 'r') as f:
        with open('output.txt', 'w') as f_out:
            for line in f:
                result = is_nested(line)
                f_out.write(result+'\n')


if __name__ == '__main__':
    main(sys.argv[1:])
