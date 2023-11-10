# mcswitch

A somewhat primitive discord bot for managing a Minecraft server (among other things).  mcswitch is written primarily in Python, however some commands require a some shell commands via SSH to work.

**Note:**
At the time of this writing (v1.3.3), there is no comprehensive installer.  That's certainly on the roadmap (not yet implemented), but at this time all modules have been hand-picked, installed, and configured by me -- for better or for worse.

mcswitch was written from the ground up to run on a Raspberry Pi.  While I've made some reasonable attempts to make this codebase platform agnostic, I can't promise it's going to run on your system if it's not explicitly stated herein.  However if you find it *does* work on a platform *not* listed here, don't hesitate to drop me an [issue](https://github.com/notoriouslogank/mcswitch/issues).

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

- This could *probably* be persuaded to work using password authentication, but it's intended use case is to have public key authentication set up between the client and the server (ie, the Minecraft server and the bot host).

## Repository

First, you'll want to clone the repo: ``git clone https://github.com/notoriouslogank/mcswitch.git``

### Config Files

[TODO]

### java.sh

[TODO]

### main.py

[TODO]

## Commands

[TODO]

## Copyright

notoriouslogank 2023
