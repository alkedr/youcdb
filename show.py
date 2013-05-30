import webapp2

import os
import urllib

from google.appengine.api import users
from google.appengine.ext import ndb

import jinja2


import wsgiref.handlers

import gdata
import gdata.urlfetch
import gdata.service
import gdata.youtube
import gdata.youtube.service

from google.appengine.ext import webapp



JINJA_ENVIRONMENT = jinja2.Environment(
	loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
	extensions=['jinja2.ext.autoescape'])


class ShowPage(webapp2.RequestHandler):

	def get(self):
		client = gdata.youtube.service.YouTubeService()
		id = self.request.get("id");
		playlist_uri = "http://gdata.youtube.com/feeds/api/playlists/" + id
		playlist = client.GetYouTubePlaylistEntry(playlist_id=id)
		playlist_video_feed = client.GetYouTubePlaylistEntry(playlist_uri)
		template_values = {
			'id': id,
			'name': "-name-",
			'description': "-description-",
			'language': "-language-",
		}
		template = JINJA_ENVIRONMENT.get_template('show.html')
		self.response.write(template.render(template_values))

