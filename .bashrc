#
# ~/.bashrc
#

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

alias ls='ls --color=auto'
PS1='[\u@\h \W]\$ '
PAGER=nvimpager

if [ -z "$VIMRUNTIME" ]; then
    FZF_DEFAULT_OPTS="--preview '~/.config/ranger/scope.sh {} 0 0 /tmp/ False'":$FZF_DEFAULT_OPTS
else
    :
fi
