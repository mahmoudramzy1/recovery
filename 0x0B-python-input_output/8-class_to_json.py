#!/usr/bin/python3
"""Defines function that returns dictaionary discribtion"""


def class_to_json(obj):
    """Returns the dictionary description with simple data structure,
    (list, dictionary, string, integer and boolean) for JSON serialization,
    of an object.

    Args:
        obj (MyClass): object.

    Returns:
        dict: dictionary.
    """
    return obj.__dict__
