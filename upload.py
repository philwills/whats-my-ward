import urllib
import urllib2
import csv

reader = csv.DictReader(open('codelist.txt'), fieldnames=['county_code', 'district_code', 'ward_code', 'name'])

url = 'http://localhost:8080/upload-region'

for line in reader:
	print line
	data = urllib.urlencode(line)
	req = urllib2.Request(url, data)
	urllib2.urlopen(req)
