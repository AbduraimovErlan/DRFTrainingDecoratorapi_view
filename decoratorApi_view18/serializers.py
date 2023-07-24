from rest_framework import serializers
from decoratorApi_view18.models import Book18



class SerializersBook18(serializers.ModelSerializer):
    class Meta:
        model = Book18
        fields = '__all__'