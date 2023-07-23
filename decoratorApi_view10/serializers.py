from rest_framework import serializers
from decoratorApi_view10.models import Book10


class SerializersBook(serializers.ModelSerializer):
    class Meta:
        model = Book10
        fields = '__all__'