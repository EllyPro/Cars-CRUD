from django.db import models
from django.core.validators import MinLengthValidator

# Create your models here.

class Make(models.Model):
    name = models.CharField(max_length=128,
    help_text='The company name of cars',
    validators=[MinLengthValidator(4,'minimum 4 chars')])

    def __str__(self):
        return self.name


class Cars(models.Model):
    nickname = models.CharField(max_length=128,unique=True)
    mileage = models.PositiveIntegerField(null=False)
    comment = models.TextField(blank=True)
    make = models.ForeignKey('Make',on_delete=models.CASCADE,null=False,related_name='cars')

    def __str__(self):
        return self.nickname
