from __future__ import unicode_literals
from django.db import models
from django.contrib import messages
import bcrypt

# Create your models here.
class UserManager(models.Manager):
    def currentUser(self, request):
        id = request.session['user_id']

        return User.objects.get(id=id)
    #so now i need to make this validateRegistration work: and need to pass in that form_data argument
    def validateRegistration(self, form_data):
    #now i need to check for required
        errors = []

        if len(form_data['name']) == 0:
            errors.append("Name is required.")
        if len(form_data['alias']) == 0:
            errors.append("Alias is required.")
        if len(form_data['email']) == 0:
            errors.append("Email is required.")
        if len(form_data['password']) < 8:
            errors.append("Please enter a password that is 8 or more characters.")
        if form_data['password'] != form_data['password_confirmation']:
            errors.append("Passwords do not match.")
        
        return errors
    #now go to views and insert "if not errors:" for verification

    def validateLogin(self, form_data):
        errors = []
#also check to see if user exists in DB. see views

        if len(form_data['email']) == 0:
            errors.append("Email is required.")
        if len(form_data['password']) == 0:
            errors.append("Password is required.")

        return errors

    #insert 'createUser' method here
    def createUser(self, form_data):
    #bcrypt step 1: is to convert user password to a str
    #password is the str form of password
        password = str(form_data['password'])
    #step 2: we need to hash that password copy and past this line: "hashed = bcrypt.hashpw(password, bcrypt.gensalt())"
        hashed_pw = bcrypt.hashpw(password, bcrypt.gensalt())
        #here is going to be all the keys and their values
        user = User.objects.create(
            name = form_data['name'],
            alias = form_data['alias'],
            email = form_data['email'],
            #so instead of saving the password to our form = "form_data['password']" we are going to save the hashed_pw
            password = hashed_pw,
            #now we are going to store this in session in views
        )

        return user
        #now we are goin to do bcrypt from here (also ref platform)
        #bcryt has installed successfully, now just import at top of this page.

class User(models.Model):
    name = models.CharField(max_length=255)
    alias = models.CharField(max_length=255)
    email = models.EmailField()
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()

class Quote(models.Model):
    content = models.CharField(max_length = 255)
    creator = models.ForeignKey(User, related_name = "posted_by")
    users = models.ManyToManyField(User, related_name = "quotes")
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)