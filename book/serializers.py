from rest_framework import serializers
from . import models

        
       
        
class BookSerializer(serializers.ModelSerializer):
    genre = serializers.PrimaryKeyRelatedField(queryset=models.Genre.objects.all())
    author = serializers.PrimaryKeyRelatedField(queryset=models.Author.objects.all())
    image=serializers.URLField(max_length=1000,required=False)
    isbn=serializers.URLField(max_length=1000,required=False)
    class Meta:
        model = models.Book
        fields = '__all__'

    def get_review_count(self, obj):
        return obj.review_set.count()  # Count the number of related reviews
class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Review
        fields = '__all__'
