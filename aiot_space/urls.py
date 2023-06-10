from django.urls import path
from aiot_space import views

app_name = 'aiot_space'
urlpatterns = [

    # Example: /aiot_space/
    path('', views.AIoTStatus.as_view(), name='status'),

    # Example: /aiot_space/consumption
    # path('consumption/', views.AIoTConsumption.as_view(), name='aiot_consumption'),
]