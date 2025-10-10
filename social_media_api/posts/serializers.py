from rest_framework import serializers
from .models import Post, Comment

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

from rest_framework import serializers
from .models import Post, Like

class LikeSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(source='user.id', read_only=True)
    post_id = serializers.IntegerField(source='post.id', read_only=True)

    class Meta:
        model = Like
        fields = ['id', 'post_id', 'user_id', 'created_at']
