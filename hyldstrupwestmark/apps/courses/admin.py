from django.conf.urls import patterns
from django.contrib import admin
from models import Course, Signup, Occurrence

from admin_views import email_attendees

class SignupInline(admin.StackedInline):
    model = Signup

class OccurrenceInline(admin.StackedInline):
    model = Occurrence

class OccurrenceAdmin(admin.ModelAdmin):
    list_display  = ('course', 'start', 'end', 'status', 'location', 'price')
    search_fields = ('course', 'details', 'location', 'price')
    list_filter   = ('course', 'start', 'end')
    inlines = [ SignupInline, ]

    def email_attendees(self, request, id):
        return email_attendees(request, self, id)

    def get_urls(self):
        urls = super(OccurrenceAdmin, self).get_urls()
        my_urls = patterns('',
              (r'^(?P<id>\d+)/email_attendees/$', self.email_attendees)
        )
        return my_urls + urls

admin.site.register(Occurrence, OccurrenceAdmin)

class CourseAdmin(admin.ModelAdmin):
    list_display  = ('title', 'priority')
    search_fields = ('title', 'description', 'body')
    prepopulated_fields = {'slug': ('title',)}

    inlines = [ OccurrenceInline, ]
    
    fieldsets = (
        (None, {
            'fields': (('title', 'slug'), 'description', 'body', 'status', 'priority')
        }),
    )
admin.site.register(Course, CourseAdmin)

class SignupAdmin(admin.ModelAdmin):
    list_display  = ('first_name', 'last_name', 'email', 'phone', 'occurrence', 'time')
    list_filter   = ('time', 'occurrence',)
    search_fields = ('first_name', 'last_name', 'note')

admin.site.register(Signup, SignupAdmin)

#    actions = [ 'email_attendants' ]
#    def email_attendants(self, request, queryset):
#        selected = request.POST.getlist(admin.ACTION_CHECKBOX_NAME)
#        return HttpResponseRedirect(reverse('email_attendants', args=[selected]))
#    email_attendants.short_description = "Send an email to all people signed up for the selected courses"