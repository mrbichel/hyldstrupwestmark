from django.shortcuts import render
from courses.models import Course
from django.conf import settings
from django.core.cache import cache
import twitter


def index(request):
    course_list = Course.public_objects.filter()

    return render(request, 'index.html', {'course_list': course_list })