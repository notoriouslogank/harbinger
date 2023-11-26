# Harbinger

Harbinger is a (fairly) straightforward Discord bot written in Python (and a tiny amount of Bash).  It contains commands for Discord servers as well as integration to control a Minecraft server from Discord.

## Installation

### Install Tmux

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

Harbinger contains two configuration files: config.ini and start.conf, both of which are located in the config directory within the root folder.

## Usage

To launch the bot (and the Minecraft server):

```bash
bash start.sh
```

To launch the bot *only* (may cause errors):

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
