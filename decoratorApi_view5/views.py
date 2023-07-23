from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from decoratorApi_view5.serializers import SerializersBook5
from decoratorApi_view5.models import Book5




@api_view(['GET', 'POST'])
def Book_list_create_api_view5(request):
    if request.method == 'GET':
        books = Book5.objects.all()
        serializers = SerializersBook5(books, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)

    if request.method == 'POST':
        serializers = SerializersBook5(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def Book_retrieve_update_delete_api_view5(request, id):
    try:
        books = Book5.objects.get(id=id)
    except Book5.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializers = SerializersBook5(books)
        return Response(serializers.data, status=status.HTTP_200_OK)


    if request.method == 'PUT':
        serializers = SerializersBook5(books, data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_200_OK)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


    if request.method == 'DELETE':
        books.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)