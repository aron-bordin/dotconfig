#!/bin/python

import sys
import os
from pick import pick


def setTheme(name):
    open('/home/aron/.config/fish/.theme', 'w').write(name)
    print(name)


name = None
if os.path.isfile('/home/aron/.config/fish/.theme'):
    name = open('/home/aron/.config/fish/.theme', 'r').read().strip()
    if not name:
        name = None
if not name:
    name = 'default-dark'

if len(sys.argv) == 1:
    print(name)
else:
    themes = [t.replace('base16-', '').replace('.sh', '')
              for t in os.listdir('/home/aron/.config/base16-shell/scripts/')]
    themes = sorted(set(themes))
    message = 'Select the desired theme:'
    opt, index = pick(themes, message, indicator='>',
                      default_index=themes.index(name))
    setTheme(opt)
