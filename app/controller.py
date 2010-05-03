import os

import re

from model import Ward, District, County, Postcode

import logging

import urllib

from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
from google.appengine.api import urlfetch
from google.appengine.api.labs import taskqueue
from google.appengine.ext import db

class ModelAndViewPage(webapp.RequestHandler):
	def render(self, view, model={}):
		path = os.path.join(os.path.dirname(__file__), 'templates', view)
		self.response.out.write(template.render(path + '.tpl', model))

class DisplayWard(ModelAndViewPage):
	def get(self):
		postcode_query = self.request.get('postcode').replace(' ', '')
		if postcode_query:
			postcodes = Postcode.all().filter('postcode =', postcode_query).fetch(limit=1)
			self.render('display', {'postcode': postcodes[0] })
		else:
			self.render('display')

class UploadPostcode(ModelAndViewPage):
	def post(self):
		postcode = self.request.get('postcode').replace(' ', '')

		latitude = self.request.get('latitude')
		longitude = self.request.get('longitude')

		ward_code = self.request.get('ward_code')
		district_code = self.request.get('district_code')
		county_code = self.request.get('county_code')
		full_code = county_code + district_code + ward_code

		wards = Ward.all().filter('full_code =', full_code).fetch(limit=1)
		postcode_obj = Postcode(
			postcode = postcode,
			latitude = float(latitude),
			longitude = float(longitude),
			ward = wards[0] if wards else None,
		)
		postcode_obj.put()

class UploadRegion(ModelAndViewPage):
	def get(self):
		self.render('upload')

	def post(self):
		ward_code = self.request.get('ward_code')
		district_code = self.request.get('district_code')
		county_code = self.request.get('county_code')

		counties = County.all().filter('code =', county_code).fetch(limit=1)
		if ward_code:
			districts = District.all().filter('code =', district_code).filter('county =', counties[0].key()).fetch(limit=1)
			ward = Ward(
				name=self.request.get('name'),
				code=ward_code,
				full_code=county_code + district_code + ward_code,
				district=districts[0],
			)
			ward.put()
		elif district_code:
			district = District(
				name=self.request.get('name'),
				code=district_code,
				county=counties[0],
			)	
			district.put()
		else:
			county = County(
				name=self.request.get('name'),
				code=county_code,
			)
			county.put()	

class DeleteStAlbansController(ModelAndViewPage):
	def post(self):
		st_albans = True
		postcodes = Postcode.all().order('-postcode').fetch(10)
		for code in postcodes:
			if code.postcode.startswith('AL'):
				code.delete()
			else:
				st_albans = False

		if st_albans:
			taskqueue.add(url='/delete-st-albans')

	def get(self):
		self.post()

class RemoveDupes(ModelAndViewPage):
	def post(self):
		postcodes = db.GqlQuery("SELECT * FROM Postcode where postcode >= 'BN274SL' order by postcode desc LIMIT 10")
		for postcode in postcodes:
			postcode.delete()
		if postcodes:
			taskqueue.add(url='/remove-dupes')

	def get(self):
		self.post()
