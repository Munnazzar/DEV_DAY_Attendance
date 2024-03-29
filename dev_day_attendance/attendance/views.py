from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from .models import *
from datetime import datetime
import pytz
from .utils import *


def landingpage(request):
    if request.method == "POST":
        code= request.POST["code"]
        usrLat= request.POST["latitude"]    #will return wgs84 coordinates
        usrLng= request.POST["longitude"]
        #print("coordinates: ", usrLat, usrLng) #debugging purposes
        if usrLat=="" or usrLng=="":
            return render(request, "html/intro.html", {"msg":"Error: Please enable location services or contact a PR member for help"})
        try:
            fastLat= 24.917066318181814 #wgs84 coordinates
            fastLng= 67.02640213636363  #TODO change these to the actual coordinates of Fast
            distance= WGS84_Distance_Calc(fastLat, fastLng, usrLat, usrLng)
            #print("distance: ", distance) #debugging purposes
            record= DevDayAttendence.objects.get(att_code=code)
            if distance>1000: #a kilometer
                return render(request, "html/intro.html", {"msg":"Error: You are not in the vicinity of the event"})
            try:
                currentTime= datetime.now()
                eventDetails= Event.objects.get(competitionName=record.comp_name)
                utcTime= currentTime.astimezone(pytz.utc) # we have to convert PKT time to UTC, since mongo
                                                          # stores time fields automatically in UTC
                if utcTime<eventDetails.start_time.replace(tzinfo=pytz.utc):
                    return render(request, "html/intro.html", {"msg":"Error: Competition has not started yet"})
                elif utcTime>eventDetails.end_time.replace(tzinfo=pytz.utc):
                    return render(request, "html/intro.html", {"msg":"Error: Competition has ended"})
            except:
                return render(request, "html/intro.html", {"msg":"Error: Competition details not found"})
           
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
