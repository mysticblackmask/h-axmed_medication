from rest_framework import serializers
from .models import MedicationSKU

class MedicationSKUSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicationSKU
        fields = ['id', 'medication_name', 'formulation', 'dosage', 'unit']

    def validate_dosage(self, value):
        if value <= 0:
            raise serializers.ValidationError("Dosage must be a positive number.")
        return value

    def validate_formulation(self, value):
        if not isinstance(value, str):
            raise serializers.ValidationError("Formulation must be a string.")
        if any(char.isdigit() for char in value):
            raise serializers.ValidationError("Formulation cannot contain numbers.")
        return value

    def validate_unit(self, value):
        if not isinstance(value, str):
            raise serializers.ValidationError("Unit must be a string and cannot be a number.")
        if any(char.isdigit() for char in value):
            raise serializers.ValidationError("Unit cannot contain numbers.")
        return value
