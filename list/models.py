from __future__ import unicode_literals

from django.db import models

# Create your models here.
class List(models.Model):
	username = models.CharField(max_length=50)
	def __str__(self):
		return self.username

class Todo(models.Model):
	todo_text = models.TextField(null=True)
	list = models.ForeignKey(List, on_delete=models.CASCADE, null=True)

class Doing(models.Model):
	doing_text = models.TextField(null=True)
	list = models.ForeignKey(List, on_delete=models.CASCADE, null=True)

class Test(models.Model):
	test_text = models.TextField(null=True)
	list = models.ForeignKey(List, on_delete=models.CASCADE, null=True)

class Done(models.Model):
	done_text = models.TextField(null=True)
	list = models.ForeignKey(List, on_delete=models.CASCADE, null=True)