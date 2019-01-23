from django.contrib import admin
from .models import Meeting, MeetingMinuted, Resource, Event

# Register your models here.
admin.site.register(Meeting)
admin.site.register(MeetingMinuted)
admin.site.register(Resource)
admin.site.register(Event)
