from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField
from django.db import models
from phone_field import PhoneField

# Create your models here.

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

class CommunityMember(User):
    phone_number = models.CharField(max_length=20)
    city = models.CharField(max_length=40)
    hobbies = models.ManyToManyField(Hobby)
    master_number = models.IntegerField(blank=True, null=True, default=None)
    master_number_generation_date = models.DateField(blank=True, null=True, default=None)
    friends = models.ManyToManyField('self', null=True, default=None)
    given_numbers = ArrayField(models.IntegerField(blank=True, null=True, default=None), size=100, null=True, default=None) # models.IntegerField(blank=True, default=0)
    def get_community_member_object(self): # TODO: consider refactoring to casting
        return





