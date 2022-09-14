from rest_framework import generics
# from rest_framework.authentication import TokenAuthentication

from movienight_auth.models import User
from movienight_auth.api.serializers import UserSerializer



class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # authentication_classes = [TokenAuthentication]
    lookup_field = "email"