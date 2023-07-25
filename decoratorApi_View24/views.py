from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from decoratorApi_View24.models import Book24
from decoratorApi_View24.serializers import SerializersBook24


@api_view(['GET', 'POST'])
def Book_list_create_api_view24(request):
    if request.method == 'GET':
        books = Book24.objects.all()
        serializers = SerializersBook24(books, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)

    if request.method == 'POST':
        serializers = SerializersBook24(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def Book_retrieve_update_delete_api_view24(reqeust, id):
    try:
        books = Book24.objects.get(id=id)
    except Book24.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if reqeust.method == 'GET':
        serializers = SerializersBook24(books)
        return Response(serializers.data, status=status.HTTP_200_OK)

    if reqeust.method == 'PUT':
        serializers = SerializersBook24(books, data=reqeust.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_200_OK)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    if reqeust.method == 'DELETE':
        books.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

