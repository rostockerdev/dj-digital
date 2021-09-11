from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from courses.models import Course
from instructors.models import Instructor
from notifications.models import Notification

from .membership_utility import get_user_membership, get_user_subscription


@login_required
def dashboard_view(request):
    courses = Course.objects.order_by("start_date").all()[:3]
    instructors = Instructor.objects.order_by("dofb").all()[:3]
    notifications = Notification.objects.filter(user=request.user, is_viewed=False)
    user_membership = get_user_membership(request)
    user_subscription = get_user_subscription(request)
    context = {
        "courses": courses,
        "instructors": instructors,
        "notifications": notifications,
        "user_membership": user_membership,
        "user_subscription": user_subscription,
    }
    return render(request, "memberships/dashboard.html", context)
