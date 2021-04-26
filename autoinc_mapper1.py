#!/usr/bin/env python
import sys

# input comes from STDIN (standard input)
for line in sys.stdin:

    col_val = line.split(',')
    incident_type = col_val[1]
    vin = col_val[2]
    vehicle_make = col_val[3]
    vehicle_model = col_val[4]
    vehicle_year = col_val[5]
    agg_values = (incident_type, vehicle_make, vehicle_year)

    # key / values to pass to reducer
    print(f'{vin}\t{agg_values}')

# test
# cat data.csv | python autoinc_mapper1.py | sort