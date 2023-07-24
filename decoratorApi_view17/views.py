from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from decoratorApi_view17.models import Book17
from decoratorApi_view17.serializers import SerializersBook17



@api_view(['GET', 'POST'])
def Book_list_create_api_view(request):
    if request.method == 'GET':
        books = Book17.objects.all()
        serializers = SerializersBook17(books, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)

    if request.method == 'POST':
        serializers = SerializersBook17(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def Book_retrieve_update_delete_api_view(request, id):
    try:
        books = Book17.objects.get(id=id)
    except Book17.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializers = SerializersBook17(books)
        return Response(serializers.data, status=status.HTTP_200_OK)

    if request.method == 'PUT':
        serializers = SerializersBook17(books, data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_200_OK)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


    if request.method == 'DELETE':
        books.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)