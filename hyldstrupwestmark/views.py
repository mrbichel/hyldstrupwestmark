from django.shortcuts import render
from courses.models import Course

def index(request):
    course_list = Course.public_objects.filter().order_by("priority")[:10]

    return render(request, 'index.html', {'course_list': course_list })