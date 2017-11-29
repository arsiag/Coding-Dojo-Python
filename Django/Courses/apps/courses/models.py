# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

# Create your models here.
class CourseManager(models.Manager):
	def course_validator(self,postDATA):
		errors = {}
		if len(postDATA['name']) < 5:
			errors['name'] = "Course name should have at least 5 charactors"
		return errors

class DescriptionManager(models.Manager):
	def desc_validator(self,postDATA):
		errors = {}
		if len(postDATA['desc']) < 15:
			errors['desc'] = "Description should have at least 15 charactors"
		return errors

class Course(models.Model):
	name = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	objects = CourseManager()
	def __str__(self):
		return "<Course object {}>".format(self.name)

class Description(models.Model):
	content = models.TextField()
	course = models.OneToOneField(Course, related_name = "desc")
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	objects = DescriptionManager()
	def __str__(self):
		return "{}".format(self.content)

class Comment(models.Model):
	content = models.TextField()
	course = models.ForeignKey(Course, related_name="comments")
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	def __str__(self):
		return "{}".format(self.content)
