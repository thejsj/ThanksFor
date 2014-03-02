from django.http import HttpResponse
from django.shortcuts import render
from thanksfor.models import Submission
from django.conf.urls import url, patterns, include
from django.contrib.auth.models import User, Group
from rest_framework import viewsets, routers

from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views.decorators.csrf import csrf_exempt

from thanksfor.forms import DocumentForm
import json
from django.contrib.sites.models import get_current_site
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from functions import *

def main(request):

    # Get all submissions
    submissions = Submission.objects.all().order_by('created_at')
    submissions = submissions.reverse()

    # Get Site URL for JS
    this_site_url = get_current_site(request).domain
    this_site_media_url = settings.MEDIA_URL

    return render(
        request, 
        'submission.html', 
        {
            'submissions' : submissions,
            'this_site_url' : this_site_url,
        })

@csrf_exempt
def ajax_upload(request):
    # Handle file upload
    if request.method == 'POST':
        try:   
            # Get User Agent
            user_agent = str( request.META.get('HTTP_USER_AGENT', '') )

            # Add Submission
            new_image_submission = Submission(
                image=request.FILES['docfile'],
                user_agent=user_agent
            )
            new_image_submission.save()

            # Crop Image
            new_image_submission = cropImage(new_image_submission)

            # If IOS Device Rotate (100% Hack)
            if request.POST.get('ios-device') == '1':
                subject = 'New Image Uploaded (From Iphone)'
                new_image_submission = rotateImageClockWise(new_image_submission)
            else:
                subject = 'New Image Uploaded (Not From Iphone)'

            # Send Email to Laurie and Jorge
            image_url = path = os.path.join(settings.MEDIA_URL, str(new_image_submission.image))
            try:
                # <img src="http://thanks-for.com' + str(image_url) + '" />'
                html_message='New Image Uploaded. <br/><br/>Please Check Image Here: <a href="http://thanks-for.com' + str(image_url) + '">' + str(image_url) + '</a><br/><br/><img src="http://thanks-for.com' + str(image_url) + '" />'
                msg = EmailMultiAlternatives(
                    subject, 
                    'New Image Uploaded. Please Check Image', 
                    'jorge.silva@thejsj.com',
                    ['jorge.silva@thejsj.com', 'laurie@designbylkc.com'], 
                )
                msg.attach_alternative(html_message, "text/html")
                msg.send()
            except:
                pass

            return HttpResponse(
                json.dumps([1, new_image_submission.pk, request.POST.get('ios-device')]), 
                content_type='application/javascript'
            )
        except:
            return HttpResponse(
                json.dumps(['Eror Processing This Form', request.POST.get('ios-device')]),
                content_type='application/javascript'
            )
    # Render list page with the documents and the form
    return HttpResponse(
        json.dumps(['This is not a Post Request']), 
        content_type='application/javascript'
    )

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    model = User

class GroupViewSet(viewsets.ModelViewSet):
    model = Group

class SubmissionViewSet(viewsets.ModelViewSet):
    model = Submission

# Routers provide an easy way of automatically determining the URL conf
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'submissions', SubmissionViewSet)
