from django.db import models
from users.models import Users
import uuid
from django.utils.timezone import now

# Create your models here.
class Employee(models.Model):
    id = models.UUIDField(auto_created=True,default=uuid.uuid4,primary_key=True)
    first_name = models.CharField()
    last_name = models.CharField()
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    isActive = models.BooleanField(default=True)
    isDeleted = models.BooleanField(default=False)
    salary = models.IntegerField()
    ROLE_CHOICES = [
        ('Dev', 'Developer'),
        ('HR', 'Human Resources'),
        ('BA', 'Business Analyst'),
        ('PM', 'Project Manager'),
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    enrollTime = models.DateField(default=now)
    userid = models.ForeignKey(Users, on_delete=models.CASCADE,null=True, blank=True,db_column='userid')
    # createdAt = models.DateTimeField(auto_now_add=True)
    # updatedAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.role}"