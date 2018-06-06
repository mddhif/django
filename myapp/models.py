# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class publisher(models.Model):
   name = models.CharField(max_length=30)
   address = models.CharField(max_length=50)
   city = models.CharField(max_length=60)
   state = models.CharField(max_length=30)
   country = models.CharField(max_length=50)
   website = models.URLField()
   def  __str__(self):
   	return self.name

   class Meta:
   		ordering = ('name',)


   class Admin:
    	pass
 
         


class author (models.Model):
    sal =  models.CharField(max_length=10)
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    email = models.EmailField()
    headshot = models.ImageField(upload_to='home/mad/mydjango/')
    def __str__(self):
    	return self.firstname
    class Admin:
    	pass
     

class book(models.Model):
	 title = models.CharField(max_length=40)
	 authors = models.ManyToManyField(author)
	 publisher = models.ForeignKey('publisher', on_delete=models.CASCADE, )
	 date = models.DateField()
	 num_pages =models.IntegerField(blank=True, null=True)
	 def __str__(self):
	 	return self.title
	 class Admin:
	 	pass