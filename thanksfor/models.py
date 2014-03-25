from django.db import models
from urllib2 import urlopen, Request
import socket
import json
from django.conf import settings
from datetime import datetime


class Submission(models.Model):

    # Required 

    created_at = models.DateTimeField(
        default=datetime.now,
        editable=True,
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
        editable=True,
    )

    location = models.CharField(
        max_length=255,
        blank=True, 
        null=True,
        editable=True,
    )

    # User Agent
    user_agent = models.CharField(
        max_length=255,
        blank=True, 
        null=True,
    ) 

    # Moderation

    show_in_site = models.BooleanField (
        default=True,
    )

    def __str__(self):
        return str(self.created_at.strftime('%m/%d/%Y')) + " || " + str(self.image)

    def image_thumb(self):
        if self.image:
            return u'<img src="%s" style="max-width: 200px; max-height: 200px;" />' % (self.image.url)
        else:
            return "No Image To Display"
    image_thumb.short_description = 'Thumbnail'
    image_thumb.allow_tags = True

    def save(self, *args, **kwargs):
        # Add a defulat IP addres for Testing
        if self.ip_address is not None and self.ip_address != '':
            # Get Location by IP Address
            url = "http://freegeoip.net/json/" + self.ip_address
            socket.setdefaulttimeout(5)
            headers = {'Typ':'django','Ver':'1.1.1','Connection':'Close'}
            try:
                req = Request(url, None, headers)
                urlfile = urlopen(req)
                response = json.loads(urlfile.read())
                urlfile.close()
            except Exception:
                pass
            if response and (self.location == "" or self.location is None):
                if response['region_name']:
                    if response['city'] and response['country_code']:
                        self.location = response['city'] + ", " + response['region_name']
                else:
                    if response['city'] and response['country_name']:
                        self.location = response['city'] + ", " + response['country_name']
        super(Submission, self).save(*args, **kwargs)
