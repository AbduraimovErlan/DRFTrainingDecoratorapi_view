from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from decoratorApi_view16.models import Book16
from decoratorApi_view16.serializers import SerializersBook16


@api_view(['GET', 'POST'])
def Book_list_create_api_view16(request):
    if request.method == 'GET':
        books = Book16.objects.all()
        serializers = SerializersBook16(books, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)

    if request.method == 'POST':
        serializers = SerializersBook16(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def Book_retrieve_update_delete_api_view(request, id):
    try:
        books = Book16.objects.get(id=id)
    except Book16.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializers = SerializersBook16(books)
        return Response(serializers.data, status=status.HTTP_200_OK)

    if request.method == 'PUT':
        serializers = SerializersBook16(books, data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_200_OK)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        books.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
