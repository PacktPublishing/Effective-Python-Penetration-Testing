#!/usr/bin/env python

from zapv2 import ZAPv2
from pprint import pprint
import time


target = 'http://example.com/'
zap = ZAPv2()

zap.urlopen(target)
time.sleep(2)

scan = zap.spider.scan(target)
time.sleep(2)

while (int(zap.spider.status(scan)) < 100):
    print 'Spider progress %: ' + zap.spider.status(scan)
    time.sleep(2)

print 'Spidering completed'
time.sleep(5)

scan = zap.ascan.scan(target)

while (int(zap.ascan.status(scan)) < 100):
    print 'Scan progress %: ' + zap.ascan.status(scanid)
    time.sleep(5)

print 'Passive Scan completed'


pprint (zap.core.alerts())