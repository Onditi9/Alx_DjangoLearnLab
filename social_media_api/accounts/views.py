from rest_framework import generics, permissions, status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import User  # or CustomUser if you renamed it
from .serializers import UserSerializer  # optional, for response

class FollowUserView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = User.objects.all()

    def post(self, request, user_id):
        target_user = get_object_or_404(User, id=user_id)
        request.user.follow(target_user)
        return Response({'message': f'You followed {target_user.username}'}, status=status.HTTP_200_OK)


class UnfollowUserView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = User.objects.all()

    def post(self, request, user_id):
        target_user = get_object_or_404(User, id=user_id)
        request.user.unfollow(target_user)
        return Response({'message': f'You unfollowed {target_user.username}'}, status=status.HTTP_200_OK)
