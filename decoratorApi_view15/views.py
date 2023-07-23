from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from decoratorApi_view15.models import Book15
from decoratorApi_view15.serializers import SerializersBook15


@api_view(['GET', 'POST'])
def Book_list_create_api_veiw15(request):
    if request.method == 'GET':
        books = Book15.objects.all()
        serializers = SerializersBook15(books, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)

    if request.method == 'POST':
        serializers = SerializersBook15(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def Book_retrieve_update_delete_api_view15(reqeust, id):
    try:
        books = Book15.objects.get(id=id)
    except Book15.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if reqeust.method == 'GET':
        serializers = SerializersBook15(books)
        return Response(serializers.data, status=status.HTTP_200_OK)

    if reqeust.method == 'PUT':
        serializers = SerializersBook15(books, data=reqeust.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_200_OK)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    if reqeust.method == 'DELETE':
        books.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

