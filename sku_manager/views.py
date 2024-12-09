# views.py
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import MedicationSKU
from .serializers import MedicationSKUSerializer

@api_view(['GET'])
def read_skus(request):
    if request.method == 'GET':
        skus = MedicationSKU.objects.all()
        if not skus.exists():
            return Response({'message': 'No SKUs found'}, status=404)
        serializer = MedicationSKUSerializer(skus, many=True)
        return Response(serializer.data)

@api_view(['POST'])
def create_sku(request):
    if request.method == 'POST':
        serializer = MedicationSKUSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)