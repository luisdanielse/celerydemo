from django.shortcuts import render
import json
from django.http import JsonResponse
from .tasks import sendEmail

# Create your views here.
def index(request):
    return render(request, "emails/index.html")


def wsSendEmail(request):
    try:
        data = request.body
        dataObject = json.loads(data)
        email = dataObject["email"]
        mensaje = dataObject["mensaje"]
        emailResponse = sendEmail.delay(email, mensaje)
        if(emailResponse):
            json_response = {'success': 'true'}
        else:
            json_response = {'success': 'fail'}
    except:
        json_response = {'success': 'fail'}
    response = JsonResponse(json_response)
    return response
