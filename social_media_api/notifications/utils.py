from django.contrib.contenttypes.models import ContentType
from .models import Notification

def create_notification(recipient, actor, verb, target=None):
    """
    Create a notification; target can be any model instance (Post, Comment, User, etc.)
    """
    if recipient == actor:
        return None
    kwargs = {
        'recipient': recipient,
        'actor': actor,
        'verb': verb,
    }
    if target is not None:
        ct = ContentType.objects.get_for_model(target.__class__)
        kwargs['target_content_type'] = ct
        kwargs['target_object_id'] = target.pk
    return Notification.objects.create(**kwargs)
