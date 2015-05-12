from setuptools import setup

setup(
    name='django-request-log',
    version=__import__('log').__version__,
    description='Pluggable Django applications to record user login and logout events and URL views.',
    long_description=open('README.rst').read(),
    author='Oregon Center for Applied Science',
    author_email='pperez@orcasinc.com',
    url='https://github.com/orcasgit/django-request-log',
    license='Apache 2.0',
    packages=['log', 'log.migrations', 'log.south_migrations'],
    package_data={'': ['LICENCE']},
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
