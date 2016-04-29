#
# Regular cron jobs for the python-cfclient package
#
0 4	* * *	root	[ -x /usr/bin/python-cfclient_maintenance ] && /usr/bin/python-cfclient_maintenance
