from django.core.urlresolvers import reverse
from django.test import TestCase
from nose.tools import eq_

from log.models import Log
from .basefactory import UserFactory


class TestLog(TestCase):

    def setUp(self):
        self.user = UserFactory.create()
        self.client.post(reverse('login'), {'username': self.user.username,
                                            'password': 'password'})

    def test_login_handler(self):
        visit = Log.objects.filter(user=self.user, varname='VisitNo').count()
        eq_(visit, 1)

    def test_get_log_value(self):
        ipaddr = Log.get_log_value(self.user, 'IPAddr')
        eq_(ipaddr, '127.0.0.1')

    def test_has_varname(self):
        varname = Log.has_varname(self.user, 'UsrAgnt')
        eq_(varname, True)

    def test_create_requestlog(self):
        resp = self.client.get(reverse('create_requestlog'))
        eq_(resp.status_code, 200)

        path = resp.request.get('PATH_INFO')
        eq_(path, '/create-log/')

    def test_logout_handler(self):
        resp = self.client.get(reverse('logout'))
        eq_(resp.status_code, 200)
