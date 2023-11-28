import json

from django.http import HttpResponse
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.generic import View
from django.views.decorators.csrf import csrf_exempt

iot_temperature = 25.0
iot_ir_state = 'O'


class IoTStatus(View):
    def get(self, request):
        return render(request, 'iot_status.html', {'temperature': iot_temperature, 'detection': iot_ir_state})

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request):
        global iot_temperature
        global iot_ir_state
        data = json.loads(request.body)
        print(data)

        iot_temperature = data.get('temperature')
        iot_ir_state = data.get('detection')

        return render(request, 'iot_status.html', {'temperature': iot_temperature, 'detection': iot_ir_state})

    def http_method_not_allowed(self, request, *args, **kwargs):
        return HttpResponse("Method Not Allowed", status=405)