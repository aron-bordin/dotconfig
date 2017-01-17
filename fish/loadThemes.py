#!/bin/python

import sys
import os
from pick import pick

def setTheme(name):
    open('.theme', 'w').write(name)
    print(name)

themes = [t.replace('base16-', '').replace('.theme', '').replace('.16', '') for t in os.listdir('/home/aron/.local/share/xfce4/terminal/colorschemes/')]
themes = sorted(set(themes))
name = None
if os.path.isfile('/home/aron/.config/fish/.theme'):
    name = open('/home/aron/.config/fish/.theme', 'r').read()
    if not name:
        name is None
else:
    name = 'default-dark'

if len(sys.argv) == 1:
    setTheme(name)
else:
    message = 'Select the desired theme:'
    opt, index = pick(themes, message, indicator='>',
                      default_index=themes.index(name))
    setTheme(opt)
