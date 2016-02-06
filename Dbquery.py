#!/usr/bin/python

# This is the string library for mysql query's are stored. Basically returning the correct string. 

import datetime

def handler(command, loc=None):
	return globals()[command]

def locations(params=None, date=None):
	param = 'Yes'
	string = ("""SELECT * FROM Pod WHERE IsOpen='%s'""" % (param,))
	return string

def checkout(params, date=None):
	string = ("""UPDATE Pod SET IsOpen='No', VerifyDate='%s' WHERE Location='%s'""" % (date, params[0],))
	return string

def checkin(params, date=None):
	string = ("""UPDATE Pod SET IsOpen='Yes', VerifyDate='%s' WHERE Location='%s'""" % (date, params[0]))
	return string

def add_location(params, date):
	loc, switch, isopen, date = params[0], params[1], params[2], date
	string = ("""INSERT INTO Pod (Location, Switchport, VerifyDate, IsOpen) VALUES ('%s', '%s', '%s', '%s')""" % (loc, switch, date, isopen))
	return string

def lookup(params):
	string = ("""SELECT * FROM Pod WHERE Location='%s'""" % (params))
	return string
