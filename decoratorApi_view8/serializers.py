from rest_framework import serializers
from decoratorApi_view8.models import Book8


class SerializersBook8(serializers.ModelSerializer):
    class Meta:
        model = Book8
        fields = '__all__'