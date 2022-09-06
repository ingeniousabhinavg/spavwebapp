from multiprocessing import context
from django.shortcuts import render
from .models import Alert, Noticeboard, UpcomingLect
from django.core.paginator import Paginator

# Create your views here.

lectureData = UpcomingLect.objects.all()
noticeData = Noticeboard.objects.all()
alertData = Alert.objects.all()

# noticeboard pagination #


# noticeboard pagination #

context = {
    'alert': alertData,
    'notice':noticeData,
    'lecture': lectureData,
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