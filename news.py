import webapp2

import os
import urllib

from google.appengine.api import users
from google.appengine.ext import ndb

import jinja2


JINJA_ENVIRONMENT = jinja2.Environment(
	loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
	extensions=['jinja2.ext.autoescape'])


class News(ndb.Model):
	title = ndb.StringProperty(indexed=False)
	text = ndb.StringProperty(indexed=False)
	date = ndb.DateTimeProperty(auto_now_add=True)


class NewsPage(webapp2.RequestHandler):

	def get(self):

		news_query = News.query().order(News.date)

		template_values = {
			'news': news_query,
		}
		template = JINJA_ENVIRONMENT.get_template('news.html')
		self.response.write(template.render(template_values))
