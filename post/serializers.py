from rest_framework import serializers 
from .models import Post 

class PostSerializer(serializers.ModelSerializer):
	url = serializers.SerializerMethodField(read_only=True)
	class Meta:
		model = Post 
		fields = ["url","id",'title','content','user','created_at','updated_at']
		read_only_fields = ['pk','user']

	def get_url(self,obj):
		request = self.context.get("request")
		return obj.get_api_url(request=request)

	def validate_title(self, value):
		qs = Post.objects.filter(title__iexact=value)
		if self.instance:
			qs = qs.exclude(pk=self.instance.pk)
		if qs.exists():
			raise serializers.ValidationError("This title has already been used!")
		return value
