#!/usr/bin/env python3

'''
Author: Glorifer Balajadia

'''
import sys

def fileop(file) -> str:
    try:
        f = open(file, 'r')
        x = f.read()
        f.close()
        return x
    except:
        return ''

def process_data(list) -> int:
    x = 0
    for item in list:
        if item == 'banana':
            x += 1
    return x

if __name__ == '__main__':
    #file='test.txt'
    #print(fileop(file))
    #list_of_lines = fileop(file).split('\n')
    #print(list_of_lines)
    #print(process_data(list_of_lines))
    
    if len(sys.argv) < 2:
        print('Error: no arguments found')
        exit()
    
    for file in sys.argv[1:]:                   #lookup file start from second argument to last argumeent
        file2list = fileop(file).split('\n')    #call function fileop() to get a list from file
        count = process_data(file2list)         #call function process_data to count no. of banana
        print (file + ': ' + str(count) + ' bananas!')