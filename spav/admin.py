from tkinter.messagebox import NO
from django.contrib import admin
from .models import Alert, Noticeboard, UpcomingLect, FeaturedLogo, GlimpseSW, SystemAdmin, TechanicalOfficer, Chairperson, Director

# Register your models here.

admin.site.register(Director)
admin.site.register(Chairperson)
admin.site.register(TechanicalOfficer)
admin.site.register(SystemAdmin)
admin.site.register(GlimpseSW)
admin.site.register(FeaturedLogo)
admin.site.register(Alert)
admin.site.register(Noticeboard)
admin.site.register(UpcomingLect)