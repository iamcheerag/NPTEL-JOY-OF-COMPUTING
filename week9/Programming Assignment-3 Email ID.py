# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 14:54:43 2019

@author: cheerag.verma
"""

import re
text = 'abc@xyz.com'

data = re.search(r'(.*)@(.*)(.com)',text)
print(data.group(2))

