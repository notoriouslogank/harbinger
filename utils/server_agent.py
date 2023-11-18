from fabric import Connection, transfer
from configparser import ConfigParser
#from harbinger import *
import pathlib
import os

config_path = "config.ini"
config = ConfigParser()
config.read(config_path)
agent = Connection(host=f"{config['Server']['mc_host']}")


class ServerAgent:
    def check_server():
        server_dir = config["Paths"]["server_dir"]
        server_script = config["Paths"]["server_script"]
        os.chdir(pathlib.Path(server_dir))  # Move to dir with server.jar
        if os.path.exists(server_dir + server_script):
            print("exists")
        else:
            print("does not appear to")

    def get_server_ip():  ## This can probably be done in a much better way.
        """Run curl on remote and send text file back to local."""
#        Harbinger.timestamp("BOT", "GET_IP", "ATTEMPTING TO GET SERVER IP")
        query_ip = agent.run(
            "curl https://ipinfo.io/ip > /home/logank/paper-test/ip.txt"
        )
        get_ip = transfer.Transfer(agent).get(remote="/home/logank/paper-test/ip.txt")

    def start_server():
        # Couldn't these commands just be one bash script? Or at least the two agent.run() statements could be one?
        """Create an SSH connection and start the Minecraft server."""
        server_dir = config["Bot"]["server_dir"]
        server_script = config["Bot"]["server_script"]
        create_tmux = agent.run("tmux new -d -s server")
        cd_to_dir = agent.run(f'tmux send -t server:0 "cd {server_dir}" C-m')
        server_start = agent.run(f'tmux send -t server:0 "{server_script}" C-m')

    def stop_server():
        """Runs the /stop command in the Minecraft server."""
        server_stop = agent.run('tmux send -t server:0 "stop" C-m')
#        Harbinger.timestamp("BOT", "STOP_SERVER", "STOPPING SERVER")

    def command_server(command: str):
        """Send a command to the Minecraft server via tmux.
        Args:
            command (str): Minecraft server command to send
        """
        server_command = agent.run(f'tmux send -t server:0 "{command}" C-m')
#        Harbinger.timestamp("BOT", "SERVER_COMMAND", "SENDING USER STRING TO SERVER")


ServerAgent.check_server()
