from django.urls import path
from . import views
from .views import pryCivil
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path('', views.pryCivil),
    path('proyecto/', pryCivil),
    path('registrarProyecto/', views.registrarProyecto),
    path('edicionProyecto/<codigo>', views.edicionProyecto),
    path('editarProyecto/', views.editarProyecto),
    path('eliminarProyecto/<codigo>', views.eliminarProyecto),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)