#!/bin/bash

python3 -m venv .venv                               # Create Python venv
source .venv/bin/activate                           # Activate .venv
pip install --upgrade pip                           # Upgrade venv pip
python3 -m pip install -r requirements.txt          # Install requirements
tmux new -d -s harbinger                            # Create tmux session
tmux send -t harbinger:0 '"python3 harbinger.py" C-m' # Start the bot
tmux split-window                                   # Create server tmux pane
tmux send -t harbinger:0 '"zsh ~/SERVER/run.sh" C-m'  # Start the server
tmux send -t harbinger:0 '"C-b q 1" C-m'              # Change tmux pane
tmux a -t harbinger                                 # Attach to tmux
