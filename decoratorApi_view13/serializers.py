from rest_framework import serializers
from decoratorApi_view13.models import Book13



class SerializersBook13(serializers.ModelSerializer):
    class Meta:
        model = Book13
        fields = '__all__'