from django.conf import settings
from django.conf.urls import handler400, handler403, handler404, handler500
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView

from pages.views.home_view import home_view

urlpatterns = [
    path("i18n/", include("django.conf.urls.i18n")),
    # Robots.txt
    path(
        "robots.txt",
        TemplateView.as_view(template_name="robots.txt", content_type="text/plain"),
    ),
    path("", home_view, name="home"),
    path("admin/", admin.site.urls),
    path("faqs/", include("pages.urls", namespace="pages")),
]

# Error Handler
handler400 = "errors.views.error_view.bad_request"
handler403 = "errors.views.error_view.permission_denied"
handler404 = "errors.views.error_view.not_found"
handler500 = "errors.views.error_view.server_error"

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
