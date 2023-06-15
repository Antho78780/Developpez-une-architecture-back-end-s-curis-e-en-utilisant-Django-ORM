from django.db import models

class Customer(models.Model):
    firstname = models.CharField(max_length=25)
    lastname = models.CharField(max_length=25)
    email = models.CharField(max_length=100)
    mobile = models.CharField(max_length=20)
    compagny_name = models.CharField(max_length=100)
    date_created = models.DateField()
    date_updated = models.DateField()


class Contract(models.Model):
    contract_status = models.BooleanField()
    amount = models.IntegerField()
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    date_created = models.DateField()
    date_updated = models.DateField()


class Event(models.Model):
    contract = models.OneToOneField(Contract, on_delete=models.CASCADE)
    date_created = models.DateField()
    date_updated = models.DateField()