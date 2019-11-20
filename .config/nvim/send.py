#!/usr/bin/env python
import neovim
import sys

nvim = neovim.attach('socket', path='/tmp/vim-server')
nvim.command(' '.join(sys.argv[1:]))
