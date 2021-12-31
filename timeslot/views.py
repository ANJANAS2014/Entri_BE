from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Users
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime
import json
import requests
from datetime import timedelta


@csrf_exempt
def listUsers(request):
    try:
        users = list(Users.objects.all().values())
        return JsonResponse({'UserList': users})
    except Exception as e:
        return JsonResponse({'message': 'Server Exception.'+str(e)}, status=500)


@csrf_exempt
def registerUser(request):
    try:
        jsonReq = json.loads(request.body)

        userobj = Users(firstname=jsonReq['firstname'], middlename=jsonReq['middlename'],
                        lastname=jsonReq['lastname'], starttime=jsonReq['starttime'],
                        endtime=jsonReq['endtime'], is_interviewer=jsonReq['is_interviewer'])
        userobj.save()

        return JsonResponse({"message": "Successfully created"}, status=200)

    except Exception as e:
        return JsonResponse({'message': 'Server Exception.'+str(e)}, status=500)


@csrf_exempt
def availabletime(request):
    try:
        jsonReq = json.loads(request.body)

        def daterange(start_time, end_time):
            for n in range(0, int((end_time-start_time).total_seconds()/3600)):
                yield (datetime.strftime(start_time, "%H:%M"),
                       datetime.strftime((start_time + timedelta(seconds=3600)), "%H:%M"))
                start_time += timedelta(seconds=3600)

        users = Users.objects.filter(userid__in=[jsonReq['candidateid'],
                                                 jsonReq['interviewerid']]).values('is_interviewer', 'starttime', 'endtime').order_by('is_interviewer')

        timeslots_candidate = []
        timeslots_interviewer = []

        start_time_candidate = datetime.strptime(
            str(users[0]['starttime']), "%H:%M:%S")
        end_time_candidate = datetime.strptime(
            str(users[0]['endtime']), "%H:%M:%S")
        for singleslot in daterange(start_time_candidate, end_time_candidate):
            timeslots_candidate.append(singleslot)

        start_time_interviewer = datetime.strptime(
            str(users[1]['starttime']), "%H:%M:%S")
        end_time_interviewer = datetime.strptime(
            str(users[1]['endtime']), "%H:%M:%S")
        for singleslot in daterange(start_time_interviewer, end_time_interviewer):
            timeslots_interviewer.append(singleslot)

        return JsonResponse({"available time slots": [item for item in timeslots_interviewer if item in timeslots_candidate]}, status=200)
        pass
    except Exception as e:
        return JsonResponse({'message': 'Server Exception.'+str(e)}, status=500)
