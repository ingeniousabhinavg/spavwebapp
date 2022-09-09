from multiprocessing import context
from django.shortcuts import render
from .models import *
from django.core.paginator import Paginator

# Create your views here.

FicData = FIC.objects.all()
sliderImage = Slider.objects.all()
adminData = Administration.objects.all()
bogData = BOG.objects.all()
bwcData = Bwc.objects.all()
fcData = Fc.objects.all()
senateData = Senate.objects.all()
deansData = Deans.objects.all()
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
    'fcData':fcData,
    'bwcData':bwcData,
    'senateData':senateData,
    'deansData':deansData,
    'sliderImage':sliderImage,
    'adminData':adminData,
    'FicData':FicData,
}

def index(request):
    return render(request, 'index.html',context)

def planning(request):
    return render(request, 'planning.html',context)

def architecture(request):
    return render(request, 'architecture.html',context)

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

def fc(request):
    return render(request, 'fc.html', context )

def bwc(request):
    return render(request, 'bwc.html', context )

def senate(request):
    return render(request, 'senate.html', context )

def deans(request):
    return render(request, 'deans.html', context )

def administration(request):
    return render(request, 'administration.html', context )

def fic(request):
    return render(request, 'fic.html', context )

def health(request):
    return render(request,  'health.html', context )