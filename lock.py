#!/usr/bin/env python

'''farmware-unlock
'''

from farmware_tools import device
device.emergency_lock()
device.log(message='farware-lock exectued', message_type='success')
