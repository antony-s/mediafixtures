from setuptools import setup, find_packages


setup(
        name='mediafixtures',
        version='1.0',
        description='Collects media-files as fixtures from django apps.',
        long_description=open('README.rst').read(),
        author='Leander Hanwald',
        author_email='leander@hanwald.de',
        url='http://github.com/gamemine/mediafixtures/',
        license='MIT',
        packages=find_packages(),
        include_package_data=True,
        classifiers=[
            'Development Status :: 4 - Beta',
            'Environment :: Web Environment',
            'Framework :: Django',
            'Intended Audience :: Developers',
            'License :: OSI Approved :: MIT License',
            'Operating System :: OS Independent',
            'Programming Language :: Python',
            'Topic :: Software Development :: Libraries :: Python Modules',
        ],
    )
