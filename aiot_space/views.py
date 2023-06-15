from django.http import HttpResponse
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.generic import View
from django.views.decorators.csrf import csrf_exempt
from aiot_space.models import DhtSensor, IrSensor

import json

class AIoTStatus(View):
    def get(self, request):
        aiot_context = request.session.get['aiot_context']
        if aiot_context:
            context = {'aiot_context': aiot_context}
            return render(request, 'aiot_status.html', context)
        else:
            return HttpResponse('Session value not found.')

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request):
        data = json.loads(request.body.decode('utf-8'))
        aiot_temperature = data['aiot_temperature']
        aiot_ir_state = data['aiot_ir_state']
        aiot_context = {'aiot_temperature': aiot_temperature, 'aiot_ir_state': aiot_ir_state}
        request.session['aiot_context'] = aiot_context

        return render(request, 'aiot_status.html', context=aiot_context, content_type='application/json')

    # def get(self, request):
    #     latest_dht_sensor = DhtSensor.objects.latest('timestamp')
    #     latest_temperature = latest_dht_sensor.temperature
    #     latest_ir_sensor = IrSensor.objects.latest('timestamp')
    #     latest_status = latest_ir_sensor.status
    #
    #     context = {
    #         'latest_temperature': latest_temperature,
    #         'latest_status': latest_status
    #     }
    #
    #     return render(request, 'aiot_status.html', context)