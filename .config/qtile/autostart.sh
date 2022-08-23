#!/bin/sh

# systray battery icon
cbatticon -u 5 &

# systray volume
pasystray &

# external disk mount icon 
udiskie -t &

# network applet 
nm-applet &