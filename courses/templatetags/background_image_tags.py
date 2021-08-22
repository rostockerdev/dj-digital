from django import template

from courses.models import Course

register = template.Library()


@register.filter()
def background_image_url(course_slug):
    # print(course_slug)
    """return image url"""
    return Course.objects.filter(slug=course_slug).get().thumbnail.url
    # return 'rasel'


# @register.simple_tag(background_image_url)
