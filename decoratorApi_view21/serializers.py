from rest_framework import serializers
from decoratorApi_view21.models import Book21


class SerializersBook21(serializers.ModelSerializer):
    class Meta:
        model = Book21
        fields = '__all__'