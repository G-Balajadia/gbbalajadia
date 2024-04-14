#!/usr/bin/env python3

import sys

def read_file(filename: str) -> list:
    try:
        content = open(file_name, 'r')
        list_content = content.readlines()
        content.close()
        return list_content
    except:
        return ['File not found!']

if __name__ == '__main__':
    
    if len(sys.argv) < 2:
        print('Error: no file specified.')
        exit()
    
    file_name = sys.argv[1]

    output = read_file(file_name)
    count = 0
    
    for line in output:
        print(line)
        count = count + 1
    
    print('Number of lines: ' + str(count))