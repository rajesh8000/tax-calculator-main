from django.db import models
from django.urls import reverse
from django.contrib.auth.models import (UserManager,AbstractUser)

class Post(models.Model): # creating class for news to store in database
    title = models.CharField(max_length=100)
    content = models.TextField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('inside-news', args=[str(self.id)])

class Faqs(models.Model): # creating class for faq to store in database
    question = models.CharField(max_length=5000)
    answer = models.TextField()

class User(AbstractUser):
    USERNAME_FIELD='username'
    REQUIRED_FIELD=['first_name','last_name']

    objects = UserManager()
    
    def str(self):
        return self.email

class incomeTaxHistory(models.Model): # creating class to store history in database
    income_amount = models.FloatField()
    deductions_amount = models.FloatField()
    tax_amount = models.FloatField()
    calculation_date = models.DateField()

    def __str__(self):
        return self.tax_amount
    