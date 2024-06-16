#!/usr/bin/python3
"""Defines write file function"""


def write_file(filename="", text=""):
    """Write in the file"""
    with open(filename, 'w', encoding='utf-8') as fi:
        return fi.write(text)
