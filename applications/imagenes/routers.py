from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()

router.register(r'imagenes', views.ImagenesViewSet, basename="imagenes")
router.register(r'documentos', views.DocumentosViewSet, basename="documentos")



urlpatterns = router.urls