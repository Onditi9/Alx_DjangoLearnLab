from rest_framework import serializers
from .models import Notification

class NotificationSerializer(serializers.ModelSerializer):
    actor_username = serializers.CharField(source='actor.username', read_only=True)
    recipient_id = serializers.IntegerField(source='recipient.id', read_only=True)

    class Meta:
        model = Notification
        fields = ['id', 'recipient_id', 'actor_username', 'verb', 'unread', 'timestamp']
