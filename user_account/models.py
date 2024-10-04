from django.db import models
from django.contrib.auth.models import User
# Create your models here.
ROLE = [
    ('Reader', 'Reader'),
    ('Admin', 'Admin'),

]

class UserAccount(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    image_url = models.URLField(max_length=500, null=True, blank=True) 
    mobile_no = models.CharField(max_length = 12)
    address=models.CharField(max_length=100)
    amount=models.IntegerField(default=0)
    role = models.CharField(choices = ROLE, max_length = 10, default = "Reader")
    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"