# -*- coding: utf-8 -*-
"""
Internal module

Used to read the channelfinderapi.conf file

example file
cat ~/channelfinderapi.conf
[DEFAULT]
BaseURL=http://localhost:8080/ChannelFinder
username=MyUserName
password=MyPassword
"""

def __loadConfig():
    import os.path
    import ConfigParser
    dflt={'BaseURL':'https://localhost:8181/ChannelFinder',
          'username' : 'devuser',
          'password' : 'E=mc^2',
          'owner' : 'cf-update',
          'channelOwner' : 'cf-channels',
          'channelUsername' : 'devuser',
          'channelPassword' : 'E=mc^2',          
          'propOwner' : 'cf-properties',
          'propUsername' : 'devuser',
          'propPassword' : 'E=mc^2',
          'tagOwner' : 'cf-tags',
          'tagUsername' : 'devuser',
          'tagPassword' : 'E=mc^2'
        }
    cf=ConfigParser.SafeConfigParser(defaults=dflt)
    cf.read([
        '/etc/channelfinderapi.conf',
        os.path.expanduser('~/channelfinderapi.conf'),
        'channelfinderapi.conf'
    ])
    return cf
_testConf=__loadConfig()
