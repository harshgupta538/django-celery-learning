from django.shortcuts import render, HttpResponse
from .tasks import test_func
# Create your views here.

def test_view(request):
    test_func.delay()
    return HttpResponse("Done")