from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class bankreq(models.Model):
    Hospital_Name = models.CharField(max_length=100, primary_key=True)
    Address = models.CharField(max_length=100)
    contact = models.IntegerField(max_length=10)
    Units_of_A_Positive = models.IntegerField(max_length=2)
    Units_of_A_Negative = models.IntegerField(max_length=2)
    Units_of_B_Positive = models.IntegerField(max_length=2)
    Units_of_B_Negative = models.IntegerField(max_length=2)
    Units_of_O_Positive = models.IntegerField(max_length=2)
    Units_of_O_Negative = models.IntegerField(max_length=2)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.Hospital_Name

    def get_absolute_url(self):
        return reverse('bank-detail', kwargs={'pk': self.pk})


class bank(models.Model):
    Hospital_Name = models.CharField(max_length=100, primary_key=True)
    Address = models.CharField(max_length=100)
    contact = models.IntegerField(max_length=10)
    Units_of_A_Positive = models.IntegerField(max_length=2)
    Units_of_A_Negative = models.IntegerField(max_length=2)
    Units_of_B_Positive = models.IntegerField(max_length=2)
    Units_of_B_Negative = models.IntegerField(max_length=2)
    Units_of_O_Positive = models.IntegerField(max_length=2)
    Units_of_O_Negative = models.IntegerField(max_length=2)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.Hospital_Name

