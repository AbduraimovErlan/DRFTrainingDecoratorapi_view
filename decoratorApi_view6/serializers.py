from rest_framework import serializers
from decoratorApi_view6.models import Book6


class SerializersBook6(serializers.ModelSerializer):
    class Meta:
        model = Book6
        fields = '__all__'