import subprocess

from config.read_configs import ReadConfigs as configs

STARTUP_SCRIPT = configs.startup_script()
SERVER_DIR = configs.server_dir()

start_tmux = ("tmux", "-S", "/tmp/pair")
tmux_perms = ("chmod", "777", "/tmp/pair")
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
attach_tmux = ("tmux", "a")

commands = [
    start_tmux,
    tmux_perms,
    split_window,
    start_harbinger,
    cd_mc,
    start_minecraft,
    attach_tmux,
]

if __name__ == "__main__":
    for command in commands:
        subprocess.run(command)
