###
# Extremely simple util script to produce an output file with every Nth line
# of the input file.
# For a more robust script, this can be made directory- and filename-agnostic
# as with other files in this project but there are higher priorities.

import glob
import os

N = 10
HACK = 'dir'
message = """This is a very simple utility with a lot of hard coding.
Please cp or mv the file you want to convert into the project's sample_data
directory and call it input.csv. This script will grab one out of every {}
lines from the input and save as the output."""
footer = "*****"
print (message.format(N))
print (footer * 16)



def convert(infile_name, outfile_name, n): 
  with open(infile_name, 'r') as infile:
    lines = infile.readlines()
    print ("Count of lines: {}".format(len(lines)))
    filtered_lines = lines[::n]

  with open(outfile_name, 'w') as outfile:
    outfile.writelines(filtered_lines)

def hardcoded_single():
  dirname = 'sample_data'
  infile_name = os.path.join(dirname, 'input.csv')
  outfile_name = os.path.join(dirname, 'output.csv')
  convert(infile_name, outfile_name, N)

def hardcoded_dir():
  dirname = '/home/philip/data-gdelt/'
  filenames = glob.glob(os.path.join(dirname, "*.csv"))
  for x in filenames:
    convert(x, x+".converted", N)

if HACK == "dir":
  hardcoded_dir()
if HACK == "single":
  hardcoded_single()

