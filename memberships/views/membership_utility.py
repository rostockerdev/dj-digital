from accounts.models import Profile, Subscription
from memberships.models import Membership


def get_user_membership(request):
    user_membership_qs = Profile.objects.filter(user=request.user)
    if user_membership_qs.exists():
        return user_membership_qs.first()
    return None


def get_user_subscription(request):
    user_subscription_qs = Subscription.objects.filter(
        profile=get_user_membership(request)
    )
    if user_subscription_qs.exists():
        return user_subscription_qs.first()
    return None


def get_selected_membership(request):
    membership_type = request.session["selected_membership_type"]
    selected_membership_qs = Membership.objects.filter(membership_type=membership_type)
    if selected_membership_qs.exists():
        return selected_membership_qs.first()
    return None
