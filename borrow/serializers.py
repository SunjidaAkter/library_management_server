from rest_framework import serializers
from . import models
# from django.contrib.auth.models import Usera
class BorrowSerializer(serializers.ModelSerializer):
    borrower = serializers.PrimaryKeyRelatedField(queryset=models.UserAccount.objects.all())
    book = serializers.PrimaryKeyRelatedField(queryset=models.Book.objects.all())
    class Meta:
        model = models.Borrow
        fields = "__all__"
      