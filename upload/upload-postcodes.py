import urllib
import urllib2
import csv
import os

def upload(req, count=0):
	try:
		urllib2.urlopen(req)
	except urllib2.URLError:
		if (count < 3):
			print count
			upload(req, count + 1)
		else:
			raise

for file in os.listdir('postcode_data'):
	print file
	reader = csv.DictReader(open('postcode_data/' + file), fieldnames=['postcode', '', 'latitude', 'longitude', '', '', '', 'county_code', 'district_code', 'ward_code'])

	url = 'http://whats-my-ward.appspot.com/upload-postcode'

	for line in reader:
		print line
		data = urllib.urlencode(line)
		req = urllib2.Request(url, data)
		upload(req)
