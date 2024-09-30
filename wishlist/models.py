from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
from django.db import models
from user_account.models import UserAccount
from book.models import Book
# from django.contrib.auth.models import User
# Create your models here.


class Wishlist(models.Model):
    borrower = models.ForeignKey(UserAccount, on_delete = models.CASCADE)
    book = models.ForeignKey(Book, on_delete = models.CASCADE)
    created_on = models.DateField(auto_now_add=True)
    

    def __str__(self):
        return f"User : {self.customer.user.first_name} , Menu Item : {self.menu.title}"
    