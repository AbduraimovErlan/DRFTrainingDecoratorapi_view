from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from decoratorApi_view4.models import Book4
from decoratorApi_view4.serializers import SerializersBook4
from rest_framework import status




@api_view(['GET', 'POST'])
def Book_list_create_api_view4(request):
    if request.method == 'GET':
        books = Book4.objects.all()
        serializers = SerializersBook4(books, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)

    if request.method == 'POST':
        serializers = SerializersBook4(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def Book_retrieve_update_delete_api_view4(request, id):
    try:
        books = Book4.objects.get(id=id)
    except Book4.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializers = SerializersBook4(books)
        return Response(serializers.data, status=status.HTTP_200_OK)


    if request.method == 'PUT':
        serializers = SerializersBook4(books, data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_200_OK)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        books.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)