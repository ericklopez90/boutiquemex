from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()

router.register(r'productos', views.ProductosViewSet, basename="productos")
router.register(r'proveedores', views.ProveedoresViewSet, basename="proveedores")
router.register(r'generos', views.GenerosViewSet, basename="generos")
router.register(r'tipoproductos', views.TipoProductosViewSet, basename="tipoproductos")
router.register(r'temporadas', views.TemporadasViewSet, basename="temporadas")



urlpatterns = router.urls