from django.db import models

# Create your models here.
class Company(models.Model):
    name=models.CharField(max_length=255)
    description=models.TextField(blank=True)
    website=models.URLField(blank=True)
    street_line1=models.CharField(max_length=255)
    street_line2=models.CharField(max_length=255, blank=True)
    city=models.CharField(max_length=80)
    state=models.CharField(max_length=80)
    zip=models.CharField(max_length=10)

    def __str__(self):
        return self.name