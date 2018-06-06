# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, render_to_response

# Create your views here.
import  datetime, MySQLdb

from django.http import HttpResponse, HttpResponseRedirect, Http404

from django.contrib import auth
from django.db.models import Q
from django.shortcuts import render_to_response
from .models import book , publisher
from django.core.mail import send_mail
from .forms import contactform ,pubform
from django.template import RequestContext, Template, TemplateDoesNotExist
from django.core.mail import send_mail, EmailMessage
import csv
from reportlab.pdfgen import canvas
from io import StringIO
from django.views.decorators.cache import cache_page
from django.urls import reverse
from django.utils.translation import gettext
from django.utils import translation
from django.conf import settings

passengers = [125,65,875, 873, 986, 54, 653, 123, 434]

def hoi(request):
	# txt = """<h1> welcoming you </h1>"""
	 #return HttpResponse(txt)
	timenow = datetime.datetime.now()
	days = ['m', 't','w', 'th', 'f', 's', 'su']
	return render(request, "h2.html", {"time": timenow, "daysweek": days})



def article(req, id):
	 txt = "displaying article number : %s" %id
	 return  HttpResponse(txt) 



def dbom(request):
	 db = MySQLdb.connect(user='root', db= 'djangodb', passwd='giessen', host='localhost')
	 cursor = db.cursor()
	 cursor.execute('select name from names' )
	 names = [row[0] for row in cursor.fetchall()]
	 db.close()
	 return render_to_response('books.html', {'namesintemplate': names})


def search (request):
	query = request.GET.get('q', '')
	printed = query
	if query:
		qset = (Q(title__icontains=query) | Q(authors__firstname__icontains=query) |
				Q(authors__lastname__icontains=query) | Q(authors__email__icontains=query)
 

			)

		results = book.objects.filter(qset).distinct()

	else:
		results = []

	return render_to_response("search.html" , {
		 "r": results, "q":query, "printed":printed,



		}) 

def index(request):
		return render_to_response("index.html")


def contact(request):
	if request.method == 'POST':
		form = contactform(request.POST, initial={'sender':'use@example.com'})
		if form.is_valid():
			topic = form.cleaned_data['topico']
			message = form.cleaned_data['message']
			
			sender = form.cleaned_data.get('sender', 'noreply@example.com')
			send_mail('feedback from site, topic: %s' % topic, message, '', ['med.abuali@gmail.com'], fail_silently=False,)
			return HttpResponseRedirect('index')
			#return HttpResponseRedirect(reverse('sendmail'))

	else:
		form = contactform(initial={'sender':'u@example.com'})
	
	return render(request, 'contact.html', {'form':form})


def publish(request):
	if request.method == 'POST':
		form = pubform(request.POST)
		if form.is_valid():
		
			form.save()
			return HttpResponseRedirect(".")

	else : 
		form = pubform()

	return render(request, 'add_publish.html', {'form': form})
	
def send(request):
	msg = EmailMessage('req callback', 'here is the msg',to=['med.abuali@gmail.com'])
	msg.send()

	#return HttpResponseRedirect('contact/')
	#return HttpResponseRedirect(reverse('sendmail'))
	return render_to_response("search.html")
 

def viewing(request, tmpname):
	return render_to_response(tmpname)



def mailing(request):
	msg= EmailMessage('subject ', 'mesj from inside mail def', to=['meddhif@gmail.com'])


	msg.send()

	return render_to_response('success.html')

def whatever(request):
	try:
		return render_to_response('djk.html')
		
	except TemplateDoesNotExist:
		raise Http404()
		


def csv(request):
	# img = open("/home/mad/Pictures/cpm.pdf", "rb").read()
	# return HttpResponse(img, content_type="application/pdf")
	resp = HttpResponse(content_type='text/csv')
	resp['Content-Disposition']= 'attachment; filename=ruly.csv'


	writer = csv.writer(resp)
	for (year, num) in zip(range(1995,2006), passengers):
		writer.writerow([year,num])

	return resp



def pdf(request):

	resp = HttpResponse(content_type='application/pdf')
	resp['Content-Disposition'] = 'attachment; filename=mypdf.pdf'


	p = canvas.Canvas(resp)

	p.drawString(10,10, "hi there A company needs to develop a strategy for software product development for which it has a choice of two programming languages L1 and L2. The number of lines of code (LOC) developed using L2 is estimated to be twice the LOC developed with Ll. The product will have to be maintained for five years. Various parameters for the company are given in the table below.")

	p.showPage()

	p.save()

	return resp



def pdfx(request):

	resp = HttpResponse(content_type='application/pdf')
	resp['Content-Disposition'] = 'attachment; filename=mypdf.pdf'

	tmp = StringIO()


	p = canvas.Canvas(tmp)

	p.drawString(10,10, "hi there A company needs to develop a strategy for software product development for which it has a choice of two programming languages L1 and L2. The number of lines of code (LOC) developed using L2 is estimated to be twice the LOC developed with Ll. The product will have to be maintained for five years. Various parameters for the company are given in the table below.")

	p.showPage()

	p.save()
	resp.write(tmp.getvalue())
	return resp



@cache_page(60 * 1)
def simpletxt(any):

	if any.user.is_anonymous:
		return HttpResponse("u r logged in  %s" % any.user.is_superuser)
	else:
		return HttpResponse("not logged in")




def log(request):

	if request.method == 'POST':
		usern = request.POST['user']
		passw = request.POST['pass']

		user = auth.authenticate(username=usern, password=passw)
		if user is not None and user.is_active:
			auth.login(request, user)
			return HttpResponse("successful login")

		else:
			return HttpResponse("failed to login")


	return render(request, "log.html")



def logout(request):
	auth.logout(request)

	return render(request, "log.html")



def trans(req):
	#translation.activate('de')
	
	# if req.LANGUAGE_CODE == 'nl':
	#  	return HttpResponse("it is dutch")

	# else:
	#  	return HttpResponse("it is still english")

	#req.session[translation.LANGUAGE_SESSION_KEY] = 'de'
	#req.LANGUAGE_CODE= 'de'
	#if 'HTTP_ACCEPT_LANGUAGE' not in req.META:

		
		 #del req.META['HTTP_ACCEPT_LANGUAGE']

	
	output = gettext("welcome to my site")
	text = u'<html><body>  <h1> header </h1> </hmtl></body>'
	return HttpResponse(text)

	


def transnl(req):

	#req.session[translation.LANGUAGE_SESSION_KEY] = 'nl'
	#req.LANGUAGE_CODE= 'nl'

	

	output = gettext("welcome to my site")

	return HttpResponse(settings.LANGUAGE_CODE)


def inter(req):

	# if LANGUAGE_CODE == 'de':
	# 	return HttpResponse("it is de")
	# else:
	# 	return HttpResponse("it is not de")
	


	#return render(req, "inter.html")
	return HttpResponse(settings.LANGUAGE_CODE)