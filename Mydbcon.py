#!/usr/bin/python

# This is going to be a way we manage empty spaces on C5.
# I'll be going through and getting an initial database and once something is
# checked out to a location we can mark it off etc, I'll attempt to audit 1'ce/week.

import MySQLdb

class Controller(object):
	def __init__(self):
		self.con = None
	
	def __enter__(self):
		self.con = MySQLdb.connect(host='71.6.132.43',
				user='cari',
				passwd='',
				db='C5Datacenter')
		return self.con.cursor()
	
	def __exit__(self, type, value, traceback):
		if self.con:
			self.con.commit()
			self.con.close()
		else:
			raise Exception("Something went wrong")

class Mydbcon(object):
	def __init__(self):
		pass

	def query(self, string):
		with Controller() as db:
			if db.execute("""%s""" % (string,)):
				result = db.fetchall()
			return result
