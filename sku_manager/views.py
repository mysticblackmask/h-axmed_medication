from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import MedicationSKU
from .serializers import MedicationSKUSerializer

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

@api_view(['GET'])
def read_skus(request):
    if request.method == 'GET':
        skus = MedicationSKU.objects.all()
        if not skus.exists():
            return Response({'message': 'No SKUs found'}, status=404)
        serializer = MedicationSKUSerializer(skus, many=True)
        return Response(serializer.data)

@swagger_auto_schema(
    method='post',
    request_body=MedicationSKUSerializer,
    responses={201: MedicationSKUSerializer}
)

@api_view(['POST'])
def create_sku(request):
    if request.method == 'POST':
        serializer = MedicationSKUSerializer(data=request.data)
        if serializer.is_valid():
            medication_name = request.data.get('medication_name')
            phonetic_name = soundex(medication_name)
            existing_sku = MedicationSKU.objects.filter(phonetic_name=phonetic_name).first()
            if existing_sku:
                return Response({"error": "Medication name already exists"}, status=status.HTTP_400_BAD_REQUEST)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@swagger_auto_schema(
    method='put',
    request_body=MedicationSKUSerializer,
    responses={
        200: MedicationSKUSerializer,
        400: 'Validation errors',
        404: 'Not found'
    },
    operation_summary="Update a Medication SKU",
    operation_description="Updates the details of an existing Medication SKU using a full update (PUT)."
)

@api_view(['PUT'])
def update_sku(request, pk):
    if request.method == 'PUT':
        try:
            sku = MedicationSKU.objects.get(pk=pk)
            serializer = MedicationSKUSerializer(sku, data=request.data)
            if serializer.is_valid():
                medication_name = request.data.get('medication_name')
                phonetic_name = soundex(medication_name)
                if phonetic_name != sku.phonetic_name:
                    existing_sku = MedicationSKU.objects.filter(phonetic_name=phonetic_name).first()
                    if existing_sku and existing_sku.id != pk:
                        return Response({"error": "Medication name already exists"}, status=status.HTTP_400_BAD_REQUEST)
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except MedicationSKU.DoesNotExist:
            return Response({'message': 'No data found for the given ID'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['DELETE'])
def delete_sku(request, pk):
    if request.method == 'DELETE':
        try:
            sku = MedicationSKU.objects.get(pk=pk)
            sku.delete()
            return Response({'message': 'SKU deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
        except MedicationSKU.DoesNotExist:
            return Response({'message': 'No data found for the given ID'}, status=status.HTTP_404_NOT_FOUND)

@swagger_auto_schema(
    method='post',
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'skus': openapi.Schema(
                type=openapi.TYPE_ARRAY,
                items=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'medication_name': openapi.Schema(type=openapi.TYPE_STRING, description="Name of the medication."),
                        'formulation': openapi.Schema(type=openapi.TYPE_STRING, description="Formulation (e.g., tablet, capsule)."),
                        'dosage': openapi.Schema(type=openapi.TYPE_INTEGER, description="Dosage amount."),
                        'unit': openapi.Schema(type=openapi.TYPE_STRING, description="Unit (e.g., mg)."),
                    },
                    required=['medication_name']
                ),
                description="List of SKUs to be created."
            )
        },
        required=['skus'],
    ),
    responses={
        201: openapi.Response(
            description="List of created SKUs",
            schema=openapi.Schema(
                type=openapi.TYPE_ARRAY,
                items=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'id': openapi.Schema(type=openapi.TYPE_INTEGER, description="ID of the SKU."),
                        'medication_name': openapi.Schema(type=openapi.TYPE_STRING),
                        'formulation': openapi.Schema(type=openapi.TYPE_STRING),
                        'dosage': openapi.Schema(type=openapi.TYPE_INTEGER),
                        'unit': openapi.Schema(type=openapi.TYPE_STRING),
                    }
                )
            )
        ),
        400: "Validation errors or missing required fields",
    },
    operation_summary="Bulk create SKUs",
    operation_description="Create multiple SKUs in a single request by providing an array of SKU objects."
)

@api_view(['POST'])
def bulk_create_skus(request):
    if request.method == 'POST':
        skus = request.data.get('skus', [])
        for sku_data in skus:
            if 'medication_name' not in sku_data:
                return Response({"error": "Each SKU must include 'medication_name'."}, status=status.HTTP_400_BAD_REQUEST)
        phonetic_names = [soundex(sku['medication_name']) for sku in skus]
        existing_skus = MedicationSKU.objects.filter(phonetic_name__in=phonetic_names)
        for sku_data, existing_sku in zip(skus, existing_skus):
            if soundex(sku_data['medication_name']) == existing_sku.phonetic_name:
                return Response({"error": "Duplicate medication names detected."}, status=status.HTTP_400_BAD_REQUEST)
        serializer = MedicationSKUSerializer(data=skus, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)