import urllib2

req = urllib2.Request('http://my.pretend.server')
try: urllis=b2.urlopen(req)
except urllib2.URLError as e:
	print e.reason
else:
	print 'site is up'