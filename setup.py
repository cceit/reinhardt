from setuptools import setup, find_packages

setup(
    name="reinhardt",
    version="0.1a",
    author_email='devhelp@cce.ou.edu',
    description='A collection of Django tools created for ease of use and rapid development.',
    author='University of Oklahoma - College of Continuing Education - IT',
    license='BSD',
    install_requires=[
        "django-currentuser",
        "arrow",
        "openpyxl",
        "django-tables2",
    ],
    classifiers=[
        'Development Status :: 0.1a',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'Topic :: Software Development :: Libraries :: Python Modules',
        ],
    url='https://github.com/cceit/django-dx',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
)
