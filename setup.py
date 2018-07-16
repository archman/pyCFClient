'''
Created on Apr 4, 2011

@author: shroffk
'''

from setuptools import setup

setup(
    name='channelfinder',
    version='3.1.0',
    description='Python ChannelFinder Client Lib',
    author='Kunal Shroff',
    author_email='shroffk@bnl.gov',
    url='http://channelfinder.sourceforge.net/channelfinderpy',
    scripts=['cf-update-ioc', 'cf-monitor-test'],
    packages=['channelfinder', 'channelfinder/util', 'channelfinder/cfUpdate',],
      long_description="""\
      Python ChannelFinder Client Lib
      """,
      license='GPL',
      install_requires=[
        'requests',
      ],
      )
