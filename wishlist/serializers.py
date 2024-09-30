from rest_framework import serializers
from . import models
from book.serializers import BookSerializer
# from django.contrib.auth.models import Usera
class WishlistSerializer(serializers.ModelSerializer):
    borrower = serializers.PrimaryKeyRelatedField(queryset=models.UserAccount.objects.all())
    book = serializers.PrimaryKeyRelatedField(queryset=models.Book.objects.all())
    class Meta:
        model = models.Wishlist
        fields = '__all__'