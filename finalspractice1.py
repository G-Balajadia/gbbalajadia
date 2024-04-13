#!/usr/bin/env python3
'''
Author: Glorifer Balajadia
'''

import sys


def fileop(filename):
    try:
        with open(filename, 'r') as file:
            return file.read()
    except FileNotFoundError:
        return ""


def process_data(inp: list) -> int:
    count = 0
    for x in inp:
        l = x.split()
        if l and l[0] == 'banana':
            count += 1
    return count


if __name__ == "__main__":
    try:
        if len(sys.argv) < 2:
            raise IndexError("Error: no arguments found")
        
        for arg in sys.argv[1:]:
            try:
                x = fileop(arg)
                if not x:
                    print(f"{arg}: 0 bananas!")
                    continue
                num_bananas = process_data(x.strip().split('\n'))
                print(f"{arg}: {num_bananas} bananas!")
            except FileNotFoundError:
                print(f"File '{arg}' not found.")
    except IndexError as e:
        print(e)
        sys.exit(1)