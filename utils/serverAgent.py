from os import getenv

from dotenv import load_dotenv
from fabric import Connection

load_dotenv()
mc_hostname = getenv("MC_HOST")
# startup_script = /home/logank/paper-test/java.sh
# public_up = get_ip()


def startServer():
    """Create an SSH connection and start the Minecraft server."""
    bot = Connection(f"{mc_hostname}")  # Could probably be gloablly scoped?
    serverSetup = bot.run(
        "tmux new -d -s server"
    )  # These can probably be pared down into one long command
    serverGetip = bot.run('tmux send -t server:0 "cat ip.txt" C-m')
    serverDir = bot.run('tmux send -t server:0 "cd /home/logank/paper-test" C-m')
    serverStart = bot.run('tmux send -t server:0 "./java.sh" C-m')
    print("Starting the server...")


def stopServer():
    """Runs the /stop command in the Minecraft server."""
    bot = Connection(f"{mc_hostname}")
    serverStop = bot.run('tmux send -t server:0 "stop" C-m')
    print("Stopping the server...")


def commandServer(command: str):
    """Send a command to the Minecraft server via tmux.

    Args:
        command (str): Minecraft server command to send
    """
    bot = Connection(f"{mc_hostname}")
    serverCommand = bot.run(f'tmux send -t server:0 "{command}" C-m')
    print(f"Sent command: {command}.")
