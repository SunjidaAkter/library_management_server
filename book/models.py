from django.db import models
from genre.models import Genre
from author.models import Author
from django.contrib.auth.models import User
# Create your models here.
class Book(models.Model):
    isbn = models.CharField(max_length=13, unique=True, blank=False, null=False)
    title=models.CharField(max_length=50)
    description=models.CharField(max_length=500)
    price=models.IntegerField()
    quantity=models.IntegerField()
    image=models.URLField(max_length=1000,blank=True,null=True)
    genre=models.ForeignKey(Genre,on_delete=models.CASCADE)
    author=models.ForeignKey(Author,on_delete=models.CASCADE)
    def __str__(self) -> str:
        return self.title
    
class Review(models.Model):
    reviewer = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    title = models.CharField(max_length=50, null=True, blank=True)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(default=1)  # Ensure rating is an integer field

    def __str__(self):
        return f"User: {self.reviewer.username} ; Book: {self.book.title}"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.book.update_rating()  # Update book rating whenever a review is saved
        self.book.update_reviews_count() 