#!/bin/bash

#   LOCAL


tmux -d -s bot # Launch new tmux session [BOT]
tmux split-window 'ssh logank@mimir' # Split tmux window, run ssh in new pane [BOT]

tmux new -d -s server # Launch new tmux session [SERVER]
tmux send -t server:0 "cd /home/logank/paper-test" C-m # Change directory to server.jar location [SERVER]
tmux send -t server:0 "./java.sh" C-m # Launch java.sh (start server) [SERVER]

tmux send -t bot:1 "tmux a -t server" # Attach to tmux server [LOCAL]
