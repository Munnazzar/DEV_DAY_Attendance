from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from datetime import datetime
import pytz


def landingpage(request):
    if request.method == "POST":
        code= request.POST["code"]
        try:
            record= DevDayAttendence.objects.get(att_code=code)
            try:
                currentTime= datetime.now()
                eventDetails= Event.objects.get(competitionName=record.comp_name)
                utcTime= currentTime.astimezone(pytz.utc) # we have to convert PKT time to UTC, since mongo
                                                          # stores time fields automatically in UTC
                if utcTime<eventDetails.start_time.replace(tzinfo=pytz.utc):
                    return render(request, "html/intro.html", {"msg":"Error: Event has not started yet"})
                elif utcTime>eventDetails.end_time.replace(tzinfo=pytz.utc):
                    return render(request, "html/intro.html", {"msg":"Error: Event has ended"})
            except:
                return render(request, "html/intro.html", {"msg":"Error: Event details not found"})
           
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
