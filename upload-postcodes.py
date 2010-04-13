import urllib
import urllib2
import csv
import os

for file in os.listdir('postcode_data'):
	reader = csv.DictReader(open('postcode_data/' + file), fieldnames=['postcode', '', 'latitude', 'longitude', '', '', '', 'county_code', 'district_code', 'ward_code'])

	url = 'http://localhost:8080/upload-postcode'

	for line in reader:
		print line
		data = urllib.urlencode(line)
		req = urllib2.Request(url, data)
		urllib2.urlopen(req)
