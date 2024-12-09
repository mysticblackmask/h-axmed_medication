from django.db import models

class MedicationSKU(models.Model):
    id = models.AutoField(primary_key=True)
    medication_name = models.CharField(max_length=100,blank=True, null=True)
    formulation = models.CharField(max_length=100,blank=True, null=True)
    dosage = models.IntegerField()
    unit = models.CharField(max_length=10,blank=True, null=True)
    phonetic_name = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        unique_together = ('phonetic_name', 'formulation', 'dosage', 'unit')

    def save(self, *args, **kwargs):
        self.phonetic_name = soundex(self.medication_name)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.medication_name} {self.formulation} {self.dosage}{self.unit}"
