#!/usr/bin/python
"""
@brief Run QuickBot class for Beaglebone Black

@author Rowland O'Flaherty 
@date 08/27/2013
"""

import sys
from QuickBot import *

print "Running QuickBot"

baseIP = '192.168.7.1'
robotIP = '192.168.7.2'

if len(sys.argv) > 3:
    print 'Invalid number of command line arguments.'
    print 'Proper syntax:'
    print '>> QuickBotRun.py baseIP robotIP'
    print 'Example:'
    print '>> QuickBotRun.py ', baseIP, ' ', robotIP
    sys.exit()

if len(sys.argv) >= 2:
    baseIP = sys.argv[1]

if len(sys.argv) >= 3:
    robotIP = sys.argv[2]

print 'Running QuickBot Program'
print '    Base IP: ', baseIP
print '    Robot IP: ', robotIP

QB = QuickBot(baseIP, robotIP)
QB.run()
QB.cleanup()