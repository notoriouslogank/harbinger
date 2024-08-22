import subprocess

from config.read_configs import ReadConfigs as configs

STARTUP_SCRIPT = configs.startup_script()
SERVER_DIR = configs.server_dir()

start_tmux = ("tmux", "-S", "/var/tmux/Harbinger", "new", "-s", "Harbinger")
go_to = ("cd", "/var/tmux")
split_window = ("tmux", "split-window", "-v")
start_harbinger = (
    "tmux",
    "send",
    "-t",
    "Harbinger.2",
    "python3 harbinger.py",
    "ENTER",
)
cd_mc = ("tmux", "send", "-t", "Harbinger.1", f"cd {SERVER_DIR}", "ENTER")
start_minecraft = ("tmux", "send", "-t", "Harbinger.1", f"{STARTUP_SCRIPT}", "ENTER")
attach_tmux = ("tmux", "-S", "/var/tmux/Harbinger", "att", "-t", "Harbinger")
commands = [
    start_tmux,
    go_to,
    split_window,
    start_harbinger,
    cd_mc,
    start_minecraft,
    attach_tmux,
]

if __name__ == "__main__":
    for command in commands:
        subprocess.run(command)
