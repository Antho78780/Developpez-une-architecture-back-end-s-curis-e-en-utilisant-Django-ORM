from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
   autorisations_choice = [
      ("MA", "managment_team"),
      ("SA", "sales_team"),
      ("SU", "support_team")
   ]
   autorisations = models.CharField(choices=autorisations_choice, default="MA")

