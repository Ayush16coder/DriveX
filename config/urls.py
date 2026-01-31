from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('DriveX.urls')),
    path('owner/', include('Owner.urls')),
    path('renter/', include('Renter.urls')),
    path('manager/', include('Manager.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
