from rest_framework import viewsets
from . import models
from . import serializers
from book.models import Book
from user_account.models import UserAccount
from django.shortcuts import get_object_or_404
from rest_framework.exceptions import ValidationError
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
class BorrowViewSet(viewsets.ModelViewSet):
    queryset = models.Borrow.objects.select_related('book').all()
    serializer_class = serializers.BorrowSerializer
    http_method_names = ['get', 'post', 'patch', 'delete']
    def get_queryset(self):
        borrower_id = self.request.query_params.get('borrower_id')

        # If borrower_id is not provided, return the full queryset
        if borrower_id is None:
            return super().get_queryset()

        # Check if borrower_id is a valid integer
        if not borrower_id.isdigit():
            raise ValidationError({"borrower_id": "Invalid Borrower ID. It must be a number."})

        # Filter queryset by borrower_id
        return super().get_queryset().filter(borrower_id=int(borrower_id))
    def send_return_email(self, user_account, borrow, subject, template):
        message = render_to_string(template, {
            'user_account': user_account,
            'borrow': borrow,
        })
        send_email = EmailMultiAlternatives(subject, '', to=[user_account.user.email])
        send_email.attach_alternative(message, "text/html")
        send_email.send()
    def perform_update(self, serializer):
        # Save the updated instance first
        instance = serializer.save()

        # Check if the borrow status has changed to "Returned"
        if instance.borrow_status == "Returned":
            # Get the associated book and user
            book = instance.book
            user_account = instance.borrower

            # Increase the book quantity by 1
            book.quantity += 1
            book.save()

            # Refund the user's balance
            user_account.balance += book.price
            user_account.save()

            # Optionally, send a return confirmation email
            self.send_return_email(user_account, instance, "Book Return Confirmation", "return_email.html")



    def send_borrow_email(self, user_account, borrow, subject, template):
        message = render_to_string(template, {
            'user_account': user_account,
            'borrow': borrow,
        })
        send_email = EmailMultiAlternatives(subject, '', to=[user_account.user.email])
        send_email.attach_alternative(message, "text/html")
        send_email.send()

    @method_decorator(login_required(login_url='/user_account/login/'))
    def perform_create(self, serializer):
        request = self.request
        pk = self.kwargs.get('pk')  # Get the book ID from the request path

        # Retrieve the book and user account
        book = get_object_or_404(Book, pk=pk)
        user_account = UserAccount.objects.get(user=request.user)

        # Check if the book is available in stock
        if book.quantity <= 0:
            raise ValidationError({"error": "This book is currently out of stock."})

        # Check if the user has enough balance to borrow the book
        if user_account.balance < book.price:
            raise ValidationError({"error": "Insufficient balance to borrow this book."})

        # Deduct the price of the book from the user's balance
        user_account.balance -= book.price
        user_account.save()

        # Decrease the book quantity by 1
        book.quantity -= 1
        book.save()

        # Optionally, you can send a confirmation email to the user
        self.send_borrow_email(user_account, serializer.instance, "Book Borrowing Message", "borrow_email.html")

        # Create the borrow record with the updated balance
        serializer.save(borrower=user_account, book=book, balance_after_borrow=user_account.balance)