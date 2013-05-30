import webapp2

import os
import urllib

from google.appengine.api import users
from google.appengine.ext import ndb

import jinja2


JINJA_ENVIRONMENT = jinja2.Environment(
	loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
	extensions=['jinja2.ext.autoescape'])



class PersonPage(webapp2.RequestHandler):

	def get(self):
		template_values = {
			'first_name': "-first_name-",
			'last_name': "-last_name-",
			'biography': "-biography-",
			'language': "-language-",
			'registration_date': "-registration_date-",
		}
		template = JINJA_ENVIRONMENT.get_template('person.html')
		self.response.write(template.render(template_values))

