from django.db import models
# Create your models here.
GENDER_TYPE=(
    ('Male','Male'),
    ('Female','Female'),
)
class Author(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(unique=True)
    nationality=models.CharField(max_length=100)
    bio=models.TextField(max_length=500)
    gender = models.CharField(max_length=10,choices=GENDER_TYPE)
    image=models.URLField(max_length=500)
    slug=models.SlugField(max_length=100,unique=True)
    def __str__(self) -> str:
        return self.name