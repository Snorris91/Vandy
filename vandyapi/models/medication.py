from django.db import models

class Medication(models.Model):
    medication_id = models.IntegerField(null=True, blank=True)
    name = models.CharField(max_length=150)
    generic_name = models.CharField(max_length=50)
    route = models.CharField(max_length=50)
    outpatients = models.IntegerField(null=True, blank=True)
    inpatients = models.IntegerField(null=True, blank=True)
    patients = models.IntegerField(null=True, blank=True)
    values = models.ManyToManyField(
        "ValueSet",
        through='ValueMedication',
        related_name="medications"
    )
