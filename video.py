import webapp2

import os
import urllib

from google.appengine.api import users
from google.appengine.ext import ndb

import wsgiref.handlers

import gdata
import gdata.urlfetch
import gdata.service
import gdata.youtube
import gdata.youtube.service
import jinja2


JINJA_ENVIRONMENT = jinja2.Environment(
	loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
	extensions=['jinja2.ext.autoescape'])



class VideoPage(webapp2.RequestHandler):

	def PrintEntryDetails(self, entry):
		print 'Video title: %s' % entry.media.title.text
		print 'Video published on: %s ' % entry.published.text
		print 'Video description: %s' % entry.media.description.text
		print 'Video tags: %s' % entry.media.keywords.text
		print 'Video watch page: %s' % entry.media.player.url
		print 'Video flash player URL: %s' % entry.GetSwfUrl()
		print 'Video duration: %s' % entry.media.duration.seconds

	def get(self):
		youtube = gdata.youtube.service.YouTubeService()
		id = self.request.get("id");
		video = youtube.GetYouTubeVideoEntry(video_id=id)
		#self.PrintEntryDetails(video)
		
		template_values = {
			'video': video
		}
		template = JINJA_ENVIRONMENT.get_template('video.html')
		self.response.write(template.render(template_values))



