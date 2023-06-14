from django.contrib.admin import action
from django.http import HttpResponse, JsonResponse, HttpRequest
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.generic import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView
import json

temp = 10
detect = 'X'
#-- TemplateView
class IoTStatus(View):
    def get(self, request):
        # pointId = Point.objects.all()
        # return render('iot_status.html', pointId)
        # return render(request, 'iot_status.html')
        return render(request, 'iot_status.html', {'temperature': temp, 'detection': detect})
    # def ListFunc(request):
    #     datas = SangTab.objects.all()
    #     return render(request, 'list.html', {'sangpums': datas})

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    # temp = Temperture(temp=data1)
    # temp.save()
    def post(self, request):
        json_data = json.loads(request.body)
        temp = json_data.get('temperature')
        detect = json_data.get('detection')
        return JsonResponse(request, 'iot_status.html', {'temperature': temp, 'detection': detect})