from django.db import models
from django.contrib.auth.models import User

# Create your models here.

YEAR_CHOICES = [
        ('1', 'First Year'),
        ('2', 'Second Year'),
        ('3', 'Third Year'),
        ('4', 'Fourth Year'),
    ]

class Department(models.Model):
    department = models.CharField(max_length=50)
    def __str__(self):
        return self.department

class Role(models.Model):
    role = models.CharField(max_length=200)
    def __str__(self):
        return self.role

class UserProfile(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(unique=True, null = True)
    password = models.CharField(max_length=200, null = True)
    is_verified = models.BooleanField(default = False)
    token = models.CharField(max_length=100, default=None)
    last_login = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=False)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    has_module_perms = models.BooleanField(default=False)
    def __str__(self):
        return self.name
    
class EventApplication(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    year = models.CharField(max_length=1, choices=YEAR_CHOICES)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)


class Venue(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class Categorie(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class Event(models.Model):
    title = models.CharField('Title',max_length=200)
    description  = models.TextField('Description')
    organizer = models.ForeignKey(UserProfile, on_delete = models.CASCADE, null=True)
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE)
    venue = models.ForeignKey(Venue, on_delete = models.CASCADE)
    startTime = models.TimeField(blank=False, null=True)
    endTime = models.TimeField(blank=False, null=True)
    startDate = models.DateField(blank=False, null=True)
    endDate = models.DateField(blank=False, null=True)
    chief_guest = models.CharField(max_length = 200, null = True)
    approval = models.BooleanField(default = False)
    def __str__(self):
        return self.title
