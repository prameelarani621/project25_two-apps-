from django.db import models

# Create your models here.

class Topic(models.Model):
    topic_name=models.CharField(max_length=100,primarekey=True)


class Webpage(models.Model):
    topic_name=models.ForeignKey