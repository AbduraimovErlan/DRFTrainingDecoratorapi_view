from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from decoratorApi_view3.models import Book3
from decoratorApi_view3.serializers import SerializersBook3



@api_view(['GET', 'POST'])
def Book_list_create_api_view3(request):
    if request.method == 'GET':
        books = Book3.objects.all()
        serializers = SerializersBook3(books, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)

    if request.method == 'POST':
        serializers = SerializersBook3(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def Book_retrieve_updata_delete_api_view3(request, id):
    try:
        books = Book3.objects.get(id=id)
    except Book3.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializers = SerializersBook3(books)
        return Response(serializers.data, status=status.HTTP_200_OK)


    if request.method == 'PUT':
        serializers = SerializersBook3(books, data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_200_OK)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        books.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

