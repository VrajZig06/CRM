from django.db import models
import uuid
from django.utils import timezone



# Create your models here.
class Users(models.Model):
    id = models.UUIDField(auto_created=True,default=uuid.uuid4,primary_key=True)
    username = models.CharField(max_length=50,unique=True)
    password = models.CharField()
    email = models.CharField()
    company_name = models.CharField(unique=True)
    isActive = models.BooleanField(default=True)
    isDeleted = models.BooleanField(default=False)
    accessToken = models.TextField(editable=True)
    lastLogin = models.DateTimeField(default=timezone.now)

    

    def __str__(self):
        return self.company_name