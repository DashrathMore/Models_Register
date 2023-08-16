from django.db import models

# Create your models here.
class Topic (models.Model):
    Topic_name=models.CharField(max_length=100, primary_key=True)

class WebPage(models.Model):
    Topic_name=models.ForeignKey(Topic, on_delete=models.CASCADE)
    Name=models.CharField(max_length=100)
    url=models.URLField()

class Record(models.Model):
    Name=models.ForeignKey(WebPage, on_delete=models.CASCADE)
    Date=models.DateField()
    Author=models.CharField(max_length=100)