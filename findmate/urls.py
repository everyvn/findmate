from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('api/', include('apps.api.urls')),
    path('admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('accounts/', include('allauth.urls')),
    path('profile/', include('apps.member.urls')),
    path('', include('apps.core.urls')),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
