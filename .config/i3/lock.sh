#!/bin/bash

lock() {
    i3lock-fancy
}

case "$1" in
    lock) lock ;;
    logout) i3-msg exit ;;
    suspend) lock && systemctl suspend ;;
    hibernate) lock && systemctl hibernate ;;
    reboot) systemctl reboot ;;
    shutdown) systemctl poweroff -i ;;
esac
exit 0
