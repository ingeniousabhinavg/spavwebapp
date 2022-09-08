from multiprocessing import context
from django.shortcuts import render
from .models import Alert, Noticeboard, UpcomingLect, FeaturedLogo, GlimpseSW, SystemAdmin, TechanicalOfficer, Chairperson, Director, BOG, Slider
from django.core.paginator import Paginator

# Create your views here.

sliderImage = Slider.objects.all()
bogData = BOG.objects.all()
directorData = Director.objects.all()
chairpersonData = Chairperson.objects.all()
toData = TechanicalOfficer.objects.all()
systemadminData = SystemAdmin.objects.all()
lectureData = UpcomingLect.objects.all()
noticeData = Noticeboard.objects.all()
alertData = Alert.objects.all()
featuredLogo = FeaturedLogo.objects.all()
studentswork = GlimpseSW.objects.all()

# noticeboard pagination #


# noticeboard pagination #

context = {
    'alert': alertData,
    'notice':noticeData,
    'lecture': lectureData,
    'logo': featuredLogo,
    'studentswork':studentswork,
    'systemadminData':systemadminData,
    'toData':toData,
    'chairpersonData':chairpersonData,
    'directorData':directorData,
    'bogData':bogData,
    'sliderImage':sliderImage,

}

def index(request):
    return render(request, 'index.html',context)

def noticeboard(request):
    noticeData = Noticeboard.objects.all()
    paginator = Paginator(noticeData, 2) # Show 25 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    contextt = {
        'notice': noticeData,
        'page':page_obj
    }
    return render(request, 'noticeboard.html',contextt)

def registration(request):
    return render(request, 'registration.html' )

def cc(request):
    return render(request, 'cc.html', context )

def chairperson(request):
    return render(request, 'chairperson.html', context )

def director(request):
    return render(request, 'director.html', context )

def actsnstatute(request):
    return render(request, 'actsnstatute.html', context )

def bog(request):
    return render(request, 'bog.html', context )