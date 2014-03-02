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

from functions import cropImage

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
            # Add Submission
            new_image_submission = Submission(image=request.FILES['docfile'])
            new_image_submission.save()

            # Crop Image
            cropImage(new_image_submission)

            return HttpResponse(
                json.dumps([1, new_image_submission.pk]), 
                content_type='application/javascript'
                )
        except:
            return HttpResponse(
                json.dumps(['Eror Processing This Form']),
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
