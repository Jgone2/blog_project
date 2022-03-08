from django.contrib import admin
from .models import Blog, Comment

# Register your models here.
admin.site.register(Blog)   # admin사이트에 Blog객체 적재
admin.site.register(Comment)
