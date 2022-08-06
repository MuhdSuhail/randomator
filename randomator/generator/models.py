from django.db import models


class RandomPassword(models.Model):
    """
    Model class for saving password and site where password is used
    """
    password = models.CharField(max_length=200)
    description = models.TextField(max_length=200)
    created_date = models.DateTimeField('date created')
