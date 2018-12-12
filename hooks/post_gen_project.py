#!/usr/bin/env python

import os

for dirpath, dirs, files in os.walk(os.getcwd()):
    if 'keep' in files:
        for file in files:
            path = os.path.join(dirpath, file)
            os.unlink(path)
