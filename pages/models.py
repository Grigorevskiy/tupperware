from django.db import models


# Create your models here.
class Faq(models.Model):
    question = models.TextField(verbose_name= 'question')
    answer = models.TextField(verbose_name='answer')
