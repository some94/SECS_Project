from django.http import HttpResponse
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.generic import View
from django.views.decorators.csrf import csrf_exempt

import json

#-- TemplateView
class IoTStatus(View):
    def get(self, request):
        return render(request, 'iot_status.html')

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request):
        data = json.loads(request.body.decode('utf-8'))
        temperature = data['temperature']
        iot_ir_state = data['iot_ir_state']
        context = {'temperature': temperature, 'iot_ir_state': iot_ir_state}

        return render(request, 'iot_status.html', context=context)
