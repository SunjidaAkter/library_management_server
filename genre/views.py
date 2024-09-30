from rest_framework import viewsets
from . import models
from . import serializers
# Create your views here.
class GenreViewSet(viewsets.ModelViewSet):
    queryset = models.Genre.objects.all()
    serializer_class =  serializers.GenreSerializer
    
    def get_queryset(self):
        queryset = super().get_queryset() 
        return queryset