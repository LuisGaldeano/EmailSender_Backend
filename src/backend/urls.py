from django.conf.urls import include
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from backend.settings import settings

urlpatterns = (
    [
        path("jet/", include("jet.urls", "jet")),
        path("jet/dashboard/", include("jet.dashboard.urls", "jet-dashboard")),  # Django JET dashboard URLS
        path("admin/", admin.site.urls),
        path("api/", include("core.api.urls", "core")),
    ]
    + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
)
