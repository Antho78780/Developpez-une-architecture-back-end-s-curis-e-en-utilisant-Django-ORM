from django.db import models
from authentication.models import User

class Customer(models.Model):
    firstname = models.CharField(max_length=25)
    lastname = models.CharField(max_length=25)
    email = models.CharField(max_length=100)
    mobile = models.CharField(max_length=20)
    compagny_name = models.CharField(max_length=100)
    sales_contact = models.ForeignKey(User, on_delete=models.CASCADE)
    date_created = models.DateField(auto_now_add=True)
    date_updated = models.DateField(auto_now=True)


class Contract(models.Model):
    amount = models.FloatField()
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    status = models.BooleanField()
    payment_due = models.DateTimeField()
    date_created = models.DateField(auto_now_add=True)
    date_updated = models.DateField(auto_now=True)


class Event(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    attendees = models.IntegerField()
    support_contact = models.ForeignKey(User, on_delete=models.CASCADE)
    notes = models.CharField(max_length=300)
    event_date = models.DateTimeField()
    date_created = models.DateField(auto_now_add=True)
    date_updated = models.DateField(auto_now=True)