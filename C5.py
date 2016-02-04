#!/usr/bin/python

# Here is the main module looking for noc command line options.

import sys
import datetime
import Dbquery
from Mydbcon import Mydbcon

def main(com):
	date = datetime.date.today().isoformat()
	q = Dbquery.handler(com)(sys.argv[2:], date)
	result = Mydbcon().query(q)
	if result:	
		for i in result:
			print("Location: " + i[0] + " | Switchport: " + i[1] + " | Date: " + i[2].isoformat() + "\n"
				+ "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
	if (len(sys.argv) > 2):
		v = Dbquery.handler('verify')(sys.argv[2])
		for i in Mydbcon().query(v):
			print('\nLocation: ' + i[0] + ' | Open: ' + i[3] + ' | Verify Date: ' + i[2].isoformat() + '\n')
	

if __name__ == '__main__':
	import sys
	main(sys.argv[1])
