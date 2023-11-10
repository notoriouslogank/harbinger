from fabric import Connection, transfer
from helpers import Helpers

# startup_script = /home/logank/paper-test/java.sh <<< This should probably be included in the repo


class ServerAgent:
    """A class to represent the SSH agent managing the server/client connection.

    Attributes
    ----------
    agent: Class_method
        the instance of the server agent

    Methods
    -------
    get_server_ip(agent):
        run curl on remote server to get public IP
    start_server(agent):

    stop_server(agent):

    command_server(agent):
    """

    mc_hostname = Helpers.get_mc_host()
    agent = Connection(f"{mc_hostname}")

    def __init__(self, agent):
        """Constructs necessary paramenters for initializing the agent."""
        self.agent = agent

    def get_server_ip(agent):
        """Run curl on remote and send text file back to local."""
        query_ip = agent.run(
            "curl https://ipinfo.io/ip > /home/logank/paper-test/ip.txt"
        )
        get_ip = transfer.Transfer(agent).get(remote="/home/logank/paper-test/ip.txt")

    def start_server(agent):
        """Create an SSH connection and start the Minecraft server."""
        create_tmux = agent.agent("tmux new -d -s server")
        cd_to_dir = agent.run('tmux send -t server:0 "cd /home/logank/paper-test" C-m')
        server_start = agent.run('tmux send -t server:0 "./java.sh" C-m')
        print("Starting the server...")

    def stop_server(agent):
        """Runs the /stop command in the Minecraft server."""
        server_stop = agent.run('tmux send -t server:0 "stop" C-m')
        print("Stopping the server...")

    def command_server(command: str, agent):
        """Send a command to the Minecraft server via tmux.

        Args:
            command (str): Minecraft server command to send
        """
        server_command = agent.run(f'tmux send -t server:0 "{command}" C-m')
        print(f"Sent command: {command}.")
