from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from .models import Maqola, Rasm

class MaqolaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Maqola
        fields = ('id', 'maqola', 'sarlavha')
    def validate_sarlavha(self, value):
        if len(value) < 10:
            raise ValidationError(detail="Sarlavha kamida 10 ta harf bo'lsin")
        return value

class RasmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rasm
        fields = ('id', 'maqola_id', 'rasm')
    def validate_rasm(self, qiymat):
        if not qiymat.endswith('.jpg'):
            raise ValidationError(detail="To'g'ri formatda rasm qo'shing")
        return qiymat