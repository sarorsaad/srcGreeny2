from django.db import models
from django_countries.fields import CountryField
from django.contrib.auth.models import User
from utlis.generate_code import generate_code
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User,  related_name= 'user_profile',on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg',upload_to="users/")

    code=models.CharField(max_length=10,default=generate_code)
    code_used= models.BooleanField(default=False)
    active=models.BooleanField(default=False)

def __str__(self):
        return f'{self.user} Profile'


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

DATA_TYPE=(
    ( 'Home','Home'),
    ( 'Office','Office'),
    ( 'Academy','Academy'),
    ( 'Other','Other'),

)


class UserPhoneNumber(models.Model):
    user = models.ForeignKey(User,related_name='user_phone',on_delete=models.CASCADE)
    number = models.CharField(max_length=30)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    image = models.ImageField(upload_to="users/")
    type=models.CharField(choices=DATA_TYPE,max_length=10)




class UserAddress(models.Model):

    # Fields
    region = models.CharField(max_length=30)
    user =  models.ForeignKey(User,related_name='user_address',on_delete=models.CASCADE)
    note = models.CharField(max_length=200)
    state = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    country = CountryField()
    street = models.CharField(max_length=80)
    type=models.CharField(choices=DATA_TYPE,max_length=10)

  

   

    
