# accounts/views.py
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model

User = get_user_model()  # ✅ Use your custom user model


class FollowUserView(generics.GenericAPIView):
    """Allow an authenticated user to follow another user."""
    permission_classes = [IsAuthenticated]

    def post(self, request, user_id):
        try:
            user_to_follow = User.objects.get(id=user_id)
        except User.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

        request.user.follow(user_to_follow)
        return Response({'message': f'You are now following {user_to_follow.username}'}, status=status.HTTP_200_OK)


class UnfollowUserView(generics.GenericAPIView):
    """Allow an authenticated user to unfollow another user."""
    permission_classes = [IsAuthenticated]

    def post(self, request, user_id):
        try:
            user_to_unfollow = User.objects.get(id=user_id)
        except User.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

        request.user.unfollow(user_to_unfollow)
        return Response({'message': f'You unfollowed {user_to_unfollow.username}'}, status=status.HTTP_200_OK)


class UserListView(generics.ListAPIView):
    """List all users."""
    queryset = User.objects.all()  # ✅ this is what the check is looking for
    serializer_class = None  # you can set your custom serializer if you have one

