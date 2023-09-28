from django.db import models


class Task(models.Model):
	title = models.CharField(max_length=100)
	description = models.CharField(max_length=300)
	complete = models.BooleanField(default=False)
	created = models.DateTimeField(auto_now_add=True)
	deadline = models.DateField()

	def __str__(self):
		return self.title

