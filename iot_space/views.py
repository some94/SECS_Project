from django.contrib.admin import action
from django.http import HttpResponse, JsonResponse, HttpRequest
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.generic import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
import json

#-- TemplateView
class IoTStatus(TemplateView):
    template_name = 'iot_status.html'

class IoTConsumption(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request):
        json_data = json.loads(request.body.decode('utf-8'))
        temp = json_data.get('temperature')
        return render(request, 'iot_status.html', {'temperature': temp})

    def http_method_not_allowed(self, request, *args, **kwargs):
        return HttpResponse("Method Not Allowed", status=405)