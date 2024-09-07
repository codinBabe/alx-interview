#!/usr/bin/env python3
"""A method that check utf-8 encoding"""

def validUTF8(data):
    """check if a set of data is a valid utf-8"""
    for i in range(len(data)):
        num = data[i]
        if chr(num):
            return True
        else:
            return False