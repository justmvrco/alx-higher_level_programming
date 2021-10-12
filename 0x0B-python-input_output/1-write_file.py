#!/usr/bin/python3
"""
    1-write_file: write_file()
"""


def write_file(filename="", text=""):
    """
        write_file writes a string to a text file.
        Args:
            filename (str): name of file.
            text (str): text to be written.
        Returns: number of bytes written.
    """
    with open(filename, "w", encoding='utf-8') as a_file:
        return a_file.write(text)
