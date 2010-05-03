from google.appengine.ext import db

import logging

class County(db.Model):
	name = db.StringProperty()
	code = db.StringProperty()
	version=db.IntegerProperty(default=1)

class District(db.Model):
	name = db.StringProperty()
	code = db.StringProperty()
	county = db.ReferenceProperty(County)	
	version=db.IntegerProperty(default=1)

class Ward(db.Model):
	name = db.StringProperty()	
	code = db.StringProperty()
	full_code = db.StringProperty()
	district = db.ReferenceProperty(District)	
	version=db.IntegerProperty(default=1)

class Postcode(db.Model):
	postcode = db.StringProperty()
	latitude = db.FloatProperty()
	longitude = db.FloatProperty()
	ward = db.ReferenceProperty(Ward)
	version = db.IntegerProperty(default=1)
