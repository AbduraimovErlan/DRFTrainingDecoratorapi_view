from rest_framework import serializers
from decoratorApi_View26.models import Book26


class SerializersBook26(serializers.ModelSerializer):
    class Meta:
        model = Book26
        fields = '__all__'