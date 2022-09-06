from multiprocessing import context
from django.shortcuts import render
from .models import Alert

# Create your views here.

alertData = Alert.objects.all

context = {
    'alert': alertData
}


def index(request):
    return render(request, 'index.html',context)