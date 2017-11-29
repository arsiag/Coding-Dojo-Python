# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
import re
# Create your models here.


EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
NAME_REGEX = re.compile(r'^[a-zA-Z.+_-]+$')

class UserManager(models.Manager):
	def user_validator(self, postData):
		errors = {}
		if len(postData['first_name']) == 0 or not NAME_REGEX.match(postData['first_name']):
		    errors["first_name"] = "Please enter a valid first name"
		if len(postData['last_name']) == 0 or not NAME_REGEX.match(postData['last_name']):
			errors["last_name"] = "Please enter a valid last name"
		if len(postData['email']) == 0 or not EMAIL_REGEX.match(postData['email']):
			errors["email"] = "Please enter a valid email"
		if len(errors) == 0:
			user = User.objects.filter(email = postData['email'])
			if len(user):
				errors["email"] = "Email already exists!"
		return errors

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return "<User object {} {} {} {}".format(self.first_name, self.last_namem, self.email, self.created_at)
    objects = UserManager()
