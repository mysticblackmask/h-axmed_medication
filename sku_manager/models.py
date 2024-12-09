from django.db import models

# Create your models here.

class MedicationSKU(models.Model):
    id = models.AutoField(primary_key=True)
    medication_name = models.CharField(max_length=100,blank=True, null=True)  # Medication name or INN (International Nonproprietary Name)
    formulation = models.CharField(max_length=100,blank=True, null=True)     # Presentation (e.g., Tablet, Capsule)
    dosage = models.IntegerField()                      # Dosage amount
    unit = models.CharField(max_length=10,blank=True, null=True)              # Unit (e.g., mg)

    class Meta:
        unique_together = ('medication_name', 'formulation', 'dosage', 'unit')

    def __str__(self):
        return f"{self.medication_name} {self.formulation} {self.dosage}{self.unit}"
