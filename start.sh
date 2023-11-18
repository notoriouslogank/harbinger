#!/bin/bash

# Script to start the Bot on Linux

# Navigate to server dir
# Ensure we have server.jar and paper.jar
# Ensure we have java.sh
# Tmux into two windows; start harbinger.py on one




### Basic Config - Uses .venv

tmux new -d -s harbinger
tmux send -t harbinger:0 "source .venv/bin/activate" C-m
tmux split-window
tmux send -t harbinger:0 "python3 -m pip install -r requirements.txt" C-m
tmux send -t harbinger:0 "python3 harbinger.py" C-m
tmux swap-pane
tmux send -t harbinger:0 "ssh logank@mimir" C-m



