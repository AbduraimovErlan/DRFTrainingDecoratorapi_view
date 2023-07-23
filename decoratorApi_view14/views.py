from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from decoratorApi_view14.serializers import SerializersBook14
from decoratorApi_view14.models import Book14




@api_view(['GET', 'POST'])
def Book_list_create_api_view14(request):
    if request.method == 'GET':
        books = Book14.objects.all()
        serializers = SerializersBook14(books, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)


    if request.method == 'POST':
        serializers = SerializersBook14(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def Book_retrieve_update_delete_api_view14(request, id):
    try:
        books = Book14.objects.get(id=id)
    except Book14.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializers = SerializersBook14(books)
        return Response(serializers.data, status=status.HTTP_200_OK)

    if request.method == 'PUT':
        serializers = SerializersBook14(books, data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_200_OK)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        books.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)