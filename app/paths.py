from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app

from controller import *

application = webapp.WSGIApplication([
									('/upload-region', UploadRegion),
									('/upload-postcode', UploadPostcode),
									('/', DisplayWard),
									('/delete-st-albans', DeleteStAlbansController),
									('/remove-dupes', RemoveDupes),
									], debug=True)
		
def main():
	run_wsgi_app(application)

if __name__ == "__main__":
	main()
