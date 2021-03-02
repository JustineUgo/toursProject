from rest_framework import routers
from .api import BusinessViewSet, BusinessEndorsementViewSet, EndorsementViewSet, WheelViewSet, MediaViewSet, BusinessMediaViewSet, ShelPhotoViewSet, ShelfViewSet, BusinessShelfViewSet, ABusinessViewSet

router = routers.DefaultRouter()
router.register('api/business', BusinessViewSet, 'business')
router.register('api/abusiness', ABusinessViewSet, 'abusiness')
router.register('api/endorsement', EndorsementViewSet, 'endorsement')
router.register('api/businessendorsement', BusinessEndorsementViewSet, 'businessendorsement')
router.register('api/wheel', WheelViewSet, 'wheel')
router.register('api/media', MediaViewSet, 'media')
router.register('api/business_media', BusinessMediaViewSet, 'business_media')
router.register('api/shelfphoto', ShelPhotoViewSet, 'shelfphoto')
router.register('api/shelf', ShelfViewSet, 'shelf')
router.register('api/businessshelf', BusinessShelfViewSet, 'businessshelf')


urlpatterns = router.urls

