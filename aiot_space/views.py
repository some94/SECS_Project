from django.http import HttpResponse
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.generic import View
from django.views.decorators.csrf import csrf_exempt
from aiot_space.models import DhtSensor, IrSensor

import json

aiot_temperature = 25.0
aiot_ir_state = 'O'


class AIoTStatus(View):
    def get(self, request):
        return render(request, 'aiot_status.html', {'temperature': aiot_temperature, 'detection': aiot_ir_state})

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request):
        global aiot_temperature
        global aiot_ir_state
        data = json.loads(request.body)
        print(data)

        aiot_temperature = data.get('temperature')
        aiot_ir_state = data.get('detection')

        return render(request, 'iot_status.html', {'temperature': aiot_temperature, 'detection': aiot_ir_state})

    def http_method_not_allowed(self, request, *args, **kwargs):
        return HttpResponse("Method Not Allowed", status=405)