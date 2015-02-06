"""
Tests in this file are for testing everything in log.admin
"""
import django

from django.contrib.contenttypes.models import ContentType
from django.core.urlresolvers import reverse
from django.test import TestCase
from django.utils import timezone
from django.utils.formats import date_format
from nose.tools import eq_

from log.models import Log, RequestLog

from .basefactory import LogFactory, RequestLogFactory, UserFactory


class TestLogAdmin(TestCase):
    """ Test all the log admin classes """

    def setUp(self):
        self.user = UserFactory.create()
        self.user.is_active = True
        self.user.is_staff = True
        self.user.is_superuser = True
        self.user.save()
        self.django_version = django.get_version().split('.')

    def test_log_list(self):
        """ Test the list view for the Log admin """
        self.client.login(username=self.user.username,
                          password='password')

        list_url = self._admin_url(Log)
        add_url = self._admin_url(Log, Log())
        eq_(list_url, '/admin/log/log/')

        res = self.client.get(list_url)
        self.assertContains(res, '4 logs')
        self.assertContains(res, add_url)

        log = LogFactory(user=self.user)
        log.save()
        change_url = self._admin_url(Log, log)
        res = self.client.get(list_url)
        self.assertContains(res, '5 logs')
        self.assertRegexpMatches(
            res.content.decode(), '<tr.*%s.*%s.*%s.*%s.*%s.*</tr>' % (
                log.user.username, log.session, log.varname,
                date_format(timezone.localtime(log.stamp)), log.value
            ))
        if self.django_version[0] >= '1' and self.django_version[1] > '4':
            self.assertContains(res, change_url)
        else:
            # Django 1.4 used relative change url
            self.assertContains(res, '%i/' % log.id)
        self.assertContains(res, add_url)

    def test_requestlog_list(self):
        """ Test the list view for the RequestLog admin """
        self.client.login(username=self.user.username,
                          password='password')

        list_url = self._admin_url(RequestLog)
        add_url = self._admin_url(RequestLog, RequestLog())
        eq_(list_url, '/admin/log/requestlog/')

        res = self.client.get(list_url)
        self.assertContains(res, '0 request logs')
        self.assertContains(res, add_url)

        request_log = RequestLogFactory(user=self.user,
                                        url=reverse('login'))
        request_log.save()
        request_log_stamp = date_format(timezone.localtime(request_log.stamp))
        change_url = self._admin_url(RequestLog, request_log)
        res = self.client.get(list_url)
        self.assertContains(res, '2 request logs')
        self.assertContains(res, request_log.user.username)
        self.assertContains(res, request_log.session)
        self.assertContains(res, request_log.url)
        self.assertContains(res, request_log_stamp)
        self.assertRegexpMatches(
            res.content.decode(), '<tr.*%s.*%s.*%s.*%s.*</tr>' % (
                request_log.user.username, request_log.session,
                request_log.url, request_log_stamp))
        if self.django_version[0] >= '1' and self.django_version[1] > '4':
            self.assertContains(res, change_url)
        else:
            # Django 1.4 used relative change url
            self.assertContains(res, '%i/' % request_log.id)
        self.assertContains(res, add_url)

    def _admin_url(self, model, obj=None):
        """ Utility method to get an admin url for a model """
        content_type = ContentType.objects.get_for_model(model)
        uri = "admin:%s_%s" % (content_type.app_label, content_type.model)
        args = ()
        if obj:
            if obj.id:
                uri += '_change'
                args = (obj.id,)
            else:
                uri += '_add'
        else:
            uri += '_changelist'
        return reverse(uri, args=args)
