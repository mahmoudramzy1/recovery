#!/usr/bin/python3
"""Defines function that appent text on file"""


def append_write(filename="", text=""):
    """append the file with text"""
    with open(filename, 'a', encoding='utf-8') as f:
        return f.write(text)
