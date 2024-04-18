from rest_framework import viewsets, status
from rest_framework import serializers
from rest_framework.response import Response
from vandyapi.models import Medication, ValueSet
from vandyapi.views import MedicationSimpleSerializer


class ValueSerializer(serializers.ModelSerializer):
    medication = MedicationSimpleSerializer
    class Meta:
        model = ValueSet
        fields = ['value_id', 'value_name', 'medication']

class ValueViewSet(viewsets.ViewSet):

    def list(self, request):
        value = ValueSet.objects.all()
        serializer = ValueSerializer(value, many=True, context={'request': request})
        return Response(serializer.data)
