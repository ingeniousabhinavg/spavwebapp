from tkinter.messagebox import NO
from django.contrib import admin
from .models import Alert, Noticeboard, UpcomingLect, FeaturedLogo, GlimpseSW

# Register your models here.

admin.site.register(GlimpseSW)
admin.site.register(FeaturedLogo)
admin.site.register(Alert)
admin.site.register(Noticeboard)
admin.site.register(UpcomingLect)