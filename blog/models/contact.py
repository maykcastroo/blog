from django.db import models
from django.utils import timezone

class Contact(models.Model):
	name = models.CharField(max_length=200)
	email = models.EmailField()
	phone = models.CharField(null=True, max_length=13)
	message = models.TextField()
	created_date = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.message