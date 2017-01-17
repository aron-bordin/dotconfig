#!/bin/sh

if [ "$DESKTOP_SESSION" = "i3" ]; then
    eval $(/usr/bin/gnome-keyring-daemon --start --components=pkcs11,secrets,ssh)
    export SSH_AUTH_LOCK
    echo "OK"
    echo $SSH_AUTH_LOCK
fi
