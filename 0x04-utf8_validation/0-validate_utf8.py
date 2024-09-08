#!/usr/bin/python3
"""A method that check utf-8 encoding"""

def validUTF8(data):
    """check if a set of data is a valid utf-8"""
    n_byte = 0
    for byte in data:
        if n_byte == 0:
            if byte & 0b11111000 == 0b11110000:
                n_byte = 3
            elif byte & 0b11110000 == 0b11100000:
                n_byte = 2
            elif byte & 0b11100000 == 0b11000000:
                n_byte = 1
            elif byte & 0b10000000 == 0:
                n_byte = 0
            else:
                return False
        else:
            if byte & 0b11000000 != 0b10000000:
                return False
            n_byte -= 1

    return n_byte == 0
