from django import template

from courses.models import Review

register = template.Library()


@register.filter()
def get_user_review(user, course_name):
    if user.is_authenticated:
        qs = (
            Review.objects.all()
            .filter(user__username=user, course__slug=course_name)
            .values("rating", "comment", "pub_date")
        )
        if qs.exists():
            return qs[0]
    return None
