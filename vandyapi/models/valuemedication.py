from django.db import models

class ValueSetMedication(models.Model):
    value_set = models.ForeignKey("ValueSet", on_delete=models.CASCADE, null=True)
    medication = models.ForeignKey("Medication", on_delete=models.CASCADE, null=True)
