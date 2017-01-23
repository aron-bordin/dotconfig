#!/bin/bash

echo "Installing symbolic links"

rm -rf ~/.config/fish
rm -rf ~/.config/i3
rm -rf ~/.config/rofi
rm -rf ~/.vimrc
rm -rf ~/.config/termite
rm -rf ~/.config/teiler
rm -rf ~/.config/tmux
rm -f ~/.tmux.conf

ln -s /home/aron/Programming/GitHub/dotconfig/fish/ /home/aron/.config/fish
ln -s /home/aron/Programming/GitHub/dotconfig/i3/ /home/aron/.config/i3
ln -s /home/aron/Programming/GitHub/dotconfig/rofi/ /home/aron/.config/rofi
ln -s /home/aron/Programming/GitHub/dotconfig/teiler/ /home/aron/.config/teiler
ln -s /home/aron/Programming/GitHub/dotconfig/termite/ /home/aron/.config/termite
ln -s /home/aron/Programming/GitHub/dotconfig/tmux/ /home/aron/.config/tmux
ln -s /home/aron/Programming/GitHub/dotconfig/.tmux.conf /home/aron/
ln -s /home/aron/Programming/GitHub/dotconfig/.vimrc /home/aron/

echo "Done with symlinks"

echo "Installing deps"

rm -rf /home/aron/.config/base16-shell
git clone https://github.com/chriskempson/base16-shell.git ~/.config/base16-shell

rm -rf /home/aron/.vim/bundle
git clone https://github.com/VundleVim/Vundle.vim.git /home/aron/.vim/bundle/Vundle.vim
