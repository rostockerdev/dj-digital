from django.shortcuts import render


def bad_request(request, exception=None, template_name="400.html"):
    return render(request, "errors/400.html")


def permission_denied(request, exception=None, template_name="403.html"):
    return render(request, "errors/403.html")


def not_found(request, exception=None, template_name="404.html"):
    return render(request, "errors/404.html")


def server_error(request, exception=None, template_name="500.html"):
    return render(request, "errors/500.html")
