from django.conf import settings
from django.conf.urls import handler400, handler403, handler404, handler500
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.contrib.sitemaps.views import sitemap
from django.contrib.staticfiles.storage import staticfiles_storage
from django.urls import include, path
from django.views.generic import TemplateView
from django.views.generic.base import RedirectView

from accounts import views as user_views
from core.sitemap import CourseSitemap, InstructorSitemap, StaticViewSitemap
from core.views.home_view import home_view

site_sitemaps = {
    "static": StaticViewSitemap,
    "courses": CourseSitemap,
    "instructors": InstructorSitemap,
}

urlpatterns = [
    path(
        "robots.txt",
        TemplateView.as_view(template_name="robots.txt", content_type="text/plain"),
    ),
    path(
        "sitemap.xml",
        sitemap,
        {"sitemaps": site_sitemaps},
        name="django.contrib.sitemaps.views.sitemap",
    ),
    path("instructors/", include("instructors.urls", namespace="instructors")),
    path("courses/", include("courses.urls", namespace="courses")),
    path("i18n/", include("django.conf.urls.i18n")),
    path("", home_view, name="home"),
    path("admin/", admin.site.urls),
    path("dashboard/", include("memberships.urls", namespace="memberships")),
    path("faqs/", include("pages.urls", namespace="pages")),
    path("profile/", user_views.profile_view, name="profile"),
    path("register/", user_views.registration_view, name="register"),
    path(
        "login/",
        auth_views.LoginView.as_view(template_name="accounts/login.html"),
        name="login",
    ),
    path(
        "logout/",
        auth_views.LogoutView.as_view(template_name="accounts/logout.html"),
        name="logout",
    ),
    path(
        "password-reset/",
        user_views.password_reset_request,
        name="password_reset",
    ),
    path(
        "password-reset/done/",
        auth_views.PasswordResetDoneView.as_view(
            template_name="accounts/password_reset_done.html"
        ),
        name="password_reset_done",
    ),
    path(
        "password-reset-confirm/<uidb64>/<token>",
        auth_views.PasswordResetConfirmView.as_view(
            template_name="accounts/password_reset_confirm.html"
        ),
        name="password_reset_confirm",
    ),
    path(
        "password-reset-complete",
        auth_views.PasswordResetCompleteView.as_view(
            template_name="accounts/password_reset_complete.html"
        ),
        name="password_reset_complete",
    ),
    path("subscribe/", include("subscriptions.urls", namespace="subscriptions")),
    path("notifications/", include("notifications.urls", namespace="notifications")),
    path("search/", include("search.urls", namespace="search")),
    path("ckeditor/", include("ckeditor_uploader.urls")),
    path(
        "favicon.ico",
        RedirectView.as_view(url=staticfiles_storage.url("favicon/favicon.ico")),
    ),
]

# Error Handler
handler400 = "errors.views.error_view.bad_request"
handler403 = "errors.views.error_view.permission_denied"
handler404 = "errors.views.error_view.not_found"
handler500 = "errors.views.error_view.server_error"

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
