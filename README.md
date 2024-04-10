# Harbinger <!-- omit from toc -->

Harbinger, a Discord bot crafted in Python with a touch of Bash, seamlessly blends essential Discord server commands with a sophisticated integration that empowers users to effortlessly control their Minecraft server directly from within the Discord platform.

- [Installation](#installation)
- [Configuration](#configuration)
  - [Email](#email)
  - [Bot](#bot)
  - [Server](#server)
  - [Roles](#roles)
- [Usage](#usage)
- [Support](#support)
- [Contributing](#contributing)
- [License](#license)
- [Copyright](#copyright)
- [Acknowledgements](#acknowledgements)

## Installation

First, clone the repo:

```bash
git clone https://github.com/notoriouslogank/harbinger.git
```

Next, go ahead and install the requirements.  It is highly recommended to do so in a virtual environment, but you may install on bare metal at your own risk!

```bash
cd harbinger
pip install -r requirements.txt
```

In order for Harbinger to launch, you'll need to generate a configuration file.  This can be done in one of two (quite similar) manners:

```bash
python3 harbinger.py -c
```

or

```bash
python3 harbinger.py -C
```

The only difference between the two above listed methods is whether or not Harbinger subsequently launches once configuration is complete: '-c' flag to generate the configuration file only; '-C' flag to generate this configuration file and then launch Harbinger immediately afterward.

## Configuration

Once the configuration script has started, simply follow the onscreen prompts until the configuration completes.

The following serves as a quick guide to the keys and values for the config.ini file:

### Email

- address: An email address to send/receive bug reports. (Harbinger *does not* validate this.)
- password: The password to the email address, for automated logging in, sending mail, etc.

### Bot

- discord_token: The Discord API token for your bot.  You'll get that from the [Discord Developer Portal](https://discord.com/developers/docs/intro) when you're setting up your bot on the backend.
- bot_channel: The Channel ID for the channel you'd like to receive general bot status messages that have no specific context. Must be ``int``.
- delete_after: Amount of time, in seconds, before auto-deleting messages auto-delete. Must be ``int``.
- owner_id: The Member ID number for the bot's registered owner. Must be ``int``.
- custom_color: The RGB value for Harbinger's main color scheme in your server. Must be in format ``000 000 000``.

### Server

- server_dir: Path to the directory your Minecraft server is launched from. (Works with ~/ file paths.)
- startup_script: Path to the script used to launch your Minecraft server. (Works with ~/ file paths.)
- server_local_ip: The local, private IP address of the Minecraft server.
- server_public_ip: The public IP address of the Minecraft server.

### Roles

- moderator: The Role ID of the highest role in your server (used for checking Harbinger command permissions)
- developer: The Role ID of the developer role in your server (used for sending bot commands like !status, !up; can be same as moderator for higher security.)

Once you've provided all the necessary information to the configuration script, it will go ahead and write your (fully-encrypted) config.ini file.  Do not share this file -- or your key.key file -- with anyone you don't want to have *full access* to all bot functionality (as well as potentially cleartext passwords in some cases).

## Usage

All that's left at this point is to run your instance and let the magic happen.

This can be performed with two separate methods, listed below (beginning with the autorun method):

```bash
python3 run.py
```

When launched in this manner, Harbinger will automatically create a new tmux session with two panes and attach to it.  In the first pane, the Minecraft Server instance will launch; in the second pane, the Harbinger bot instance will launch simultaneously.  At this point, the tmux session can be safely detached and continue running in the background.

Please see the [tmux Github repository](https://github.com/tmux/tmux/wiki) for more information.

```bash
python3 harbinger.py
```

Using this method, Harbinger will start.  However, when launched directly in this way, it will *not* automatically begin a tmux session, nor will it launch the Minecraft Server instance (these must be done manually).

## Support

Please send any questions/comments/concerns to [logankdevemail@gmail.com] -- or submit an [issue](https://github.com/notoriouslogank/harbinger/issues)!

## Contributing

Feel free to submit a pull request if you have a new feature/bugfix/whatever -- I"ll take all the help I can get.

## License

MIT

## Copyright

notoriouslogank 2023

## Acknowledgements

[Jivanyatra](https://github.com/jivanyatra) for [zalgolib](https://github.com/jivanyatra/zalgolib/blob/master/src/zalgolib/zalgolib.py), which I rather shamelessly copied into this bot.
