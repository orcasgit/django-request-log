from setuptools import setup

setup(
    name='orcas-log',
    version=__import__('log').__version__,
    description='Pluggable Django applications to record user login and logout events and URL views.',
    long_description=open('README.md').read(),
    author='Oregon Center for Applied Science',
    author_email='pperez@orcasinc.com',
    url='https://github.com/orcasgit/orcas-log',
    license='Apache 2.0',
    packages=['log'],
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved ::Apache',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
