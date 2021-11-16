from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .models import Maqola, Rasm
from .serializers import MaqolaSerializer, RasmSerializer

class MaqolaViewSet(ModelViewSet):
    queryset = Maqola.objects.all()
    serializer_class = MaqolaSerializer
    @action(detail=True, methods=['GET'])
    def rasm(self, request, *args, **kwargs):
        maqola = self.get_object()
        serializer = RasmSerializer(maqola.rasm_set.all(), many=True)
        return Response(serializer.data)
    @action(detail=True, methods=['POST'], url_path='rasm-qosh')
    def rasm_qosh(self, request, *args, **kwargs):
        serializer = RasmSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)

class RasmViewSet(ModelViewSet):
    queryset = Rasm.objects.all()
    serializer_class = RasmSerializer
    @action(detail=True, methods=['GET'])
    def maqola(self, request, *args, **kwargs):
        rasm = self.get_object()
        maqola = Maqola.objects.get(id=rasm.maqola_id.id)
        serializer = MaqolaSerializer(maqola)
        return Response(serializer.data)
