from rest_framework import serializers
from decoratorApi_view19.models import Book19


class SerializersBook19(serializers.ModelSerializer):
    class Meta:
        model = Book19
        fields = '__all__'