from django.db import models

class ValueSet(models.Model):
    value_id = models.CharField(max_length=100, unique=True)
    value_name = models.CharField(max_length=150)