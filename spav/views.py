from multiprocessing import context
from django.shortcuts import render
from .models import Alert, Noticeboard, UpcomingLect

# Create your views here.

lectureData = UpcomingLect.objects.all()
noticetData = Noticeboard.objects.all()
alertData = Alert.objects.all()

context = {
    'alert': alertData,
    'notice': noticetData,
    'lecture': lectureData,
}


def index(request):
    return render(request, 'index.html',context)

def noticeboard(request):
    return render(request, 'noticeboard.html',context)