"""
Definition of models.
"""

from django.db import models

# Create your models here.

class test(models.Model):
    """
    Description: Model Description
    """
    nom = models.CharField(max_length=250)
    prenom = models.CharField(max_length=250)
    picture = models.FileField(upload_to="picture")
    active = models.BooleanField(default=True)

    class Meta:
        pass