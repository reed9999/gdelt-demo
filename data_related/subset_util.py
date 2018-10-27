###
# Extremely simple util script to produce an output file with every Nth line
# of the input file.

import os
# For a more robust script, this could be made directory- and filename-agnostic
# as with other files in this project.
DIR = 'sample_data'
INPUT = os.path.join(DIR, 'input.csv')
OUTPUT = os.path.join(DIR, 'output.csv')
N = 10

with open(INPUT, 'r') as infile:
    lines = infile.readlines()
    print ("Count of lines: {}".format(len(lines)))
    filtered_lines = lines[::N]

with open(OUTPUT, 'w') as outfile:
    outfile.writelines(filtered_lines)