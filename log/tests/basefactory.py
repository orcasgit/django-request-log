import factory

from datetime import datetime
from django.contrib.auth.models import User
from django.utils.timezone import utc

from log.models import Log, RequestLog


class UserFactory(factory.Factory):
    FACTORY_FOR = User

    username = factory.Sequence(lambda n: 'username{0}'.format(n))
    password = 'password'
    email = factory.Sequence(lambda n: 'email{0}@example.com'.format(n))

    @classmethod
    def _prepare(cls, create, **kwargs):
        plain_password = kwargs.pop('password')
        user = super(UserFactory, cls)._prepare(create, **kwargs)
        user.set_password(plain_password)
        user.save()
        return user


class LogFactory(factory.Factory):
    FACTORY_FOR = Log

    session = factory.Sequence(lambda n: 'session{0}'.format(n))
    varname = factory.Sequence(lambda n: 'varname{0}'.format(n))
    stamp = datetime.utcnow().replace(tzinfo=utc)
    value = factory.Sequence(lambda n: 'value{0}'.format(n))


class RequestLogFactory(factory.Factory):
    FACTORY_FOR = RequestLog

    session = factory.Sequence(lambda n: 'session{0}'.format(n))
    stamp = datetime.utcnow().replace(tzinfo=utc)
