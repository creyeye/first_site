from django.db import models

class Shishka(models.Model):
    title = models.CharField(max_length=123)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=6)
    strength = models.CharField(max_length=123)
    sort = models.CharField(max_length=123)