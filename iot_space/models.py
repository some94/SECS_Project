from django.db import models
from django.utils import timezone

# 온습도 센서
class DhtSensor(models.Model):
    name = models.CharField(max_length=50)
    timestamp = models.DateTimeField(default=timezone.now)
    temperature = models.FloatField(verbose_name='Temperature')
    humidity = models.FloatField(verbose_name='Humidity')

    def __str__(self):
        return f'Temperature: {self.temperature}, Humidity: {self.humidity}'

    # 현재 시간을 기준으로 내림차순 정렬
    class Meta:
        ordering = ['-timestamp']


# 적외선 센서
class IrSensor(models.Model):
    name = models.CharField(max_length=50)
    timestamp = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=50, verbose_name='Motion Detected')

    def __str__(self):
        return f'Motion Detected: {self.status}'

    class Meta:
        ordering = ['-timestamp']


# 쿨링팬
class Fan(models.Model):
    name = models.CharField(max_length=50)
    runtime = models.DurationField(verbose_name='Fan Runtime')
    fan_consumption = models.FloatField(verbose_name='Fan Consumption', blank=True)
    daily = models.CharField(max_length=20)
    month = models.CharField(max_length=20)


# 전구
class Bulb(models.Model):
    name = models.CharField(max_length=50)
    runtime = models.DurationField(verbose_name='Bulb Runtime')
    bulb_consumption = models.FloatField(verbose_name='Bulb Consumption', blank=True)
    daily = models.CharField(max_length=20)
    month = models.CharField(max_length=20)


# IoT Space의 일월별 전력 소비량
class Consumption(models.Model):
    daily_consumption = models.FloatField(verbose_name='Daily Consumption', null=True)
    monthly_consumption = models.FloatField(verbose_name='Month Consumption', null=True)
