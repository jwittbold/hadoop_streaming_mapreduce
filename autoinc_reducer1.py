#!/usr/bin/env python
import sys


# initialize an empty dict to store incident types and associated values
master_dict = {}
current_vin = None
output_lst = []

# reset() to empty values for reading each line from stdin 
def reset():
    global master_dict
    global current_vin
    global output_lst

    master_dict = {}
    current_vin = None
    output_lst = [] 


# flush values after each line is read 
def flush():

    global master_dict
    global current_vin
    global output_lst

    for vehicle_info in output_lst:
        
        # checks for type 'A' incidents and parses values for vin, incident_type, make, year, prints values
        incident_type = vehicle_info[0]
        if incident_type == 'A':
            make = master_dict[current_vin][1]
            year = master_dict[current_vin][2]
            vehicle_info = (incident_type, make, year)
            print(f'{current_vin}\t{vehicle_info}')
        # skips incidents not of type 'A'
        else:
            continue


# reads from the mapper
for line in sys.stdin:

    col_val = line.split('\t')
    vin = col_val[0]

    # convert string to tuple 
    vehicle_info = eval(col_val[1])

    # adds vin as key to master_dict if incident_type = 'I'
    incident = vehicle_info[0]
    if incident == 'I':
        master_dict[vin] = vehicle_info

    if current_vin != vin: 
        if current_vin != None:
            # flush() function writes results to STDOUT
            flush()
        reset()

    # appends vehicle_info to output_lst to be used within flush() function
    output_lst.append(vehicle_info)
    current_vin = vin

# flush output from last group
flush()


# test mapper and reducer 
# cat data.csv | python autoinc_mapper1.py | sort | python autoinc_reducer1.py