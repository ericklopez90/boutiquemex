from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()

router.register(r'bancos', views.BancosViewSet, basename="bancos")
router.register(r'infobancos', views.InfoBancosViewSet, basename="infobancos")



urlpatterns = router.urls