from fabric import Connection
from dotenv import load_dotenv
from os import getenv

load_dotenv()
mc_hostname = getenv("MC_HOST")

def startServer():
    bot = Connection(f'{mc_hostname}')
    agentSetup = bot.run('tmux new -d -s server')
    agentCd = bot.run('tmux send -t server:0 "cd /home/logank/paper-test" C-m')
    agentStart = bot.run('tmux send -t server:0 "./java.sh" C-m')
    
def stopServer():
    bot = Connection(f'{mc_hostname}')
    agentStop = bot.run('tmux send -t server:0 "stop" C-m')
    