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
import jinja2
import re


JINJA_ENVIRONMENT = jinja2.Environment(
	loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
	extensions=['jinja2.ext.autoescape'])


class SearchPage(webapp2.RequestHandler):

	def SearchAndPrint(search_terms):
		yt_service = gdata.youtube.service.YouTubeService()
		query = gdata.youtube.service.YouTubeVideoQuery()
		query.vq = search_terms
		query.orderby = 'viewCount'
		query.racy = 'include'
		feed = yt_service.YouTubeQuery(query)
		PrintVideoFeed(feed)

	def get(self):
		youtube = gdata.youtube.service.YouTubeService()

		query = gdata.youtube.service.YouTubeVideoQuery()
		query.vq = self.request.get('q').encode('utf8')
		query.orderby = 'viewCount'
		query.racy = 'include'

		videos = youtube.YouTubeQuery(query).entry

		videoIds = {}
		for video in videos:
			videoIds[video.id] = urllib.unquote_plus(video.id.ToString().split('<')[2].split('/')[9])

		template_values = {
			'q': self.request.get('q'),
			'videos': videos,
			'videoIds': videoIds,
		}
		for video in videos:
			print '%s', video.id
		template = JINJA_ENVIRONMENT.get_template('search.html')

		self.response.write(template.render(template_values))

