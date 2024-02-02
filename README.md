# Harbinger

Harbinger, a Discord bot crafted in Python with a touch of Bash, seamlessly blends essential Discord server commands with a sophisticated integration that empowers users to effortlessly control their Minecraft server directly from within the Discord platform.

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

In order for Harbinger to launch, you'll need to supply it with a configuration file.  The Harbinger repository contains a tool to help you in this task: ``harbinger/config/configure.py``. Before we can generate the config file, however, we need to generate some cryptographic keys (to ensure no secret tokens, passwords, et al leak from the config file if it were erroneously (or maliciously) shared).

A detailed explanation of Fernet key cryptography -- and symmetric encryption more generally -- can be fround in the documentation for the [cryptography](https://cryptography.io/en/latest/fernet/) module we'll use to generate our key(s).

You will need to have a Fernet key generated and placed in the proper location: by default, Harbinger looks for the Fernet key file called ``key.key`` within the config/ directory:

```bash
cd config
python3
```

From the Python interactive shell, run the following commands (if you'd rather, this can be saved as a script (with a .py extension) and run directly, ie ``python3 script_name.py``).:

```python
from cryptography.fernet import Fernet
key = Fernet.generate_key()
with open("config/key.key", "wb") as key_file:
    key_file.write(key)
```

Once you've generated this file (config/key.key), make sure you *do not misplace it*: it will be required to encrypt and decrypt your configuration file as needed; if you lose this key, you will have to generate a new key (and, therefore, a new config file).  Now we can create our configuration file (Harbinger will use our keyfile by default for the encryption):

```bash
python3 config/configure.py
```

Follow the onscreen prompts to provide the Harbinger config file with all of the necessary data.  The config.ini key/value pairs are described in the following section.

## config.ini

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

- server_dir: An absolute path to the directory your Minecraft server is launched from.
- startup_script: An absolute path to the script used to launch your Minecraft server.
- server_local_ip: The local, private IP address of the Minecraft server.
- server_public_ip: The public IP address of the Minecraft server.

### Roles

- moderator: The Role ID of the highest role in your server (used for checking Harbinger command permissions)
- developer: The Role ID of the developer role in your server (used for sending bot commands like !status, !up; can be same as moderator for higher security.)

Once you've provided all the necessary information to the configuration script, it will go ahead and write your (fully-encrypted) config.ini file.  Do not share this file -- or your key.key file -- with anyone you don't want to have *full access* to all bot functionality (as well as potentially cleartext passwords in some cases).

## Usage

All that's left at this point is to run your instance and let the magic happen:

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

## Acknowledgements

[Jivanyatra](https://github.com/jivanyatra) for [zalgolib](https://github.com/jivanyatra/zalgolib/blob/master/src/zalgolib/zalgolib.py), which I rather shamelessly copied into this bot.
