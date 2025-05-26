from django.contrib import admin

from .models import Topic, Entry #imported the Topic class from the model file.

# Register your models here.
admin.site.register(Topic) #tells Django to manage our model through admin-site
admin.site.register(Entry)

