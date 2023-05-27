from django.db import models
from django.utils import timezone

# 온습도 센서의 현재 상태
class DhtSensor(models.Model):
    name = models.CharField(max_length=50, unique=True)
    timestamp = models.DateTimeField(default=timezone.now())
    temperature = models.FloatField(verbose_name='Temperature')
    humidity = models.FloatField(verbose_name='Humidity')

    def __str__(self):
        return f'Temperature: {self.temperature}, Humidity: {self.humidity}'

    # 현재 시간을 기준으로 내림차순 정렬
    class Meta:
        ordering = ['-timestamp']

# 적외선 센서의 현재 상태
class IrSensor:
    name = models.CharField(max_length=50, unique=True)
    timestamp = models.DateTimeField(default=timezone.now())
    status = models.BooleanField(verbose_name='Motion Detected')

    def __str__(self):
        return f'Motion Detected: {self.status}'

    class Meta:
        ordering = ['-timestamp']

# 쿨링팬의 작동 시간 저장
class Fan:
    name = models.CharField(max_length=50, unique=True)
    timestamp = models.DateTimeField(default=timezone.now())
    status = models.BooleanField(verbose_name='Is Fan On')
    runtime = models.DurationField(verbose_name='Fan Runtime')

    class Meta:
        ordering = ['-timestamp']

# 전구의 작동 시간 저장
class Bulb:
    name = models.CharField(max_length=50, unique=True)
    timestamp = models.DateTimeField(default=timezone.now())
    status = models.BooleanField(verbose_name='Is Bulb On')
    runtime = models.DurationField(verbose_name='Bulb Runtime')

    class Meta:
        ordering = ['-timestamp']

# IoT Space의 일월별 전력 소비량(작성 예정)