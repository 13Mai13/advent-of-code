"""
Utility functions for the Advent of Code 2025.
"""

def read_sequence(file_path: str) -> list[str]:
    """
    Read the sequence from the file.
    """
    with open(file_path, 'r') as file:
        return file.read().splitlines()