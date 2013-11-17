from django.db import models
from urllib2 import urlopen, Request
import socket
import json
from django.conf import settings

class Submission(models.Model):

	# Required 

	created_at = models.DateTimeField(
		editable=False,
		auto_now_add=True,
	)

	image = models.ImageField(
		"Submitted Image", 
		upload_to='media/documents/%Y/%m/',
		blank=False, 
		null=False,
	)

	# User info is Optional

	name = models.CharField(
		max_length=255,
		blank=True, 
		null=True,
	)

	email = models.EmailField(
		blank=True, 
		null=True,
	)

	# Get Location

	ip_address = models.GenericIPAddressField(
		blank=True, 
		null=True,
		editable=False,
	)

	location = models.CharField(
		max_length=255,
		blank=True, 
		null=True,
		editable=False,
	)

	# Moderation

	show_in_site = models.BooleanField (
		default=True,
	)

	def __str__(self):
		return str(self.created_at.strftime('%m/%d/%Y')) + " || " + str(self.image)

	def save(self, *args, **kwargs):
		# Add a defulat IP addres for Testing
		if self.ip_address is None and settings.DEBUG:
			self.ip_address = "72.84.236.204"

		# Get Location by IP Address
		url = "http://freegeoip.net/json/" + self.ip_address
		socket.setdefaulttimeout(5)
		headers = {'Typ':'django','Ver':'1.1.1','Connection':'Close'}
		print url
		try:
			req = Request(url, None, headers)
			urlfile = urlopen(req)
			response = json.loads(urlfile.read())
			urlfile.close()
		except Exception:
			pass
		if response:
			if response['region_name']:
				if response['city'] and response['country_code']:
					self.location = response['city'] + ", " + response['region_name']
			else:
				if response['city'] and response['country_name']:
					self.location = response['city'] + ", " + response['country_name']
		super(Submission, self).save(*args, **kwargs)
