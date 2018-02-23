from __future__ import unicode_literals
from django.contrib.auth.models import User
from django import forms
from django.db import models
from django.db.models.signals import post_save
#from register.forms import AdminForm
from django.db.models.signals import *
import os
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)

# Create your models here.
from django.conf import settings
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name= models.CharField(max_length=200,blank=True)
    about_yourself= models.TextField( blank=True)
    age = models.IntegerField(default=0, blank=True)
    contact_number= models.IntegerField(default=0,blank=True)
    address=models.TextField(blank=True)
    Education =models.TextField(blank=True)
    Experience =models.TextField(blank=True)
    skills =models.TextField(blank=True)
    Work =models.TextField(blank=True)
    profile_photo = models.ImageField( blank=True,default="static\abc1.jpg",null=True,upload_to='media/')#default = os.path.join(settings.STATIC_ROOT,'static','abc1.jpg'),
    resume = models.FileField( blank=True,upload_to='media/',null=True)
    #default = os.path.join(settings.STATIC_ROOT,'static','abc1.jpg'),
   
                            #)#upload_to='media/')
    #rate=models.IntegerField()
#(max_length=100) #upload_to='media/')

    def __str__(self):
        return self.user.username

    def create_user_profile(sender, instance, created, **kwargs):
       if created:
        full_name=''#instance._full_name
        about_yourself=''#instance._about_yourself
        age=0 #instance._age
        contact_number=0 #instance._contact_number
        address=''#instance._address
        Education=''#instance._Education
        Experience=''#instance._Experience
        skills=''#instance._skills
        Work=''#instance._Work
        profile_photo=''#instance._profile_photo
        resume=''#instance._resume
      
        #c=instance._rate
        a=Profile.objects.create(user=instance,full_name=full_name)#,rate=c)

    post_save.connect(create_user_profile ,sender=User)

class PasswordField(forms.CharField):
    widget = forms.PasswordInput

class PasswordModelField(models.CharField):

    def formfield(self, **kwargs):
        defaults = {'form_class': PasswordField}
        defaults.update(kwargs)
        return super(PasswordModelField, self).formfield(**defaults)

class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_staffuser(self, email, password):
        """
        Creates and saves a staff user with the given email and password.
        """
        user = self.create_user(
            email,
            password=password,
        )
        user.staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        """
        Creates and saves a superuser with the given email and password.
        """
        user = self.create_user(
            email,
            password=password,
        )
        user.staff = True
        user.admin = True
        user.save(using=self._db)
        return user


    

    
class Managers(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    department_id= models.CharField(max_length=30)
    username= models.CharField(max_length=60,unique=True)
    active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False) # a admin user; non super-user
    admin = models.BooleanField(default=False) # a superuser
    # notice the absence of a "Password field", that's built in.

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = [] # Email & Password are required by default.

    def get_full_name(self):
        # The user is identified by their email address
        return self.email

    def get_short_name(self):
        # The user is identified by their email address
        return self.email

    def __str__(self):              # __unicode__ on Python 2
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        return self.staff

    @property
    def is_admin(self):
        "Is the user a admin member?"
        return self.admin

    @property
    def is_active(self):
        "Is the user active?"
        return self.active
   
    objects = UserManager()
    
