from django.urls import path

from memberships.views.cancel_subscriptions_view import cancel_subscription
from memberships.views.dashboard_view import dashboard_view
from memberships.views.membership_list_view import MembershipListView
from memberships.views.payment_view import PaymentView
from memberships.views.update_transaction import update_transaction_view

app_name = "memberships"

urlpatterns = [
    path("", dashboard_view, name="dashboard"),
    path("cancel/", cancel_subscription, name="cancel"),
    path("payment/", PaymentView.as_view(), name="payment"),
    path("select/", MembershipListView.as_view(), name="select"),
    path(
        "update-transactions/<subscription_id>/",
        update_transaction_view,
        name="update-transactions",
    ),
]
