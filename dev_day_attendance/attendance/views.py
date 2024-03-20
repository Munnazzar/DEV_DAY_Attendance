from django.shortcuts import render
from . models import Participants,Attendance
def landingpage(request):
    return render(request, 'html/intro.html')
def success_page(request):
    return render(request, 'html/success.html')