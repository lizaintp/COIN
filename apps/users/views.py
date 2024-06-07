from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from apps.users import models
from apps.users import serializers

class UserAPI(GenericViewSet,
              mixins.ListModelMixin,
              mixins.RetrieveModelMixin,
              mixins.CreateModelMixin,
              mixins.UpdateModelMixin,
              mixins.DestroyModelMixin):
    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer