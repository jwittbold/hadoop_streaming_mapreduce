#!/usr/bin/env python
import sys

# master key and 
current_key = None
output_lst = []

# reset() to empty values for reading each line from stdin 
def reset():

    global current_key
    global output_lst

    current_key = None
    output_lst = [] 


# flush values after each line is read 
def flush():

    global current_key
    global output_lst
    total = 0

    for count in output_lst:
        total += count

    print(f'{current_key}\t{total}')


# reads from the mapper
for line in sys.stdin:
    
    # sets key as value of index 0 and count to value at index 1
    col_val = line.split('\t')
    key = col_val[0]
    count = int(col_val[1])

    if current_key != key:
        if current_key != None:
            flush()
        reset()

    # appends counts to output_lst 
    output_lst.append(count)
    current_key = key

# flush last group to stdout 
flush()


# test 
# cat data.csv | python autoinc_mapper1.py | sort | python autoinc_reducer1.py | python autoinc_mapper2.py | sort | python autoinc_reducer2.py | sort