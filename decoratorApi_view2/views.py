from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from decoratorApi_view2.models import Book2
from decoratorApi_view2.serializers import SerializersBook2



@api_view(['GET', 'POST'])
def Book_list_create_api_view2(reqeust):
    if reqeust.method == 'GET':
        books = Book2.objects.all()
        serializers = SerializersBook2(books, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)


    if reqeust.method == 'POST':
        serializers = SerializersBook2(data=reqeust.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def Book_retrieve_update_delete2(request, id):
    try:
        books = Book2.objects.get(id=id)
    except Book2.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializers = SerializersBook2(books)
        return Response(serializers.data, status=status.HTTP_200_OK)


    if request.method == 'PUT':
        serializers = SerializersBook2(books, data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_200_OK)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


    if request.method == 'DELETE':
        books.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

