from setuptools import setup

setup(
    name="reinhardt",
    version="1.1.0",
    author_email='devhelp@ou.edu',
    description='A collection of Django tools created for ease of use and rapid development.',
    author='University of Oklahoma - Digital Innovations Group',
    license='BSD',
    install_requires=[
        "Django>=4.2",
        "django-currentuser>=0.5.3",
        "arrow>=1.2.3",
        "openpyxl>=3.1.2",
    ],
    classifiers=[
        'Development Status :: 1.1.0',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.9',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'Topic :: Software Development :: Libraries :: Python Modules',
        ],
    url='https://github.com/cceit/reinhardt/',
    packages=['reinhardt'],
    include_package_data=True,
    package_data={
        'reinhardt': [
            '*.py',
            'forms/*.py',
            'models/*.py',
            'utils/*.py',
            'utils/management/commands/*.py',
            'views/*.py',
            'templatetags/*.py',
            'templates/*.html',
            'templates/forms/*.html'
        ],
    },
    zip_safe=False,
)
