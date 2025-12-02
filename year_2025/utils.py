"""
Utility functions for the Advent of Code 2025.
"""

def read_sequence(file_path: str, delimiter: None | str = None) -> list[str]:
    """
    Read the sequence from the file.
    """
    with open(file_path, 'r') as file:
        if delimiter is None:
            return file.read().splitlines()
        else:
            return file.read().split(delimiter)