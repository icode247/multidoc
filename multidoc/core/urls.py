from rest_framework.routers import DefaultRouter
from .views import OrganizationViewSet

router = DefaultRouter()
router.register(r'', OrganizationViewSet, basename='organization')
urlpatterns = router.urls