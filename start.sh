#!/bin/bash

# Script to start the Bot on Linux

# Navigate to server dir
# Ensure we have server.jar and paper.jar

tmux new -d -s harbinger # New tmux session
tmux send -t harbinger:0 "source .venv/bin/activate" C-m # Source the .venv
tmux send -t harbinger:0 "python3 -m pip install -r requirements.txt" C-m # Install requirements.txt
tmux send -t harbinger:0 "python3 harbinger.py" C-m # Run the bot
tmux split-window # Split the window; switch panes
tmux send -t harbinger:0 "ssh logank@mimir" C-m # SSH into mimir
tmux send -t harbinger:0 "cd /home/logank/logank_mc_server/try2" C-m # cd into server dir
tmux send -t harbinger:0 "zsh ./java.sh" C-m # Start Minecraft server, in theory
