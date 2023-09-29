from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters
from rest_framework.permissions import AllowAny, IsAuthenticated

from users.models import User
from .serializers import UsersCreateSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    URL requests handler to 'Users' resource endpoints.
    """

    name = "Change account information by user"
    description = "Change account information by user"

    queryset = User.objects.all()
    serializer_class = UsersCreateSerializer
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter)
    filterset_fields = ("username", "email") 
    ordering_fields = ("username", "email")

    def get_permissions(self):
        if self.action in ("list", "create", "retrieve"):
            return (AllowAny(),)
        return (IsAuthenticated(),)
