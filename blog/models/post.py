from django.db import models
from django.utils import timezone
from taggit.managers import TaggableManager

class Post(models.Model):
	author = models.ForeignKey('auth.User')
	title = models.CharField(max_length=200)
	subtitle = models.CharField(max_length=200)
	text = models.TextField()
	image = models.FileField(upload_to = 'images/')
	created_date = models.DateTimeField(default=timezone.now)
	published_date = models.DateTimeField(blank=True, null=True)
	tags = TaggableManager()

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.title