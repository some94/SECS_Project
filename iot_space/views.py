from django.http import HttpResponse
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.generic import View
from django.views.decorators.csrf import csrf_exempt
from iot_space.models import DhtSensor, IrSensor

import json

class IoTStatus(View):
    def get(self, request):
        iot_context = request.session.get['iot_context']
        if iot_context:
            context = {'iot_context': iot_context}
            return render(request, 'iot_status.html', context)
        else:
            return HttpResponse('Session value not found.')

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request):
        data = json.loads(request.body.decode('utf-8'))
        iot_temperature = data['iot_temperature']
        iot_ir_state = data['iot_ir_state']
        iot_context = {'iot_temperature': iot_temperature, 'iot_ir_state': iot_ir_state}
        request.session['iot_context'] = iot_context

        return render(request, 'iot_status.html', context=iot_context, content_type='application/json')

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
    #     return render(request, 'iot_status.html', context)
