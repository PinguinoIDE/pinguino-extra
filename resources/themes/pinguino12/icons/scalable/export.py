#!/usr/bin/env python

"""
  Author:  Yeison Cardona --<yeisoneng@gmail.com>
  Purpose:
  Created: 04/10/17
"""

import os
import shutil

root = os.path.dirname(__file__)
files = os.listdir(".")
files = list(filter(lambda f:f.endswith(".svg"), files))

for size in ["16", "24", "32", "48"]:
    path = "../{}".format(size)

    if not os.path.exists(path):
        os.makedirs(path, exist_ok=True)
    else:
        shutil.rmtree(path)
        os.makedirs(path, exist_ok=True)


    for file in files:

        filename_svg = file
        filename_png = os.path.join(path, file.replace(".svg", ".png"))

        command = "inkscape {filename_svg} -e={filename_png} -C -w={size} -h={size}".format(**locals())
        os.system(command)