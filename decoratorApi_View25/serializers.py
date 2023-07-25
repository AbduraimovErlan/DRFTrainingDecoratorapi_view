from rest_framework import serializers
from decoratorApi_View25.models import  Book25

class SerializersBook25(serializers.ModelSerializer):
    class Meta:
        model = Book25
        fields = '__all__'