import webapp2

import os
import urllib

from google.appengine.api import users
from google.appengine.ext import ndb

import jinja2


import show
import person
import news
import video
import add_news
import search



JINJA_ENVIRONMENT = jinja2.Environment(
	loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
	extensions=['jinja2.ext.autoescape'])


class MainPage(webapp2.RequestHandler):

	def get(self):
		template = JINJA_ENVIRONMENT.get_template('index.html')
		self.response.write(template.render({}))


application = webapp2.WSGIApplication([
	('/', MainPage),
	('/show', show.ShowPage),
	('/person', person.PersonPage),
	('/news', news.NewsPage),
	('/add_news', add_news.AddNewsPage),
	('/video', video.VideoPage),
	('/search', search.SearchPage),
], debug=True)


