from pyexpat import model
from typing_extensions import Required
from django.db import models
from django.db import models
from django.db import models
from django.contrib.auth.models import User
from django.forms import DateField, IntegerField
from cloudinary.models import CloudinaryField
from django.dispatch import receiver
from django.db.models.signals import post_save
from psycopg2 import Date

class Profile(models.Model):
     user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
     name = models.CharField(max_length=80, blank=True)
     age = models.IntegerField(blank=True,null=True)
     profile_picture = CloudinaryField('images/')
     relationship = models.ForeignKey('Family',on_delete=models.SET_NULL, null=True, related_name='profile', blank=True)

     def __str__(self):
         return f'{self.user.username} profile'

     @receiver(post_save, sender=User)
     def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

     @receiver(post_save, sender=User)
     def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()
    

class Records(models.Model): 
    Name = models.CharField(max_length=80)
    Allergies = models.CharField( max_length=300)
    Hospital = models.CharField(max_length=100)
    Medication = models.TextField(blank=True)
    Date = models.DateField(null=True, blank=True)
    admin = models.ForeignKey('Profile', on_delete=models.CASCADE, related_name='record')

    def __str__(self):
        return f'{self.name} record'

    def create_Record(self):
        self.save()

    def delete_Record(self):
        self.delete()

    @classmethod
    def find_Record(cls, Record_id):
        return cls.objects.filter(id=Record_id)


class Family(models.Model):
    name = models.CharField(max_length=100)
    relation = models.CharField(blank=True, max_length=100)
    EmergencyContact = models.IntegerField(null=True)
    admin = models.ForeignKey('Records', on_delete=models.CASCADE, related_name='family')
    user_name = models.ForeignKey('Profile', on_delete=models.CASCADE)


    def __str__(self):
        return f'{self.name} Family'

    def create_family(self):
        self.save()

    def delete_family(self):
        self.delete()

    @classmethod
    def search_family(cls, name):
        return cls.objects.filter(name__icontains=name).all()

        


     