# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
import re # to validate email and other criteria
import bcrypt # imports bcrypt to generate a hashed passwords

# Create your models here.

emailRegex = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
pwordRegex = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).+$')
nameRegex = re.compile(r'^[a-zA-Z\s]+[a-zA-Z]+$')

class UserManager(models.Manager):

    def register_validator(self, postData):
        errors = []
        # verify name criteria
        if len(postData['name']) < 2:
            errors.append("Name cannot have fewer than 2 characters")
        elif not nameRegex.match(postData['name']):
            errors.append("Name must contain letters only")  
              
        # verify alias criteria
        if len(postData['alias']) < 2:
            errors.append("Alias cannot have fewer than 2 characters")
        elif not nameRegex.match(postData['alias']):
            errors.append("Alias must contain letters only")

		# verify email criteria
        if len(postData['email']) == 0:
            errors.append("Email cannot be blank")
        elif not emailRegex.match(postData['email']):
            errors.append("Please enter a valid email")
        else:
            user = User.objects.filter(email = postData['email'])
            if len(user) != 0:
                errors.append("User already exists, please login!")

        # verify password criteria
        if len(postData['pword']) == 0:
            errors.append("Password cannot be blank")
        elif len(postData['pword']) < 8:
            errors.append("Password must be at least 8 characters long")
        elif not pwordRegex.match(postData['pword']):
            errors.append("Password must contain at least one lowercase letter, one uppercase letter, and one digit")
            
        # verify confirm password criteria
        if len(postData['cpword']) == 0:
            errors.append("Confirm password cannot be blank")
        elif postData['pword'] != postData['cpword']:
            errors.append("Passwords do not match")

        return errors

class User(models.Model):
    name = models.CharField(max_length=255)
    alias = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return "<User name: {} alias: {} email: {}".format(self.name, self.alias, self.email)
    objects = UserManager()

class Author(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return "<Author name: {}".format(self.name)

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, related_name="books")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return "<Book title: {}".format(self.title)

class ReviewManager(models.Manager):
    def review_validator(self, postData):
        errors = []
        # verify title criteria
        if len(postData['title']) < 1:
            errors.append('Title cannot be blank')

        # verify review criteria
        if len(postData['review']) < 1:
            errors.append('Review cannot be blank')

        # verify new_author criteria
        if not "author" in postData and len(postData['new_author']) < 5:
            errors.append('New author name must be at least five characters long')

        # verify rating criteria
        if int(postData['rating']) < 1 or int(postData['rating']) > 5:
            errors.append('Rating must be between one and five')

        return errors

    def review_creator(self, data, id):
        
        this_author = None
        # retrive existing author
        if len(data['new_author']) < 1:
            this_author = Author.objects.get(id=int(data['author']))
        # or create new author
        else:
            this_author = Author.objects.create(name=data['new_author'])

        this_book = None
        # create new book
        if not Book.objects.filter(title__iexact=data['title']):
            this_book = Book.objects.create(title=data['title'], author=this_author)
        # or retirive existing book
        else:
            this_book = Book.objects.get(title__iexact=data['title'])

        # create and returns a Review object
        return self.create(review = data['review'], rating = data['rating'], book = this_book, user = User.objects.get(id=id))

class Review(models.Model):
    review = models.TextField()
    rating = models.IntegerField()
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="reviews")
    user = models.ForeignKey(User, related_name="reviews_left")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ReviewManager()
    def __str__(self):
        return "Review: {} for book: {} and rating of: {}".format(self.review, self.book.title, self.rating)