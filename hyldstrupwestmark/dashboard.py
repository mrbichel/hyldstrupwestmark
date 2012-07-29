"""
This file was generated with the customdashboard management command and
contains the class for the main dashboard.

To activate your index dashboard add the following to your settings.py::
    GRAPPELLI_INDEX_DASHBOARD = 'hyldstrupwestmark.dashboard.CustomIndexDashboard'
"""

from django.utils.translation import ugettext_lazy as _

from grappelli.dashboard import modules, Dashboard
from grappelli.dashboard.utils import get_admin_site_name


class CustomIndexDashboard(Dashboard):
    """
    Custom index dashboard for www.
    """
    
    def init_with_context(self, context):
        site_name = get_admin_site_name(context)
        
        self.children.append(modules.ModelList(
            _('Courses'),
            collapsible=False,
            column=1,
            models=('courses.*',),
        ))

        self.children.append(modules.ModelList(
            _('Content'),
            column=1,
            collapsible=True,
            models=('django.contrib.flatpages.*','flatblocks.*'),
        ))

        self.children.append(modules.ModelList(
            _('Administration'),
            column=1,
            collapsible=True,
            models=('django.contrib.auth.*','django.contrib.sites.*'),
        ))



        self.children.append(modules.LinkList(
            _('Quick links'),
            column=2,
            children=[
                {
                    'title': _('View frontpage'),
                    'url': '/',
                    'external': False,
                },
            ]
        ))
        
        #append another link list module for "support".
        #self.children.append(modules.LinkList(
        #    _('Support'),
        #    column=2,
#            children=[
#                {
#                    'title': _('Django Documentation'),
#                    'url': 'http://docs.djangoproject.com/',
#                    'external': True,
#                },
#                {
#                    'title': _('Grappelli Documentation'),
#                    'url': 'http://packages.python.org/django-grappelli/',
#                    'external': True,
#                },
#                {
#                    'title': _('Grappelli Google-Code'),
#                    'url': 'http://code.google.com/p/django-grappelli/',
#                    'external': True,
#                },
#            ]
#        ))
        
        # append a feed module
        #self.children.append(modules.Feed(
        #    _('Latest Django News'),
        #    column=2,
        #    feed_url='http://www.djangoproject.com/rss/weblog/',
        #    limit=5
        #))
        
        # append a recent actions module
        self.children.append(modules.RecentActions(
            _('Recent Actions'),
            limit=5,
            collapsible=False,
            column=3,
        ))


