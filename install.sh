#!/bin/sh

echo "Installing symbolic links"


ln -s ~/Programming/GitHub/dotconfig/fish/ ~/.config/fish
ln -s ~/Programming/GitHub/dotconfig/i3/ ~/.config/i3
ln -s ~/Programming/GitHub/dotconfig/nvim/ ~/.config/nvim
ln -s ~/Programming/GitHub/dotconfig/rofi/ ~/.config/rofi
ln -s~/Programming/GitHub/dotconfig/teiler/ ~/.config/teiler
ln -s ~/Programming/GitHub/dotconfig/tmux/ ~/.config/tmux
ln -s ~/Programming/GitHub/dotconfig/.tmux.conf ~/

echo "Done with symlinks"

echo "Installing deps"

