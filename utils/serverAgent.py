from fabric import Connection
from dotenv import load_dotenv
from os import getenv

load_dotenv()
mc_hostname = getenv("MC_HOST")


def startServer():
    bot = Connection(f"{mc_hostname}")
    serverSetup = bot.run("tmux new -d -s server")
    serverIp = bot.run('tmux send -t server:0 "curl https://ipinfo.io/ip >> ip.txt" C-m')
    serverGetip = bot.run('tmux send -t server:) "cat ip.txt" C-m')
    print(f'{serverGetip}')
    serverDir = bot.run('tmux send -t server:0 "cd /home/logank/paper-test" C-m')
    serverStart = bot.run('tmux send -t server:0 "./java.sh" C-m')
    print("Starting the server...")


def stopServer():
    bot = Connection(f"{mc_hostname}")
    serverStop = bot.run('tmux send -t server:0 "stop" C-m')
    print("Stopping the server...")


def commandServer(command: str):
    bot = Connection(f"{mc_hostname}")
    serverCommand = bot.run(f'tmux send -t server:0 "{command}" C-m')
    print(f"Sent command: {command}.")
