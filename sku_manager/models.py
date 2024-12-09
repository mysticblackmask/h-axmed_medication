from django.db import models
from django.db.models import Q
from fuzzywuzzy import fuzz

class MedicationSKU(models.Model):
    id = models.AutoField(primary_key=True)
    medication_name = models.CharField(max_length=100, blank=True, null=True)
    formulation = models.CharField(max_length=100, blank=True, null=True)
    dosage = models.IntegerField()
    unit = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        unique_together = ('medication_name', 'formulation', 'dosage', 'unit')

    def __str__(self):
        return f"{self.medication_name} {self.formulation} {self.dosage}{self.unit}"

     def fuzzy_unique(name, formulation, dosage, unit, threshold=90):
        skus = MedicationSKU.objects.filter(
            formulation__iexact=formulation,
            dosage=dosage,
            unit__iexact=unit
        )
        for sku in skus:
            similarity = fuzz.ratio(name.lower(), sku.medication_name.lower())
            if similarity >= threshold:
                return True
        return False
