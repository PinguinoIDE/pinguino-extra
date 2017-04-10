#!/usr/bin/env python

"""
  Author:  Yeison Cardona --<yeisoneng@gmail.com>
  Purpose:
  Created: 04/10/17
"""

OLD = '#afc8e1'
NEW = '#62a3ff'

import os

files = os.listdir('.')
files = list(filter(lambda f: f.endswith(".svg"), files))


for filename in files:

    file = open(filename, 'r')
    content = file.read()
    file.close()

    file = open(filename, 'w')
    file.write(content.replace(OLD, NEW))
    file.close()




