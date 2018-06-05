from django.db import models

# Create your models here.
def job():
    date_created = models.DateTimeField(verbose_name="Date Listed", blank=False, null=False)
    decription = models.CharField(blank=False, null=False)
