from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from . import models
from . import serializers
from rest_framework.exceptions import ValidationError

class WishlistViewSet(viewsets.ModelViewSet):
    queryset = models.Wishlist.objects.all()
    serializer_class = serializers.WishlistSerializer

    def get_queryset(self):
        borrower_id = self.request.query_params.get('borrower_id')

        # If borrower_id is not provided, return the full queryset
        if borrower_id is None:
            return super().get_queryset()

        # Check if borrower_id is a valid integer
        if not borrower_id.isdigit():
            raise ValidationError({"borrower_id": "Invalid borrower_id. It must be a number."})

        # Filter queryset by borrower_id
        return super().get_queryset().filter(borrower_id=int(borrower_id))
