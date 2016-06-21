#!//anaconda/bin/python

################################################################################
##<---------------------------- 80 chars across ----------------------------->##
##        1         2         3         4         5         6         7       ##  
##2345678901234567890123456789012345678901234567890123456789012345678901234567##
################################################################################

import sys 
import os
import time
import math
import re
from operator import itemgetter, attrgetter, methodcaller

## order -----------------------------------------------------------------------
# Usage:
# 
#   order(array, fn)
#
# Returns an ordered list of sorted elements by fn.
def order(arr,fn):
	decorated = [(x,fn(x)) for x in arr]
	sortd = sorted(decorated,key=itemgetter(1))
	undecorated = [x for (x,y) in sortd]
	return undecorated

""

def main():
	if len(sys.argv) < 3:
		statement = '''
		
	Concatenates two CSVs horizontally. Cuts off the file with more rows 
	to the length of the smaller one, and aligns row by row.

	Usage:
	'''	
		print(statement)
		print('\t\t','python concat_horizontal.py <file1...n>\n')

	else:
		# open all files
		filenames = [f for f in sys.argv[1:]]
		openfiles = [open(f) for f in filenames]
		files = [x.readlines() for x in openfiles]
		print('Concatenating files ' + str(filenames) + " horizontally." )

		# timestamp for a unique filename
		timestamp = int(time.time())
		
		# make a new unique directory for CSVs to live in
		directory = "horizontally_concatenated" + "/"
		
		# make director
		if not os.path.exists(directory):
		    os.makedirs(directory)

		# sort all files by length
		sorted_by_length = order(files,len)

		# choose the smallest to be the first set of columns and strip newlines
		out = [x.strip() for x in sorted_by_length[0]]
		
		# add all rows with commas seperating
		for f in sorted_by_length[1:]:
			for i in range(0,len(sorted_by_length[0])):
				out[i] = out[i] + "," + f[i]

		# unique file for csv
		outfile = open(directory + "concat_h_" + filenames[0].split('/')[-1].split('.')[0] + "." + "csv",'w+')

		# write out all lines
		for line in out:
			outfile.write(line.strip() + '\n')

		# close just in case
		outfile.close()


if __name__ == '__main__':
	main()
