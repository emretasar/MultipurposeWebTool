from django.db import models


class Note(models.Model):
	title = models.CharField(max_length=100)
	note = models.CharField(max_length=1600)
	tag = models.CharField(max_length=20)
	create_date = models.DateTimeField(auto_now_add=True)
	last_edit_date = models.DateTimeField(auto_now_add=True)
	owner = models.CharField(max_length=16, default="Not Known")

	def __str__(self):
		return (self.title)
	
	


