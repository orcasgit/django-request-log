import factory

from django.contrib.auth.models import User

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


class RequestLogFactory(factory.Factory):
    FACTORY_FOR = RequestLog
