import subprocess
from config.read_configs import ReadConfigs as configs

STARTUP_SCRIPT = configs.startup_script()

start_tmux = ("tmux", "new-session", "-d", "-s", "Harbinger")
split_window = ("tmux", "split-window", "-v")
start_harbinger = (
    "tmux",
    "send",
    "-t",
    "Harbinger.2",
    "python3 harbinger.py",
    "ENTER",
)
start_minecraft = ("tmux", "send", "-t", "Harbinger.1", f"{STARTUP_SCRIPT}", "ENTER")
attach_tmux = ("tmux", "a")

commands = [start_tmux, split_window, start_harbinger, start_minecraft, attach_tmux]

for command in commands:
    subprocess.run(command)

# subprocess.run(("tmux", "new-session", "-d", "-s", "Harbinger"), shell="True")
