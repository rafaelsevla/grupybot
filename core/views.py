from django.shortcuts import render
from django.http.response import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
from core.message import proccess


@csrf_exempt
def events(requests):
    print(requests.body)
    json_telegram = json.loads(requests.body)
    proccess(json_telegram)
    return HttpResponse()
