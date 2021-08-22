from django.shortcuts import render

# from courses.models import Course
# from instructors.models import Instructor


def faq_view(request):
    """
    Create the faq template with context data
    """
    # courses = Course.objects.order_by('start_date').all()[:3]
    # instructors = Instructor.objects.order_by('dofb').all()[:3]
    context = {
        "title": "FAQS",
        # 'courses': '',
        # 'instructors': ''
    }
    return render(request, "pages/faqs.html", context)
