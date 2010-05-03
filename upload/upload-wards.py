import urllib
import urllib2
import csv

reader = csv.DictReader(open('codelist.txt'), fieldnames=['county_code', 'district_code', 'ward_code', 'name'])

url = 'http://whats-my-ward.appspot.com/upload-region'

for line in reader:
	print line
	data = urllib.urlencode(line)
	req = urllib2.Request(url, data)
	urllib2.urlopen(req)
