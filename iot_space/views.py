from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.generic import View
from django.views.decorators.csrf import csrf_exempt

import json

class IoTStatus(View):
    def get(self, request):
        return render(request, 'iot_status.html')

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request):
        data = json.loads(request.body.decode('utf-8'))
        iot_temperature = data['iot_temperature']
        iot_iot_ir_state = data['iot_ir_state']
        iot_context = {'iot_temperature': iot_temperature, 'iot_ir_state': iot_iot_ir_state}
        print(iot_context)

        return render(request, 'iot_status.html', context=iot_context, content_type='application/json')