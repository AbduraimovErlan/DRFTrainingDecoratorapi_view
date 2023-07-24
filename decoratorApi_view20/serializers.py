from rest_framework import serializers
from decoratorApi_view20.models import Book20


class SerializersBook20(serializers.ModelSerializer):
    class Meta:
        model = Book20
        fields = '__all__'