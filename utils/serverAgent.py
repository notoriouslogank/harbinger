from fabric import Connection, transfer
from helpers import Helpers

mc_hostname = Helpers.get_mc_host()
# startup_script = /home/logank/paper-test/java.sh <<< This should probably be included in the repo

class ServerAgent():
    
    agent = Connection(f'{mc_hostname}')
    
    def __init__(self, agent):
        self.agent = agent
        
    def ipServer(agent):
        serverIp = agent.run("curl https://ipinfo.io/ip > /home/logank/paper-test/ip.txt")
        getIp = transfer.Transfer(agent).get(remote="/home/logank/paper-test/ip.txt")

    
    def startServer(agent):
        """Create an SSH connection and start the Minecraft server."""
        serverSetup = agent.agent(
        "tmux new -d -s server"
        )  # These can probably be pared down into one long command
        serverDir = agent.run('tmux send -t server:0 "cd /home/logank/paper-test" C-m')
        serverStart = agent.run('tmux send -t server:0 "./java.sh" C-m')
        print("Starting the server...")


    def stopServer(agent):
        """Runs the /stop command in the Minecraft server."""
        serverStop = agent.run('tmux send -t server:0 "stop" C-m')
        print("Stopping the server...")


    def commandServer(command: str, agent):
        """Send a command to the Minecraft server via tmux.

        Args:
            command (str): Minecraft server command to send
        """
        serverCommand = agent.run(f'tmux send -t server:0 "{command}" C-m')
        print(f"Sent command: {command}.")
