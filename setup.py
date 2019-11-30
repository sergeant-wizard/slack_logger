from setuptools import setup

setup(
    name='slack logger',
    version='0.0.1',
    description='logging.Handler for Slack',
    author='Ryo Miyajima',
    license='TBD',
    packages=['slack_logger'],
    install_requires=[
        'requests==2.22.0',
    ],
)
