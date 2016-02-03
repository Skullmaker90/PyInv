#!/usr/bin/python

# Here is the main module looking for noc command line options.

import sys
import datetime
import Dbquery
from Mydbcon import Mydbcon

def main(com):
	date = datetime.date.today()
	date = date.isoformat()
	q = Dbquery.handler(com)
	q = q(sys.argv[2:], date)
	con = Mydbcon()
	result = con.query(q)
	if result:	
		for i in result:
			print("Location: " + i[0] + " | Switchport: " + i[1] + " | Date: " + i[2].isoformat() + "\n"
				+ "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
	
def test(com):
	print(com)

if __name__ == '__main__':
	import sys
	main(sys.argv[1])
