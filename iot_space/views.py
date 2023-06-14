from django.contrib.admin import action
from django.http import HttpResponse, JsonResponse, HttpRequest
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.generic import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView
import json

temp = 0
detect = 'O'
#-- TemplateView
class IoTStatus(View):
    def get(self, request):
        return render(request, 'iot_status.html')
        # return render(request, 'iot_status.html', {'temperature': temp, 'detection': detect})

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request):
        global temp
        global detect
        json_data = json.loads(request.body)
        temp = json_data.get('temperature')
        detect = json_data.get('detection')
        return render(request, 'iot_status.html', {'temperature': temp, 'detection': detect}, content_type='application/json')

    def http_method_not_allowed(self, request, *args, **kwargs):
        return HttpResponse("Method Not Allowed", status=405)

# class IoTConsumption(View):
#
#     @method_decorator(csrf_exempt)
#     def dispatch(self, request, *args, **kwargs):
#         return super().dispatch(request, *args, **kwargs)
#
#     def post(self, request):
#         json_data = json.loads(request.body.decode('utf-8'))
#         temp = json_data.get('temperature')
#         detect = json_data.get('detection')
#         return render(request, 'iot_status.html', {'temperature': temp, 'detection': detect})
#
#     def http_method_not_allowed(self, request, *args, **kwargs):
#         return HttpResponse("Method Not Allowed", status=405)