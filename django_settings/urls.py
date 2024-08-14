
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django_app import views
from django.conf.urls.static import static

urlpatterns = static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns = [
   
    path('grappelli/', include('grappelli.urls')), # grappelli URLS
    path('admin/', admin.site.urls),
    path('', views.index, name=''),    
    path('api/', include('django_app.urls'))
]
