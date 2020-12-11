from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model 
from rest_framework.reverse import reverse as api_reverse
# automated
#new / blank db 

from post.models import Post 
User = get_user_model()

class PostAPITestCase(APITestCase):
	def setUp(self):
		user  = User(username='testadminuser',)
		user.set_password("somepassword")
		user.save()
		post = Post.objects.create(user = user,
									title = 'New Title',
									content="Some Content"
									)

	def test_single_user(self):
		user_count = User.objects.count()
		self.assertEqual(user_count, 1)

	def test_single_post(self):
		post_count = Post.objects.count()
		self.assertEqual(post_count, 1)

	def test_get_list(self):
		#test the get list 
		data = {}
		url = api_reverse("post:post-listcreate")
		response = self.client.get(url, data, format='json')
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		print(response.data)

	
	