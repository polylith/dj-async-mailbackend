from distutils.core import setup

setup(
    name='dj-async-mailbackend',
    version='1.0.0',
    packages=['async_mails', 'async_mails.migrations'],
    url='http://polylith.de/',
    license='MIT',
    author='polylith GbR',
    author_email='developers@polylith.de',
    description='',
    install_requires=[
        'redis',
        'celery',
        'django',
    ],
)
