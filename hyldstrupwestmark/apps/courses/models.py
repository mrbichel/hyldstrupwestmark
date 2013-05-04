# coding=utf-8

import datetime
import markdown
from django.db import models

def format_html(markdownText):
    md = markdown.Markdown(
        extensions=['footnotes', 'abbr', 'tables', 'headerid']
    )

    return md.convert(unicode(markdownText))

class PublicCourseManager(models.Manager):
    """Manager for published courses returns courses with status public"""
    def get_query_set(self):
        qs = super(PublicCourseManager, self).get_query_set()
        return qs

class FutureOccurrenceManager(models.Manager):
    """Manager for future occurrences returns occurrences of courses with a end date in the future """
    def get_query_set(self):
        return super(FutureOccurrenceManager, self).get_query_set().filter(end__gte=datetime.datetime.now())

class Course(models.Model):
    """
    A course contains the detail for a generic course but no date and time
    """

    DRAFT_STATUS = 0
    PUBLIC_STATUS = 1
    ARCHIVED_STATUS = 2
    STATUS_CHOICES = (
        (DRAFT_STATUS, 'Draft'),
        (PUBLIC_STATUS, 'Public'),
        (ARCHIVED_STATUS, 'Archived'),
    )

    title = models.CharField(max_length=255)

    slug = models.SlugField(max_length=55,
        help_text="A short url friendly string",
        unique=True)   

    description = models.TextField(help_text='A short description of the course')

    body = models.TextField(
        help_text="Detailed description of the course",
        blank=True
    )
    html = models.TextField(editable=False, blank=True)
        
    add_date = models.DateTimeField(default=datetime.datetime.now, editable=False)
    mod_date = models.DateTimeField("Last updated", default=datetime.datetime.now, editable=False)

    status = models.PositiveIntegerField(choices=STATUS_CHOICES, default=DRAFT_STATUS)

    priority = models.IntegerField(default=0, help_text="Use this to sort the courses. Lower numbers come first.");

    objects = models.Manager()

    public_objects = PublicCourseManager()

    def get_future_occurrences(self):
        return self.occurrence_set.filter(end__gte=datetime.datetime.now())

    def __unicode__(self):
        return self.title

    @models.permalink
    def get_absolute_url(self):
        return ('course', (),
            {'slug': str(self.slug)})
            
    def save(self, *args, **kwargs):
        self.mod_date = datetime.datetime.now()
        self.html = format_html(self.body)
        super(Course, self).save(*args, **kwargs)
    
    class Meta:
        verbose_name = 'course'
        verbose_name_plural = 'courses'

class Occurrence(models.Model):
    """
    An Occurrence of a course is the date and time and specific details for a specific occurrence of the course
    """

    FULL_STATUS = 0
    OPEN_STATUS = 1
    CLOSED_STATUS = 2
    STATUS_CHOICES = (
        (FULL_STATUS, 'Full'),
        (OPEN_STATUS, 'Open'),
        (CLOSED_STATUS, 'Closed'),
    )

    status = models.PositiveIntegerField(choices=STATUS_CHOICES, default=OPEN_STATUS)

    course = models.ForeignKey(Course)

    start = models.DateTimeField(default=datetime.datetime.now)
    end = models.DateTimeField(blank=True)

    price = models.CharField(max_length=200, blank=True)

    location = models.CharField(max_length=200)
    details = models.TextField(help_text="Specific information for this occurrence. e.g. how to find the location or where to get a good lunch nearby.", blank=True)

    objects = models.Manager()
    future_objects = FutureOccurrenceManager()

    def __unicode__(self):
        return u"{} on {}".format(self.course.title, self.start)

    @models.permalink
    def get_absolute_url(self):
        return 'occurrence', (), {'id': self.id}

    def save(self, *args, **kwargs):
        if not self.end:
            self.end = self.start
        super(Occurrence, self).save(*args, **kwargs)

class Signup(models.Model):
    """
    A signup to an Occurrence of a course
    """
    occurrence = models.ForeignKey(Occurrence)

    email = models.EmailField(max_length=150)
    phone = models.CharField('Phone number', blank=True, max_length=16)
    first_name = models.CharField('First name', max_length=150)
    last_name = models.CharField('Last name', max_length=150)
    time = models.DateTimeField('Time', default=datetime.datetime.now, editable=False)
    note = models.TextField('Note', blank=True)
    address = models.TextField('Address',)
    postal_code = models.CharField('Postal code', max_length=20)
    country = models.CharField('Country', max_length=40)
    
    billing_address = models.TextField('Billing Address', help_text="If different from address.", blank=True)
    billing_postal_code = models.CharField('Billing Postal code', max_length=20, blank=True)
    billing_country = models.CharField('Billing Country', max_length=40, blank=True)
    
    profession = models.CharField('Profession', blank=True, max_length=80)

    def __unicode__(self):
        return u"{} signed up for {}".format(self.first_name, self.occurrence.course.title)

