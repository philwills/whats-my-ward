from model import Ward, Postcode

import logging

from google.appengine.tools import bulkloader

def get_ward(full_code):
	wards = Ward.all().filter('full_code =', full_code).fetch(limit=1)
	return wards[0] if wards else None

class PostcodeLoader(bulkloader.Loader):
	def __init__(self):
		bulkloader.Loader.__init__(self, 'Postcode',
			[
			('postcode', lambda x: x.replace(' ', '')),
			('latitude', float),
			('longitude', float),
			('ward', get_ward)
			])

loaders = [PostcodeLoader]
