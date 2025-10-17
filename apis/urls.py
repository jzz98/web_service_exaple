from .api import UserApi
from rest_framework import routers

router = routers.DefaultRouter()
router.register('api/', UserApi, 'api')

urlpatterns = router.urls
