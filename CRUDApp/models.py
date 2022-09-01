from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class Login(AbstractUser):
    is_user = models.BooleanField(default=False)

class Profile(models.Model):
     user = models.ForeignKey(Login, on_delete=models.CASCADE, related_name='user')
     phone_no = models.CharField(max_length=50)
     photo = models.ImageField(upload_to='media/uploads', blank=True)
     Bio = models.CharField(max_length=200)
     SocialMediaLinks = models.CharField(max_length=100)
     CourseName = models.CharField(max_length=100)
     CourseDuration = models.CharField(max_length=100)
     YearOfPassing = models.CharField(max_length=50)
     Percentage = models.CharField(max_length=10)
     CompanyNameORInternshipName = models.CharField(max_length=200)
     DurationOfJobORInternship = models.CharField(max_length=100)
     YourJobDescription = models.CharField(max_length=500)
     SallaryORStipendInLPA = models.CharField(max_length=50)
     ProjectName = models.CharField(max_length=200)
     DurationOfProject = models.CharField(max_length=100)
     ProjectDescription = models.CharField(max_length=1000)
     YourRoleInProject = models.CharField(max_length=100)
