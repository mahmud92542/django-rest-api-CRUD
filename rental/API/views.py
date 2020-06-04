from rest_framework.viewsets import ModelViewSet

from .serializers import *
from rental.models import *

class FriendSerializerViewSet(ModelViewSet):
	queryset = Friend.objects.all()
	serializer_class = FriendSerializer

class BelongingSerializerViewSet(ModelViewSet):
	queryset = Belonging.objects.all()
	serializer_class = BelongingSerializer
	

class BorrowedSerializer(ModelViewSet):
	queryset = Borrowed.objects.all()
	serializer_class = BorrowedSerializer