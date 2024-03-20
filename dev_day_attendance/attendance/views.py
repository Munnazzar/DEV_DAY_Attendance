from django.shortcuts import render
from .models import *


def landingpage(request):
    DevDayAttendenceData = DevDayAttendence.objects.all()

    return render(
        request, "html/intro.html", {"DevDayAttendenceData": DevDayAttendenceData}
    )
