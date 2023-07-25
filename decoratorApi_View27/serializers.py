from rest_framework import serializers
from decoratorApi_View27.models import Book27


class SerializersBook(serializers.ModelSerializer):
    class Meta:
        model = Book27
        fields = '__all__'