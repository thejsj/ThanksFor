from django.http import HttpResponse
from django.shortcuts import render
from thanksfor.models import Submission

def main(request):

	# Get all submissions
	submissions = Submission.objects.all()

	return render(
		request, 
		'index.html', 
		{
			'example' : 'Some Text',
			'submissions' : submissions
		})
	

def example(request):
	return HttpResponse("Hello World")