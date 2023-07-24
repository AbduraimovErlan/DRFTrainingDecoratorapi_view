from rest_framework import serializers
from decoratorApi_view17.models import Book17



class SerializersBook17(serializers.ModelSerializer):
    class Meta:
        model = Book17
        fields = '__all__'