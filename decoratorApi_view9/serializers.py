from rest_framework import serializers
from decoratorApi_view9.models import Book9


class SerializersBook9(serializers.ModelSerializer):
    class Meta:
        model = Book9
        fields = '__all__'