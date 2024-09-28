from rest_framework import viewsets
from . import models
from . import serializers
from rest_framework import filters, pagination
from django_filters.rest_framework import DjangoFilterBackend


    

class AuthorViewset(viewsets.ModelViewSet):
    queryset = models.Author.objects.all()
    serializer_class = serializers.AuthorSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['name','email']
    search_fields = [ 'name', 'email']
    
