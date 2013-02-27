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
        password = kwargs.pop('password', None)
        user = super(UserFactory, cls)._prepare(create, **kwargs)
        if password:
            user.set_password(password)
            if create:
                user.save()
        return user


class LogFactory(factory.Factory):
    FACTORY_FOR = Log


class RequestLogFactory(factory.Factory):
    FACTORY_FOR = RequestLog
