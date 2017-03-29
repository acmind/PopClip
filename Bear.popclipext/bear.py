#!/usr/bin/python
# -*- coding:utf-8 -*-

import os
import urllib2


def urlencode(s):
    return urllib2.quote(s)


title = urlencode(os.getenv('POPCLIP_URL_TITLES'))
url = urlencode(os.getenv('POPCLIP_BROWSER_URL'))
select = urlencode(os.getenv('POPCLIP_HTML'))

content = "bear://x-callback-url/create?type=html&title=%s&text=%s&url=%s" % (
    title, select, url)

run_command = 'open' + ' ' + '"' + content + '"'
os.popen(run_command)