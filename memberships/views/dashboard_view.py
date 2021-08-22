from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render, reverse


@login_required
def dashboard_view(request):
    context = {}

    return render(request, "memberships/dashboard.html", context)
