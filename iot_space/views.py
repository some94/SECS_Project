from django.shortcuts import render
from django.views.generic import TemplateView

#-- TemplateView
class IoTStatus(TemplateView):
    template_name = 'iot_status.html'

# class IoTConsumption:
