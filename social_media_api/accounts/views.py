from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.contrib.auth import get_user_model

User = get_user_model()

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def follow_user(request, user_id):
    try:
        user_to_follow = User.objects.get(id=user_id)
        if user_to_follow == request.user:
            return Response({"detail": "You cannot follow yourself"}, status=400)

        request.user.following.add(user_to_follow)
        return Response({"detail": "User followed successfully"})

    except User.DoesNotExist:
        return Response({"detail": "User not found"}, status=404)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def unfollow_user(request, user_id):
    try:
        user_to_unfollow = User.objects.get(id=user_id)
        request.user.following.remove(user_to_unfollow)
        return Response({"detail": "User unfollowed successfully"})

    except User.DoesNotExist:
        return Response({"detail": "User not found"}, status=404)
