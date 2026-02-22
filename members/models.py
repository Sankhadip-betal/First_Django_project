from django.db import models

# Createmodels here.
class Member(models.Model):
    firstname=models.CharField(max_length=200)
    lastname=models.CharField(max_length=200)
    