from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.generic import View
from django.views.decorators.csrf import csrf_exempt

import json

#-- TemplateView
class AIoTStatus(View):
    def get(self, request):
        return render(request, 'aiot_status.html')

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request):
        data = json.loads(request.body.decode('utf-8'))
        aiot_temperature = data['aiot_temperature']
        aiot_ir_state = data['aiot_ir_state']
        aiot_context = {'aiot_temperature': aiot_temperature, 'aiot_ir_state': aiot_ir_state}
        print(aiot_context)

        return render(request, 'aiot_status.html', context=aiot_context, content_type='application/json')