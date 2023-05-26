from django.contrib import admin
from .models import Topic, Entry

# model management should carry out through the admin site
admin.site.register(Topic)
admin.site.register(Entry)
