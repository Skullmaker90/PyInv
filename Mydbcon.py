#!/usr/bin/python

# This is going to be a way we manage empty spaces on C5.
# I'll be going through and getting an initial database and once something is
# checked out to a location we can mark it off etc, I'll attempt to audit 1'ce/week.

import MySQLdb

class Mydbcon(object):
	def __init__(self):
		pass

	def dbopen(self):
		return MySQLdb.connect(host='71.6.132.43', 
				user='cari',
				passwd='',
				db='C5Datacenter')

	def close(self, dbcon):
		if dbcon.close():
			return True

	def query(self, string):
		try:
			db = self.dbopen()
			cur = db.cursor()
			if cur.execute("""%s""" % (string,)):
				result = cur.fetchall()
				db.commit()
				self.close(cur)
			return result
				
		except:
			self.close(cur)
