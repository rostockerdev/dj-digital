from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from accounts.forms import ProfileUpdateForm, UserUpdateForm
from instructors.models import Instructor


@login_required
def profile_view(request):
    if request.method == "POST":
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(
            request.POST, request.FILES, instance=request.user.profile
        )
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, "Your account has been updated")
            return redirect("memberships:dashboard")

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    instructors = Instructor.objects.order_by("dofb").all()[:3]
    context = {
        "u_form": u_form,
        "p_form": p_form,
        "instructors": instructors,
    }
    return render(request, "accounts/profile.html", context)
