#!/usr/bin/python3
"""Defining read file function"""


def read_file(filename=""):
    """Reads filename"""
    with open(filename, encoding='utf-8') as myfile:

        print(myfile.read(), end="")
