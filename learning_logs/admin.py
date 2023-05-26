from django.contrib import admin
from .models import Topic

# model management should carry out through the admin site
admin.site.register(Topic)

