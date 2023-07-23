from rest_framework import serializers
from decoratorApi_view15.models import Book15


class SerializersBook15(serializers.ModelSerializer):
    class Meta:
        model = Book15
        fields = '__all__'