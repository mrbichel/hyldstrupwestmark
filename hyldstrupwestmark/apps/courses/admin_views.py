from django.contrib.auth.decorators import permission_required
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from models import Occurrence
from forms import EmailAttendantsForm
from django.template.context import RequestContext
from django.template.loader import render_to_string
from django.conf import settings

@permission_required('courses.add_occurrence')
def email_attendants(request, model_admin, occurrence_id):

    opts = model_admin.model._meta
    has_perm = request.user.has_perm(opts.app_label + '.' + opts.get_change_permission())

    occurrence = get_object_or_404(Occurrence, id=occurrence_id)

    if request.method == 'POST':
        form = EmailAttendantsForm(request.POST)

        if form.is_valid():

            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            for signup in occurrence.signup_set.all():

                send_mail(subject,
                    render_to_string('courses/email/attendant_message.txt', {
                            'signup': signup,
                            'message': message,
                            'occurrence': occurrence},
                        RequestContext(request)),
                    settings.DEFAULT_FROM_EMAIL,
                    [signup.email]
                )

                return HttpResponse("you emailed them all, great!")
    else:
        form = EmailAttendantsForm()

    return render(request, 'admin/courses/email_attendants.html', {
        'occurrence': occurrence,
        'form': form,
        'title': 'Email attendants',
        'opts': opts,
        'app_label': opts.app_label,
        'has_change_permission': has_perm
    })