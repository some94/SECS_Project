from django.contrib.admin import action
from django.shortcuts import render
from django.views.generic import TemplateView

#-- TemplateView
class IoTStatus(TemplateView):
    template_name = 'iot_status.html'

    # @action(methods=['POST'], detail=True)
    # def get_data(self, request, **kwargs):
    #     temp = request.data.get('temperature')
