# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
import re # to validate email and other criteria
import bcrypt # imports bcrypt to generate a hashed passwords

# Create your models here.

emailRegex = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
pwordRegex = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).+$')
nameRegex = re.compile(r'^[a-zA-Z.+_-]+$')

class UserManager(models.Manager):
    def user_validator(self, postData):
        errors = {}
        # verify first name criteria
        if len(postData['fname']) < 2:
            errors["first_name"] = "First name cannot have fewer than 2 characters"
        elif not nameRegex.match(postData['fname']):
            errors["first_name"] = "First name must contain letters only"     
              
        # verify last name criteria
        if len(postData['lname']) < 2:
			errors["last_name"] = "Last name cannot have fewer than 2 characters"
        elif not nameRegex.match(postData['lname']):
            errors["last_name"] = "Last name must contain letters only"

		# verify email criteria
        if len(postData['email']) == 0:
			errors["email"] = "Email cannot be blank"
        elif not emailRegex.match(postData['email']):
            errors["email"] = "Please enter a valid email"
        else:
			user = User.objects.filter(email = postData['email'])
			if len(user):
				errors["email"] = "User already exists, please login!"

        # verify password criteria
        if len(postData['pword']) == 0:
			errors["password"] = "Password cannot be blank"
        elif len(postData['pword']) < 8:
			errors["password"] = "Password must be at least 8 characters long"
        elif not pwordRegex.match(postData['pword']):
            errors["password"] = "Password must contain at least one lowercase letter, one uppercase letter, and one digit"
        
        # verify confirm password criteria
        if len(postData['cpword']) == 0:
			errors["confirm password"] = "Confirm password cannot be blank"
        elif postData['pword'] != postData['cpword']:
			errors["confirm password"] = "Passwords do not match"
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return "<User object {} {} {} {}".format(self.first_name, self.last_namem, self.email, self.created_at)
    objects = UserManager()
