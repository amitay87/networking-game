import uuid

from django import forms
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import User, AbstractUser
from django.contrib.postgres.fields import ArrayField
from django.core.validators import int_list_validator
from django.db import models
from phone_field import PhoneField

# Create your models here.
from networkinggame import settings


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    # choice_text = models.

class Hobby(models.Model):
    def __str__(self):
        return self.name

    name = models.CharField(max_length=40)

# class CommunityMember(AbstractBaseUser):
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     password = forms.CharField(widget=forms.PasswordInput)
#     # email = forms.EmailField()
#     phone_number = models.CharField(max_length=20)
#     city = models.CharField(max_length=40)
#     hobbies = models.ManyToManyField(Hobby)
#     master_number = models.IntegerField(blank=True, null=True, default=None)
#     master_number_generation_date = models.DateField(blank=True, null=True, default=None)
#     friends = models.ManyToManyField('self', null=True, default=None)
#     given_numbers = models.CharField(validators=[int_list_validator], max_length=200, default='[]') # models.IntegerField(blank=True, default=0)
#     objects = BaseUserManager()
#     def get_community_member_object(self): # TODO: consider refactoring to casting
#         return

class UserExtendedInfo(models.Model):
# id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(
        # settings.AUTH_USER_MODEL,
        User,
        on_delete=models.CASCADE,
        unique=True,
        related_name='extended_info'
    )
    phone_number = models.CharField(max_length=20)
    city = models.CharField(max_length=40)
    hobbies = models.ManyToManyField(Hobby)
    master_number = models.IntegerField(blank=True, null=True, default=None)
    master_number_generation_date = models.DateField(blank=True, null=True, default=None)
    # friends = models.ManyToManyField(User, null=True, blank=True, default=None)
    given_numbers = models.CharField(validators=[int_list_validator], max_length=200, default='[]') # models.IntegerField(blank=True, default=0)



