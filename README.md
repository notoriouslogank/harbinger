# harbinger

A somewhat primitive discord bot for managing a Minecraft server (among other things).  harbinger is written primarily in Python, however some commands require a some shell commands via SSH to work.

**Note:**
At the time of this writing (v1.3.3), there is no comprehensive installer [Still true as of 1.6.4].  That's certainly on the roadmap (not yet implemented), but at this time all modules have been hand-picked, installed, and configured by me -- for better or for worse.

harbinger was written from the ground up to run on a Raspberry Pi.  While I've made some reasonable attempts to make this codebase platform agnostic, I can't promise it's going to run on your system if it's not explicitly stated herein.  However if you find it *does* work on a platform *not* listed here, don't hesitate to drop me an [issue](https://github.com/notoriouslogank/harbinger/issues).

## Prerequisites

### [paper-1.20.2-280.jar](https://papermc.io/)

This is how you'll manage your Minecraft server: it'll install server.jar, bukkit, some other random things.  Getting the Minecraft server running in and of itself is outside the scope of this documentation.

### Terminal Applications

The following applications should be easily installed from the standard repo:
    - curl: ``sudo apt install curl``
    - sshd: ``sudo apt install sshd``
    - tmux: ``sudo apt install tmux``

### [Java Runtime Environment](https://ubuntu.com/tutorials/install-jre#1-overview)

Find your current version of Jave (if any): ``java --version``.

You need to have the following version (or newer): ``openjdk 17.0.9 2023-10-17``

### Python3

You likely already have python installed.

First, make sure you have pip installed: ``sudo apt install python3-pip`` (Your system may differ.)

Then, install pipreqs and the requirements file: ``python3 -m pip install pipreqs && python3 -m pipreqs . --ignore .env,__pycache__,.venv`` (Your system may differ.)

Optionally, install venv (``sudo apt install python3-venv``) to create virtual environments quickly.

### SSH

- Make sure your Minecraft server is allowing traffic to the port (by default its 25565)
- The configuration that requires the least ongoing maintenence employs SSH keys and doesn't require passwords: you simply ssh@host and connect.  Harbinger relies on this behavior -- more detail will be added in future revisions of this document.
- This could *probably* be persuaded to work using password authentication, but it's intended use case is to have public key authentication set up between the client and the server (ie, the Minecraft server and the bot host).

## Repository

First, you'll want to clone the repo: ``git clone https://github.com/notoriouslogank/harbinger.git``

### java.sh

This may or may not actually be called *java.sh*, but this is the script that you run to actually launch your Minecraft server.  Included in the docs will be an example hopefully in the future.

### config.ini

This is the global configuration file for Harbinger.  An explanation of each of the settings:

- Bot
  - token: the authentication token from the Discord developer portal
  - channel: the channel ID of your main guild channel
  - custom_color: a color to set as trim for embeds, etc.
- Paths
  - server_dir: directory where your Minecraft server information is stored
  - startup_script: the script you run to start building your server instance
- Server
  - hostname: the username@hostname of the server hosting your Minecraft world (name@192.168.0.1 or name@host)
  - ip: the public IP of the server, where players will connect

### start.sh

This script creates the tmux session(s) and then launches both Harbinger and the Server inside a session.  Future updates will hopefully provide alternate scripts (ie Windows, iOS, etc); for now, this bash script works.

## Copyright

notoriouslogank 2023
