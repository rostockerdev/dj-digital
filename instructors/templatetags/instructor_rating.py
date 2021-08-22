from django import template

from instructors.models import Rating

register = template.Library()


@register.filter()
def get_user_rating(user, instructor_name):
    if user.is_authenticated:
        qs = (
            Rating.objects.all()
            .filter(user__username=user, instructor__username=instructor_name)
            .values("rating", "review", "pub_date")
        )
        if qs.exists():
            print(qs[0])
            return qs[0]
    return None
