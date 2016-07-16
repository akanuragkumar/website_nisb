from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import *
from django.shortcuts import get_object_or_404
from django.template import loader
import datetime

# Create your views here.
def index(request):
	nisbBulletin = Bulletin.objects.filter(subjectsTo=0).order_by('-id')[:5]
	blrBulletin = Bulletin.objects.filter(subjectsTo=1).order_by('-id')[:5]
	r10Bulletin = Bulletin.objects.filter(subjectsTo=2).order_by('-id')[:5]
	ieeeBulletin = Bulletin.objects.filter(subjectsTo=3).order_by('-id')[:5]
	techNews = Bulletin.objects.filter(subjectsTo=5).order_by('-id')[:5]
	context = {
			'nisbBulletin' : nisbBulletin,
			'blrBulletin' : blrBulletin,
			'r10Bulletin' : r10Bulletin,
			'ieeeBulletin' : ieeeBulletin,
			'techNews' : techNews,
			}
	template = loader.get_template('index.html')
	return HttpResponse(template.render(context, request))

def events(request):
	dateToday = datetime.date.today()
	pastEvents = Events.objects.filter(eventDate<dateToday).order_by('eventDate')[:5]
	futureEvents = Events.objects.filter(eventDate>dateToday).order_by('eventDate')[:5]
	presentEvents = Events.objects.filter(eventDate==dateToday)
	context = {
			'pastEvents' : pastEvents,
			'futureEvents' : futureEvents,
			'todayEvents' : presentEvents,
			}
	template = loader.get_template('events.html')
	return HttpResponse(template.render(context, request))


def fg(request):
	template = loader.get_template('fg.html')
	return HttpResponse(template.render(request))

def cs(request):
	csEvents = Events.objects.filter(ag==1).order_by('eventDate')[:7]
	context = { 'eventsCS' : csEvents, }
	template = loader.get_template('cs.html')
	return HttpResponse(template.render(context, request))

def wie(request):
	wieEvents = Events.objects.filter(ag==2).order_by('eventDate')[:7]
	context = { 'eventsWIe' : wieEvents, }
	template = loader.get_template('wie.html')
	return HttpResponse(template.render(context, request))
def members(request):
	return HttpResponse("Waiting for you to join! :)")

def aboutUs(request):
	template = loader.get_template('about.html')
	return HttpResponse(template.render(request))
