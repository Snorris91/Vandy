from rest_framework import viewsets, status
from rest_framework import serializers
from rest_framework.response import Response
from vandyapi.models import ValueSet


class ValueSerializer(serializers.ModelSerializer):

    class Meta:
        model = ValueSet
        fields = ['id', 'value_id', 'value_name']

class ValueViewSet(viewsets.ViewSet):
    
    def list(self, request):
        values = ValueSet.objects.all()
        serializer = ValueSerializer(values, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        try:
            value = ValueSet.objects.get(pk=pk)
            serializer = ValueSerializer(value)
            return Response(serializer.data)
        except ValueSet.DoesNotExist:
            return Response({"error": "Value not found."}, status=status.HTTP_404_NOT_FOUND)