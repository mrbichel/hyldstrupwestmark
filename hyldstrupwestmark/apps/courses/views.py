from django.core.mail import send_mail, mail_managers
from django.shortcuts import render, get_object_or_404
from django.template.context import RequestContext
from django.template.loader import render_to_string
from models import Course, Occurrence
from forms import OccurrenceSignupForm, EmailAttendantsForm
from django.conf import settings

def occurrence(request, id):
    occurrence = get_object_or_404(Occurrence, id=id)

    if request.method == 'POST' and occurrence.status is occurrence.OPEN_STATUS:
        form = OccurrenceSignupForm(request.POST)
        if form.is_valid():

            f = form.save(commit=False)
            f.occurrence = occurrence
            f.save()

            mail_managers(
                u"{} have signed up for {}".format(
                    f.first_name,
                    f.occurrence.course.title),
                render_to_string('courses/email/signup_notice.txt',
                        {'data': f, }, RequestContext(request))
            )

            send_mail(
                u"Sign up confirmation for {}".format(
                    f.occurrence.course.title),
                render_to_string('courses/email/signup_confirmation.txt',
                        {'data': f, }, RequestContext(request)),
                settings.DEFAULT_FROM_EMAIL,
                [f.email]
            )

            return render(request, 'courses/signup_thanks.html', {
                'data': f
            })

    else:
        form = OccurrenceSignupForm()

    return render(request, 'courses/occurrence.html', {
        'occurrence': occurrence,
        'form': form
    })


def list(request):
    course_list = Course.public_objects.filter()

    return render(request, 'courses/list.html', {
        'course_list': course_list
    })

def detail(request, slug):
    course = get_object_or_404(Course, slug=slug)

    return render(request, 'courses/detail.html', {
        'course': course
    })