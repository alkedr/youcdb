import webapp2

import os
import urllib

from google.appengine.api import users
from google.appengine.ext import ndb

import jinja2


import news


JINJA_ENVIRONMENT = jinja2.Environment(
	loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
	extensions=['jinja2.ext.autoescape'])


class AddNewsPage(webapp2.RequestHandler):

	def get(self):
		template = JINJA_ENVIRONMENT.get_template('add_news.html')
		self.response.write(template.render({}))

	def post(self):
		pieceOfNews = news.News(title = self.request.get('title'), text = self.request.get('text'))
		pieceOfNews.put()
		self.redirect('/add_news')
