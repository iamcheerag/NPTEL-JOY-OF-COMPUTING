# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 10:08:08 2019

@author: cheerag.verma
"""

from datetime import datetime
print(datetime.now())

import re
import pytz
all_timezones = str(pytz.all_timezones)
re.findall(r'America/.*',all_timezones)

timezone_singapore = pytz.timezone('Singapore')
print(datetime.now(timezone_singapore))  #gives time of singapore 


import calendar
calendar.weekday(2019,10,14)
