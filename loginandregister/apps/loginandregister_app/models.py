from __future__ import unicode_literals
from django.db import models

# Create your models here.
class UserManager(models.Manager):
    def validate(self, form_data):
        #create an errors check set to a list at the top and going to append new errors to the list as goes a long
        errors = []
    # if data at the first_name key has a length ==0 we know it is blank
        if len(form_data['first_name']) == 0:
            errors.append("First Name is required.")
        if len(form_data['last_name']) == 0:
            errors.append('Last Name is required.')
        if len(form_data['email']) == 0:
            errors.append('Email is required.')
        if len(form_data['password']) == 0:
            errors.append('Password is required.')
        if form_data['password'] != form_data['password_confirmation']:
            errors.append('Password Confirmation must match password.')

        return errors 

    def validate_login(self, form_data):
        errors = []

        if len(form_data['email']) == 0:
            errors.append('Email is required.')
        if len(form_data['password']) == 0:
            errors.append('Password is required.')

        return errors

    def login(self, form_data):
        errors = self.validate_login(form_data)

        if not errors:
            user = User.objects.filter(email=form_data['email']).first()

            if user:
                if str(form_data['password']) == user.password:
                    return user

            errors.append('Invalid Account Information')

        return errors

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

#use __str__ method to see what is inside that object
#so what this is saying is any time this object is used in a  __str__ method, meaning when we try to print it out instead of it saying User Object we can change what it says. so we have to return a string and we say what string we would like it to show
    def __str__(self):
        string_output =  "id: {} first_name: {} last_name: {} email:{} password:{}"

        return string_output.format(
            self.id,
            self.first_name,
            self.last_name,
            self.email,
            self.password,
        )

    objects = UserManager()