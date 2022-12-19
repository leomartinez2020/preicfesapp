from django.contrib import admin
from django.urls import path, include

#from django.conf import settings
#from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('preicfesapp.urls')),
    path('blog/', include('blog.urls')),
    path('lista-colegios/', include('saber11.urls')),
] #+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'preicfesapp.views.error_404'
