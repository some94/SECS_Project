from django.urls import path
from iot_space import views

app_name = 'iot_space'
urlpatterns = [

    # Example: /iot_space/
    path('', views.IoTStatus.as_view(), name='status'),

]