from django.urls import path
from .views import *

app_name = 'post'

urlpatterns = [
	path('listcreate/', PostListAPIView.as_view(), name='post-listcreate'),
	path('rudview/<int:pk>/', PostRudAPIView.as_view(), name='post-rud'),
]
