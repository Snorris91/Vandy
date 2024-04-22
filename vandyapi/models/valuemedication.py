from django.db import models

class ValueMedication(models.Model):
    valueset = models.ForeignKey("ValueSet", on_delete=models.CASCADE, related_name="medication_values")
    medication = models.ForeignKey("Medication", on_delete=models.CASCADE, related_name="value_medications")
