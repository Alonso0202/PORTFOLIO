from django.contrib import admin
from django.urls import path, include
''' Parte importante para que funcione la carpeta 
midea '''
from django.conf import settings
from django.conf.urls.static import static
#impotamos views para poder ver nuestra nuestra vista principal
from portafolio import views


urlpatterns = [
    path('admin/', admin.site.urls),
    #Creamos la ruta principal del proyecto que se encuentra en la carpeta de portafolio
    path('',views.home, name='home'),
    path('blog/', include('blog.urls')),
]
''' Parte importante para que funcione la carpeta 
midea '''
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

