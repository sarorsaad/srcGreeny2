from django.db import models

# Create your models here.
class Company(models.Model):

    # Fields
    call_us = models.CharField(max_length=30)
    address = models.TextField(max_length=100)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    email = models.TextField(max_length=100)
    name = models.CharField(max_length=30)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    phone_number = models.TextField(max_length=100)
    subtitle = models.CharField(max_length=30)
    tw_link = models.URLField()
    fb_link = models.URLField(null=True, blank=True)
    logo = models.ImageField(upload_to="company/")
    email_us = models.CharField(max_length=30)

    class Meta:
        pass

    def __str__(self):
        return str(self.name)