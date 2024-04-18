from rest_framework import viewsets, status
from rest_framework import serializers
from rest_framework.response import Response
from vandyapi.models import Medication

class MedicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medication
        fields = ['medication_id', 'name', 'generic_name', 'route', 'outpatients', 'inpatients', 'patients']

class MedicationSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medication
        fields = ['medication_id', 'name']

class MedicationViewSet(viewsets.ViewSet):

    def list(self, request):
        medications = Medication.objects.all()
        serializer = MedicationSerializer(medications, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        try:
            medication = Medication.objects.get(medication_id=pk)
            serializer = MedicationSerializer(medication)
            return Response(serializer.data)
        except Medication.DoesNotExist:
            return Response({"error": "Medication not found."}, status=status.HTTP_404_NOT_FOUND)

    def create(self, request):
        medication = Medication.objects.create(
            medication_id=request.data.get('medication_id'),
            name=request.data.get('name'),
            generic_name=request.data.get('generic_name'),
            route=request.data.get('route'),
            outpatients=request.data.get('outpatients'),
            inpatients=request.data.get('inpatients'),
            patients=request.data.get('patients')
        )
        serializer = MedicationSerializer(medication, context={'request': request})
        return Response(serializer.data, status=status.HTTP_201_CREATED)