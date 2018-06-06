from django.conf.urls import url
from myapp import views
from django.conf import settings
from django.views.generic.list import ListView
from myapp.models import publisher
from django.conf.urls import include


publisher_info = {
	
"queryset" : publisher.objects.all(),


}


urlpatterns = [

url(r'^hello', views.hoi, name='xxxhi'),

url(r'^art/(\d+)/', views.article, name='arto'),
url(r'^search/', views.search, name ='search'), 
url(r'^contact/$', views.contact, name ='contact'),
url(r'^publish/', views.publish, name = 'publish'),

url(r'^simple/' , views.simpletxt, name ='simpletxt'),
url(r'^send/', views.send, name ='sendmail'),

#url(r'^pdf', views.pdf, name ='pdf'),
#url(r'^csv', views.csv, name ='csv'),

url(r'^transnl/', views.transnl,  name ='transnl'), 

]

urlpatterns += [

url(r'^xyz', views.viewing, {'tmpname' : 'temp1.html'}),

url(r'^zyx' , views.viewing, {'tmpname' : 'temp2.html'}),


#url(r'^getlog',  views.getlog,  name = 'getlogging'),

url(r'^log/', views.log,  name ='log'),
url(r'^mail', views.mailing , name ='mailing'),
url(r'^whatever/', views.whatever, name ='anything'),

url(r'^publishers/$', ListView.as_view(), publisher_info),
url(r'^inter/' , views.inter,  name ='inter'),


url(r'^i18n/', include('django.conf.urls.i18n'), name='i18n'),
url(r'^csv/', views.csv, name='image'),

url(r'^pdf/', views.pdf, name='pdf'),

url(r'^pdfx/', views.pdfx, name='pdfx'),
url(r'^trans/', views.trans, name ='trans'),

url(r'^', views.index , name ='index'),
]


# if settings.DEBUG:
# 	urlpatterns += [
#         url(r'^debuginfo', views.debug, name ='debug'),


# 	]