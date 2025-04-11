from django.db import models


class Bb(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField(blank=True,null=True)
    content = models.TextField(blank=True,null=True)
    published=models.DateTimeField(auto_now_add=True)