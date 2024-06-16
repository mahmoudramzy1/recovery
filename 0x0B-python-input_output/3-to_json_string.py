#!/usr/bin/python3
"""Defines fuction that serialize python data structure with json"""

import json


def to_json_string(my_obj):
    """serialize the data structure with json"""
    return json.dumps(my_obj)
