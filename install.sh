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

mkdir -p ~/.config
mkdir -p ~/.local/share/qutebrowser

# .config
ln -s $HOME/Programming/GitHub/dotconfig/.config/fish/ $HOME/.config/fish
ln -s $HOME/Programming/GitHub/dotconfig/.config/htop/ $HOME/.config/htop
ln -s $HOME/Programming/GitHub/dotconfig/.config/i3/ $HOME/.config/i3
ln -s $HOME/Programming/GitHub/dotconfig/.config/rofi/ $HOME/.config/rofi
ln -s $HOME/Programming/GitHub/dotconfig/.config/teiler/ $HOME/.config/teiler
ln -s $HOME/Programming/GitHub/dotconfig/.config/termite/ $HOME/.config/termite
ln -s $HOME/Programming/GitHub/dotconfig/.config/tmux/ $HOME/.config/tmux
ln -s $HOME/Programming/GitHub/dotconfig/.config/qutebrowser/ $HOME/.config/qutebrowser
ln -s $HOME/Programming/GitHub/dotconfig/.config/ranger/ $HOME/.config/ranger
ln -s $HOME/Programming/GitHub/dotconfig/.config/compton.conf $HOME/.config/
ln -s $HOME/Programming/GitHub/dotconfig/.config/dunstrc $HOME/.config/
ln -s $HOME/Programming/GitHub/dotconfig/.config/flake8 $HOME/.config/

# local/share

ln -s $HOME/Programming/GitHub/dotconfig/.local/share/qutebrowser/qtwebengine_dictionaries/ $HOME/.local/share/qutebrowser/
ln -s $HOME/Programming/GitHub/dotconfig/.local/share/qutebrowser/userscripts/ $HOME/.local/share/qutebrowser/

# $HOME
ln -s $HOME/Programming/GitHub/dotconfig/.tmux.conf $HOME/
ln -s $HOME/Programming/GitHub/dotconfig/.vimrc $HOME/
ln -s $HOME/Programming/GitHub/dotconfig/.bashrc $HOME/
ln -s $HOME/Programming/GitHub/dotconfig/.gitconfig $HOME/
ln -s $HOME/Programming/GitHub/dotconfig/.xinitrc $HOME/
ln -s $HOME/Programming/GitHub/dotconfig/.Xresources $HOME/

echo "Done with symlinks"

echo "Installing deps"

rm -rf $HOME/.config/base16-shell
git clone https://github.com/chriskempson/base16-shell.git ~/.config/base16-shell

rm -rf $HOME/.vim/bundle
git clone https://github.com/VundleVim/Vundle.vim.git $HOME/.vim/bundle/Vundle.vim

./install_packages.sh

git config --global merge.tool vimdiff
git config --global merge.conflictstyle diff3
git config --global mergetool.prompt false
