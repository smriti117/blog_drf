from django.shortcuts import render
from django.db.models import Q
from rest_framework import generics, mixins 
from .models import Post 
from .permissions import IsOwnerOrReadOnly
from .serializers import *
from rest_framework import filters


class PostListAPIView(mixins.CreateModelMixin, generics.ListAPIView):
	lookup_field = 'pk' #imp
	search_fields = ['title','content']
	filter_backends = (filters.SearchFilter,) 
	serializer_class = PostSerializer
	queryset = Post.objects.all()

	# def get_queryset(self):
	# 	qs = Post.objects.all()
	# 	query = self.request.GET.get("query")
	# 	if query is not None:
	# 		qs = qs.filter(Q(title__icontains=query) | Q(content__icontains=query))
	# 	return qs

	def perform_create(self, serializer):
		serializer.save(user=self.request.user)

	def post(self, request, *args, **kwargs):
		return self.create(request, *args, **kwargs)

	def get_serializer_context(self, *args, **kwargs):
		return {"request":self.request}


class PostRudAPIView(generics.RetrieveUpdateDestroyAPIView):
	lookup_field = 'pk'
	serializer_class = PostSerializer
	permission_classes = [IsOwnerOrReadOnly]

	def get_queryset(self):
		return Post.objects.all()

	def get_serializer_context(self, *args, **kwargs):
		return {"request":self.request}
