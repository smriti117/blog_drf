from django.db import models
from django.contrib.auth.models import User 
from rest_framework.reverse import reverse as api_reverse

class Post(models.Model):
	title = models.CharField(max_length=255)
	content = models.TextField()
	user = models.ForeignKey(User, on_delete=models.CASCADE,related_name="user")
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.user.username

	@property
	def owner(self):
		return self.user

	def get_api_url(self,request=None):
		return api_reverse("post:post-rud", kwargs={'pk':self.id}, request=request)	
