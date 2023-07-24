from rest_framework import serializers
from decoratorApi_view16.models import Book16



class SerializersBook16(serializers.ModelSerializer):
    class Meta:
        model = Book16
        fields = '__all__'