from rest_framework import routers
from .views import *

router = routers.SimpleRouter(trailing_slash=False)
router.register('friend', FriendSerializerViewSet)
router.register('belonging', BelongingSerializerViewSet)
router.register('borrowed', BorrowedSerializer)
urlpatterns = router.urls