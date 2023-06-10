from django.shortcuts import render
from django.views.generic import TemplateView

#-- TemplateView
class AIoTStatus(TemplateView):
    template_name = 'aiot_status.html'

# class AIoTConsumption:
