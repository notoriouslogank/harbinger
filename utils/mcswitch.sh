#!/bin/zsh

ssh logank@mimir -t tmux new -d -s server
ssh logank@mimir -t 'tmux send -t server:0 "cd /home/logank/paper-test" C-m'
ssh logank@mimir -t 'tmux send -t server:0 "./java.sh" C-m'
