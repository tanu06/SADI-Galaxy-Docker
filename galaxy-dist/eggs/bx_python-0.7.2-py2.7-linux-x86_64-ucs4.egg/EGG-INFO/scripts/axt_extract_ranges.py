#!/afs/bx.psu.edu/project/pythons/py2.7-linux-x86_64-ucs4/bin/python2.7

"""
Reads a list of intervals and an axt. Produces a new axt containing the
portions of the original that overlapped the intervals

usage: %prog interval_file refindex [options] < axt_file
   -m, --mincols=10: Minimum length (columns) required for alignment to be output
"""

import psyco_full

from bx.cookbook import doc_optparse

import bx.align.axt
from bx import intervals
import sys


def __main__():

	# Parse Command Line

	options, args = doc_optparse.parse( __doc__ )

	try:
		range_filename = args[ 0 ]
		refindex = int( args[ 1 ] )
		if options.mincols: mincols = int( options.mincols )
		else: mincols = 10
	except:
		doc_optparse.exit()

	# Load Intervals

	intersecter = intervals.Intersecter()
	for line in file( range_filename ):
		fields = line.split()
		intersecter.add_interval( intervals.Interval( int( fields[0] ), int( fields[1] ) ) )

	# Start axt on stdout

	out = bx.align.axt.Writer( sys.stdout )

	# Iterate over input axt

	for axt in bx.align.axt.Reader( sys.stdin ):
		ref_component = axt.components[ refindex ]
		# Find overlap with reference component
		intersections = intersecter.find( ref_component.start, ref_component.end )
		# Keep output axt ordered
		intersections.sort()
		# Write each intersecting block
		for interval in intersections: 
			start = max( interval.start, ref_component.start )
			end = min( interval.end, ref_component.end )
			sliced = axt.slice_by_component( refindex, start, end ) 
			good = True
			for c in sliced.components: 
				if c.size < 1: 
					good = False
			if good and sliced.text_size > mincols: out.write( sliced )
		 
	# Close output axt

	out.close()

if __name__ == "__main__": __main__()
