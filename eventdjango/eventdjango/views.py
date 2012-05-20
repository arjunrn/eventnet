from django.template import RequestContext
from django.shortcuts import render_to_response
from eventdjango import models

def eventform(request):
	fm = models.CreateEventForm()
	return render_to_response('create_event.html', {'fm':fm}, RequestContext(request))