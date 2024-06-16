#!/usr/bin/python3
"""Define function that convert json string to python datastructure"""

import json


def from_json_string(my_str):
    """Converts from json string to python datastructure"""
    return json.loads(my_str)
