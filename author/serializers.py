from rest_framework import serializers
from . import models

        
       
        
class AuthorSerializer(serializers.ModelSerializer):
    image = serializers.URLField(max_length=500,required=False)
    class Meta:
        model = models.Author
        fields = '__all__'

   