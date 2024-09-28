from django.shortcuts import render
from rest_framework import viewsets
from . import models
from . import serializers
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend


 
class BookViewset(viewsets.ModelViewSet):
    queryset = models.Book.objects.all()
    serializer_class = serializers.BookSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['name','genre__name']
    # pagination_class = BookPagination
    search_fields = [ 'name','genre__name']
    
class ReviewsForSpecificBook(filters.BaseFilterBackend):
    def filter_queryset(self, request, query_set, view):
        book_id = request.query_params.get("book_id")
        if book_id:
            return query_set.filter(book = book_id)
        return query_set    
class ReviewViewset(viewsets.ModelViewSet):
    queryset = models.Review.objects.all()
    serializer_class = serializers.ReviewSerializer
    filter_backends = [ReviewsForSpecificBook]