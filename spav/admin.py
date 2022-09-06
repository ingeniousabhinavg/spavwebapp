from tkinter.messagebox import NO
from django.contrib import admin
from .models import Alert, Noticeboard, UpcomingLect

# Register your models here.

admin.site.register(Alert)
admin.site.register(Noticeboard)
admin.site.register(UpcomingLect)