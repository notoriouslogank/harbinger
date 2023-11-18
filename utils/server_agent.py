from fabric import Connection, transfer
from configparser import ConfigParser
from harbinger import Harbinger

config_path = "config.ini"
config = ConfigParser()
config.read(config_path)
agent = Connection(host=f"{config['Server']['mc_host']}")


# startup_script = /home/logank/paper-test/java.sh <<< This should probably be included in the repo
class ServerAgent:
    def get_server_ip():  ## This can probably be done in a much better way.
        """Run curl on remote and send text file back to local."""
        Harbinger.timestamp("BOT", "GET_IP", "ATTEMPTING TO GET SERVER IP")
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
        Harbinger.timestamp("BOT", "STOP_SERVER", "STOPPING SERVER")

#    def command_server(command: str):
#        """Send a command to the Minecraft server via tmux.
#        Args:
#            command (str): Minecraft server command to send
#        """
#        server_command = agent.run(f'tmux send -t harbinger:0 "{command}" C-m')
#        Harbinger.timestamp("BOT", "SERVER_COMMAND", "SENDING USER STRING TO SERVER")
    def server_command(command: str):
        server_command = agent.run(f'tmux send -t harbinger:0 "{command}" C-m')
        Harbinger.timestamp("BOT", "SERVER_COMMAND", "SENDING MESSAGE TO SERVER")
    