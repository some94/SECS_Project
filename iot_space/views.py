from django.http import HttpResponse
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.generic import View
from django.views.decorators.csrf import csrf_exempt
from iot_space.models import DhtSensor, IrSensor

# # 소켓 통신 부분
# import socket, time
#
# host = 'localhost'
# port = 8000
#
# import json
#
# server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# server_socket.bind((host, port))
# server_socket.listen()
#
# client_socket, client_address = server_socket.accept()
# data = client_socket.recv(1024)
# decoded_data = data.decode()
# payload = json.loads(decoded_data)
#
# # 이 값을 html로 전송
# iot_temperature = payload[iot_temperature]
# iot_state = payload[iot_ir_state]


class IoTStatus(View):
    def get(self, request):
        iot_context = request.session.get('iot_context')
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

        return render(request, 'iot_status.html', context=iot_context)