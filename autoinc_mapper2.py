#!/usr/bin/env python
import sys


# input comes from STDIN (output from previous MapReduce)
for line in sys.stdin:

    col_val = line.split('\t')
    vin = col_val[0]

    vehicle_info = eval(col_val[1])
    make = vehicle_info[1]
    year = vehicle_info[2]
    
    composite_key = f'{make}{year}'
    count = 1

    print(f'{composite_key}\t{count}')


# test mapper1, reducer1, mapper2
# cat data.csv | python autoinc_mapper1.py | sort | python autoinc_reducer1.py | python autoinc_mapper2.py | sort 