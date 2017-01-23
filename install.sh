#!/bin/sh

echo "Installing symbolic links"

rm -rf ~/.config/fish
rm -rf ~/.config/i3
rm -rf ~/.config/nvim
rm -rf ~/.config/rofi
rm -rf ~/.config/teiler
rm -rf ~/.config/tmux
rm -f ~/.tmux.conf

ln -s /home/aron/Programming/Github/dotconfig/fish/ /home/aron/.config/fish
ln -s /home/aron/Programming/Github/dotconfig/i3/ /home/aron/.config/i3
ln -s /home/aron/Programming/Github/dotconfig/nvim/ /home/aron/.config/nvim
ln -s /home/aron/Programming/Github/dotconfig/rofi/ /home/aron/.config/rofi
ln -s /home/aron/Programming/Github/dotconfig/teiler/ /home/aron/.config/teiler
ln -s /home/aron/Programming/Github/dotconfig/tmux/ /home/aron/.config/tmux
ln -s /home/aron/Programming/Github/dotconfig/.tmux.conf /home/aron/

echo "Done with symlinks"

echo "Installing deps"

rm -rf /home/aron/.config/base16-shell
git clone https://github.com/chriskempson/base16-shell.git ~/.config/base16-shell

rm -rf /home/aron/.config/nvim/bundle
git clone https://github.com/VundleVim/Vundle.vim.git /home/aron/.config/nvim/bundle/Vundle.vim
