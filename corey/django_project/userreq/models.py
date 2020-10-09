from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class userreq(models.Model):
    Donor_name = models.CharField(max_length=100, primary_key=True)

    contact = models.IntegerField(max_length=10)
    Age = models.IntegerField(default="")
    Blood_group = models.CharField(max_length=10)
    City = models.CharField(max_length=10)
    Email = models.EmailField(max_length=30)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.Donor_name

    def get_absolute_url(self):
        return reverse('userreq-detail', kwargs={'pk': self.pk})
