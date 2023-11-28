# Harbinger

Harbinger is a (fairly) straightforward Discord bot written in Python (and a tiny amount of Bash).  It contains commands for Discord servers as well as integration to control a Minecraft server from Discord.

## Installation

Harbinger is written *primarily* in Python, and as such *can* be run in a platform-agnostic way: launching harbinger.py will launch the bot as a standalone application -- this will *not* launch the Minecraft server, *nor* will it support multiplexing.

In order to run Harbinger *as intended*, and with all supported features, tmux will need to be installed.

### Tmux

Harbinger uses [tmux](https://github.com/tmux/tmux/wiki) to multiplex your Linux terminal -- this allows for multiple "panes", each containing a separate running process (ie, one Bot process and one Server process).

Installing tmux is straightforward (on Debian-based systems):

```bash
sudo apt update && sudo apt install tmux -y
```

### Clone the Repository

```bash
git clone https://github.com/notoriouslogank/harbinger.git
```

### Install Minecraft Server

Harbinger is designed to work with the Forge mod loader for Minecraft.  Download it [here](https://files.minecraftforge.net/net/minecraftforge/forge/), and run it:

```bash
java -jar forge-x.xx.x-installer.jar --installServer
```

Detailed installation/configuration for Forge is outside the scope of this document, but more information can be found [here](https://minecraft.fandom.com/wiki/Tutorials/Setting_up_a_Minecraft_Forge_server).

### Install requirements.txt

```bash
python3 -m pip install pipreqs && python3 -m pipreqs .
```

or

```bash
pip install -r requirements.txt
```

### Setup Harbinger Configuration

The first time Harbinger is run on a new system, it will *fail* to connect unless there are valid configuration files.

By default, the configuration files for Harbinger are located in /config/:

- config.ini: global Harbinger bot configuration file; this contains the bot API token, as well as other necessary information for Harbinger to launch properly
- start.conf: configures paths necessary to auto-start the Minecraft server (as well as multiplex the terminal)

To ensure you have the configuration files created properly, it is recommended to run:

```bash
python3 config/configure.py
```

This will walk you step-by-step through writing your config.ini file; advanced users can edit this file directly with his/her favorite text editor.

## Usage

Eventually, the goal is to have startup scripts for multiple operating systems.  At the time of this writing, however (v2.1.0), only a Linux startup script exists.  

To launch via the Linux startup script (launches both Harbinger as well as the Minecraft server in a multiplexed terminal):

```bash
./start.sh
```

To launch the bot *only*:

```bash
python3 harbinger.py
```

## Support

Please send any questions/comments/concerns to [logankdevemail@gmail.com] -- or submit an [issue](https://github.com/notoriouslogank/harbinger/issues)!

## Contributing

Feel free to submit a pull request if you have a new feature/bugfix/whatever -- I"ll take all the help I can get.

## License

MIT

## Copyright

notoriouslogank 2023
