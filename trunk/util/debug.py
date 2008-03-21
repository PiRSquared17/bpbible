"""
debug.py - basic logging facilities
"""

import sys
import time
import osutils

__all__ = ["MESSAGE", "WARNING", "ERROR", "dprint", "is_debugging", "TOOLTIP"]
MESSAGE = 0
WARNING = 1
ERROR   = 2
TOOLTIP = 3

level = 0

def is_debugging():
	"""Are we debugging? 
	
	This is true if we are not py2exe'd or we have -d flag.
	TODO: work out some better way to change "py2exe'd" to "released"
	"""
	return not osutils.is_py2exe() or "-d" in sys.argv

def dprint(errorlevel, message, *args):
	if errorlevel >= level:	
		args = [message] + [repr(arg) for arg in args]
		print "%s %s" % (time.strftime("%H:%M:%S"), " ".join(args))
