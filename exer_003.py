# -*- coding: utf-8 -*-
"""
Exercise #3

Write a program that accepts a comma separated sequence of words as input
and prints the words in a comma-separated sequence after sorting them
alphabetically.

Suppose the following input is supplied to the program:
without,hello,bag,world

Then, the output should be:
bag,hello,without,world

Hint:
String join() method
"""


# your name and email address here
__author__ = 'xXLXx <leo@bywave.com.au>'


if __name__ == '__main__':
    while 1:
        try:
            x = input("Enter comma separated string: ")

            x = x.replace(" ", "")
            x = x.split(',')
            x = sorted(x)
            x = ','.join(x)

            print(x)
        except:
            print('Oops, something went wrong XD')
