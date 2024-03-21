from django.shortcuts import render
from django.http import HttpResponse
from .models import *


def landingpage(request):
    if request.method == "POST":
        code= request.POST["code"]
        try:
            record= DevDayAttendence.objects.get(att_code=code)
            try:
                attendanceObj= Attendance.objects.get(teamName=record.team_name)
                if attendanceObj.attendanceStatus:
                    msg="Your attendance has already been marked"
                else:
                    msg="Your attendance has been marked."
                    attendanceObj.update(set__attendanceStatus=True)
                
                return render(request, "html/success.html", {"msg": msg, "teamName": record.team_name})
            except:
                attendanceObj= Attendance(teamName=record.team_name)
                attendanceObj.save()
                return render(request, "html/intro.html", {"msg":"Error: Incorrect code"})
        except:
            return render(request, "html/intro.html", {"msg":"Error: Incorrect code"})
    
    return render(request, "html/intro.html", {"msg":""})
