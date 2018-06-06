# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from myapp.models import author, publisher, book
# Register your models here.
admin.site.register(author)
admin.site.register(publisher)
admin.site.register(book)