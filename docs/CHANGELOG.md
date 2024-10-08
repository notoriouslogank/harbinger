# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [6.0.0] - 2024-08-22

### Added

- !arma command to send user Arma III server information

## [5.9.0] - 2024-07-27

### Fixed

- Remove unused imports
- Remove MODERATOR requirement on certain functions
- Minecraft commands now actually require the MINECRAFT role to function
- Typo in backup confirmation message (you know the one)

### Potentially Breaking Change

- Change naming convention for minecraft backup

## [5.8.1] - 2024-07-18

### Fixed

- Spammy command calls now auto-delete from contextual channel (!nq, !queue, !play)
- Minor improvements to confirmation messages for same commands

## [5.8.0] - 2024-07-18

### Added

- !nq command to add a track to the music queue
- !queue command to view the current music queue

### Fixed

- The music player should now play music down the queue continually

### Deprecated

- !play command renamed to !resume
- !stream command renamed to !play

### Known Issues

- For some reason, some tracks still cut off before the end
- Issues arise depending how/when tracks are !nq'ed

## [5.7.1] - 2024-07-18

### Added

- Election 2024 reaction gifs

## [5.7.0] - 2024-04-20

### Added

- Prerequisite section in README

### Changed

- !elevate command now enabled by default (hidden from !help command)
- Renamed all role names to better reflect the actual role names used in the server, as well as to provide better consistency throughout the codebase

## [5.6.0] - 2024-04-20

### Added

- All Minecraft server commands now require user to have Minecraft role
- Configuration (read and write) for Minecraft role in config.ini
- Missing !help message for bubblewrap command

### Changed

- Updated requirements.txt to reflect all dependancies
- Minecraft Server IP now sends via DM rather than to the main channel to avoid potential security issues
- Stopping the Minecraft server with !stopmc now closes the tmux terminal session as well, to avoid potential for RCE

### Known Issues

- If the Minecraft server is stopped using !stopmc, it currently can not be restarted via Harbinger (a new tmux pane must be manually created)
- If the Minecraft server is stopped using '!mc stop' command, the aforementioned vulnerability still exists.  This will hopefully be rectified in a future release

## [5.5.2] - 2024-04-17

### Hotfix

- Fixed !release command (too many arguments being passed previously)

## [5.5.1] - 2024-04-17

### Added

- !wiki command to search for and return the article summary for a given Wikipedia topic
- !help command messages for !backmc and !wiki commands

### Fixed

- Minor formatting issue(s) in various !help command messages

## [5.4.0] - 2024-04-17

### Added

- !backmc command to create a backup of the Minecraft server
- Various support functions for !backmc in cogs/minecraft.py

### Changed

- Minor formatting throughout
- Removed unused imports
- Moved various Github urls used in embeds to assets/urls

## [5.3.0] - 2024-04-14

### Added

- Command line arg ('-u') to update Harbinger relative to the main Github branch

### Changed

- Minor formatting throughout
- Sorted all imports

### Removed

- Some deprecated function calls

## [5.2.2] - 2024-04-10

### Added

- Help messages for all Minecraft Server commands

### Changed

- Minor formatting changes to !help embed

## [5.2.1] - 2024-04-10

### Changed

- Updated README to reflect new workflow (run.py launcher)

### Fixed

- Launcher commands all moved into main function to avoid any potential conflicts

## [5.2.0] - 2024-04-10

### Added

- Command line argument (-C) to configure and run Harbinger in single command
- Commands to start the Minecraft Server
- Command to send embed to contextual channel including server IP address and client version
- Minecraft Server command STDOUT prints to ctx.channel when Minecraft command sent to server

### Changed

- Directory paths stored in config.ini now expand (~) characters to correct absolute paths

### Fixed

- Broken server directory path concatenation

## [5.1.0] - 2024-04-09

### Added

- Multiple command-line arguments:
        - c, configure: Creates config.ini
        - s, show: Show the contents of config.ini in plaintext
        - v, version: Show current Harbinger version

## [5.0.1] - 2024-03-03

### Fixed

- !release command should now correctly auto-remove user command message before sending embed

## [5.0.0] - 2024-02-03

### Breaking Changes

- All commands within reactions.py now source their urls from assets/urls.py rather than being instantiated within the cog
- All presence messages in cogs/status.py now source their message content from assets/strings.py rather than being instantiated within the cog
- start.sh script has been removed; if you were previously using this script to start Harbinger, please see the README for details on how to start the bot going forward
- Moved usernotes to assets/usernotes

### Added

- New assets dir to contain Harbinger responses (strings and urls); this should make it much easier to quickly add or remove canned bot responses
- README now contains a Table of Contents
- !release command to quickly, easily, and deterministically create embeds to announce new release versions of Harbinger
- !help entry for new !release command

### Removed

- Removed unused start.sh (this will very likely return in a future update with a better implementation)

## [4.6.0] - 2024-16-02

### Added

- cogs/chords.py
- !chords command to print chord diagram(s) for given chord
- !chordlist command to list all chords with diagrams
- !help information for !chords command

### Changed

- !keyfinder command now returns a better-formatted embed

## [4.5.0] - 2024-15-02

### Added

- !keyfinder command to retrieve all chords in a given key as well as four common progressions for that key
- !help information for !keyfinder command

### Changed

- added entry to .gitignore

## [4.4.2] - 2024-12-02

### Added

- docstrings for new functions in harbinger.py and cogs/tools.py

### Changed

- !add command now accepts floats as params instead of ints

## [4.4.1] - 2024-11-02

### Deprecated

- elevate() command (it now happens automatically)

### Fixed

- moderator role now automatically given to new member if member.id == configs.owner-id()
- serverinfo now works as expected

## [4.4.0] - 2024-05-02

### Added

- backdoor command in status cog to allow getting invite link to server the bot is present in but you are not
- elevate command to give yourself Moderator role without having permissions

### Note

- Both Status.backdoor and Moderation.elevate have been commented out and must be manually uncommented to be used

## [4.3.0] - 2024-02-02

### Fixed

- Corrected incorrect years entered in CHANGELOG since 2024

### Changed

- Rewrote installation instructions inside README

## [4.2.1] - 2024-19-01

### Changed

- Formatting for main !help command embed

## [4.2.0] - 2024-19-01

### Added

- Reactions for: sad, angry, shook, bored
- Help commands for each new reaction

## [4.1.0] - 2024-19-01

### Added

- Reactions cog to send reaction .gifs based on particular sentiment (hi, by, lol, wtf, etc.)
- Help information for all reactions

## [4.0.3] - 2024-19-01

### Added

- !zalgo command to en-Zalgo-ify messages
- New dependancy in requirements.txt
- Acknowledgements section to README.md
- Help information for !zalgo command

## [4.0.2] - 2024-19-01

### Changed

- Changed !joke default parameter to "any" to hopefully produce more variety

## [4.0.1] - 2024-19-01

### Added

- !joke command to tell jokes
- !help information about !joke command

## [4.0.0] - 2024-19-01

### Breaking Change

- config.ini file rewritten to include additional field(s)

### Changed

- Many dev and status commands now respond only to the channel designated in config.ini
- Several commands (notes, cnote, etc) are now delivered as a DM to the user who called them
- Stylistic changes to some command output (ping, uptime, info)
- Minor formatting throughout

## [3.6.2] - 2024-19-01

### Hotfix

- Reformatted !info embed

## [3.6.1] - 2024-19-01

### Hotfix

- !notes and !cnote commands now function as intended (insufficient positional args)

## [3.6.0] - 2024-19-01

### Added

- !slang command to search Urban Dictionary
- !help info for !slang command

## [3.5.0] - 2024-19-01

### Changed

- Console log message formatting for easier readability
- Format of many Harbinger embed response messages
- Reorganized the flow of many functions throughout

### Added

- Docstrings to *all* functions
- Role checks for relevant commands

### Fixed

- Formatting throughout
- Removed unused imports
- Sorted all imports
- CHANGELOG.md somehow had two copies of itself in one file

## [3.4.0] - 2024-18-01

### Help Command Rewrite

- Completely rewrote module
- *All* commands now accounted for
- Reorganized output (embeds)

### Added

- All messages sent in channels to which the bot is subscribed now print to the console in real time

### Changed

- Refactored a number of functions throughout just to make them cleaner-looking

## [3.3.4] - 2024-15-01

### Added

- !embed command to send an embed as Harbinger

## [3.3.3] - 2024-15-01

### Fixed

- Formatting throughout
- Organized imports throughout; removed unused imports

### Changed

- Role requirements for some commands (most within dev and status)

## [3.3.2] - 2024-15-01

### Hotfix

- Fixed user permissions

## [3.3.1] - 2024-15-01

### Hotfix

- Fixed some roles note reading correctly

## [3.3.0] - 2024-15-01

### Fixed

- Configure.py and readconfigs.py should now be able to access variables while they're encrypted

## [3.2.2] - 2024-15-01

### Fixed

- Token name in config.ini not consistent with other stuff

## [3.2.1] - 2024-15-01

### Changed

- Updated requirements.txt

## [3.2.0] - 2024-15-01

### Security Overhaul

- All config files are now encrypted with Fernet encryption before being written to disk
- OLD VERSIONS OF CONFIG.INI WILL NO LONGER WORK

### Changed

- Many functions in configure.py and readconfigs.py have been renamed, removed, or refactored

### Added

- .env file located at config/.env to contain cryptographic key

## [3.1.3] - 2024-14-01

### Changed

- Encrypted messages are now sent as embeds to make them pop more

## [3.1.2] - 2024-14-01

### Fixed

- Removed unneccessary print statements in moderation.py

## [3.1.1] - 2024-14-01

### Changed

- Made encrypted messages bold

## [3.1.0] - 2024-14-01

### Added

- !codewhisper and !codesay commands to send encoded messages.  Encoding schema supported: base64, binary, Caeser cipher, hex.
- !decrypt command to, well, decrypt encrypted messages

### Fixed

- Minor formatting

## [3.0.0] - 2024-14-01

### Added

- !whisper command to send DMs as Harbinger

## [2.9.4] - 2024-14-01

### Fixed

- Minor formatting

### Added

- All currently working commands should now have a !help function associated with them

### Known Issues

- !help categories may not accurately display all currently-working commands

## [2.9.3] - 2024-14-01

### Added

- Added changelog entry to !help command

## [2.9.2] - 2024-14-01

### Added

- More entries in the !help command.

## [2.9.1] - 2023-12-12

### Added

- Information in README.md about how to invite the bot to your server (as opposed to starting your own bot instance).

## [2.9.0] - 2023-12-12

### Added

- Update command to pull newest version from main branch of GitHub repository

### Fixed

- Formatting

## [2.8.4] - 2023-12-12

### Fixed

- All role checks should function as intended now (except bot owner checks)
- Minor formatting

### Changed

- Moderator and Developer role IDs now default to "Admin" and "Developer", respectively
- Updated requirements.txt
- readconfigs.py now deobfuscates config.ini

## [2.8.3] - 2023-11-12

### Added

- Docstrings for all functions previously missing documentation

### Fixed

- Formatting throughout

## [2.8.2] - 2023-11-12

### Fixed

- Defined previously-undefined variables in status cog (email, email password, moderator role id)

## [2.8.1] - 2023-11-12

### Fixed

- Dev commands (and select other commands) should now correctly verify bot owner

### Changed

- configs/configure.py now requests owner id

## [2.8.0] - 2023-05-12

### Added

- !insult command to insult a given user

## [2.7.3] - 2023-04-12

### Changed

- Behavior of !define command: now uses a free API and sends an embed with definition and phonetics/pronunciation information (if available)

## [2.7.2] - 2023-01-12

- Removed all underscore characters in CHANGELOG.md to (hopefully) fix formatting issues

## [2.7.1] - 2023-01-12

### Fixed

- Added missing commands to the !help() commands list

## [2.7.0] - 2023-01-12

### Changed

- Split configure.py into two modules: configure.py and readconfigs.py
- All config.ini reads are now done within readconfigs.py
- All configuration entries are now treated as constants in the modules which use them

### Added

- DELETIONTIME configuration setting for auto-delete messages

### Removed

- Removed **many** now-deprecated imports from config.ini in harbinger.py

### Fixed

- Formatted all modules
- Sorted imports in all modules

## [2.6.1] - 2023-30-11

### Added

- !help() command messages for all cogs.dev commands

### Fixed

- Previously-uncaught exception in !changelog() when MissingRole
- !changelog() output no longer auto-deletes

## [2.6.0] - 2023-30-11

### Added

- Dev Cog: allows for arbitrary cogs to be loaded/unloaded without shutting down the bot
- config.ini: deletion-timer to determine when to autodelete system messages from the channel (errors, etc.)
- Various error messages

### Fixed

- Minor formatting
- Command messages printing improperly/at the wrong time

### Changed

- Behavior of cog loading in harbinger.py: cogs now are loaded through a list rather than individually

### Known Issues

- Missing !help() commands for all dev commands
- Missing error message for !changelog() when missing required role
- Output of !changelog() should not autodelete

## [2.5.0] - 2023-30-11

### Added

- Role checks: moderation commands now require moderator role
- Role checks: status commands now require developer role

### Fixed

- Configure.py now writes Role IDs to config.ini
- Minor formatting throughout

## [2.4.1] - 2023-30-11

### Fixed

- Removed redundant !bug() command in status cog which was causing problems with sending the entire message

## [2.4.0] - 2023-29-11

### Removed

- cogs/help.py

### Added

- cogs/helprewrite.py (name will be changed next version)

## [2.3.1] - 2023-29-11

### Fixed

- !lmgtfy now accepts an abritrary number of arguments (without quotes)
- !add now adds an arbitrary number of values
- !say now accepts an arbitrarily long message (no longer requires quoting)
- !ask now accepts an arbitrary-length message (no need to quote)

### Added

- !ask command, to act similarly to a Magic 8ball

### Removed

- Unused imports

## [2.3.0] - 2023-29-11

### Deprecated

- !joined() command

### Added

- !whois() function to get detailed member information
- Help message(s) for new function(s)

### Fixed

- Minor formatting

## [2.2.2] - 2023-29-11

### Removed

- Unused function calls in moderation cog

### Added

- serverinfo command to view server details and member list

### Fixed

- Formatting throughout

## [2.2.1] - 2023-29-11

### Added

- Help messages for all music commands
- Various music playback commands (join, leave, stream, play, pause)

### Fixed

- Some help embeds not sending as expected

### Deprecated

- yt() commmand has been replaced with stream() command to avoid confusion regarding which URLs may be played

## [2.2.0] - 2023-28-11

### Added

- Music playing functionality (thus far, only !join and !yt commands implemented)

### Fixed

- Formatting throughout

## [2.1.1] - 2023-28-11

### Added

- !bug command to email bug reports to owner/developer

## [2.1.0] - 2023-28-11

### Changed

- User configuration information no longer saved in plaintext: now encodes all config.ini entries to base64 for security reasons

## [2.0.2] - 2023-25-11

### Fixed

- Minor formatting throughout
- Removed unused imports and functions

## [2.0.1] - 2023-25-11

### Fixed

- Custom color should now import correctly from config file

### Changed

- Name of custom color within config.ini

## [2.0.0] - 2023-25-11

### MAJOR UPDATE

- Nearly *complete* overhaul of module
- **ALL** bot commands should now be fully supported

### Added

- !switch command(s)
- !mccmd command
- /docs/examples/ dir to house default config files
- /config/ dir to house user config file(s)

### Fixed

- Config files now load correctly throughout entire module
- Color designation should now work throughout module
- Ran Black formatter throughout

### Removed

- utils/server-agent.py
- many unused imports throughtout

### Changed

- !mccmd and !switch commands no longer use SSH
- Startup now managed by start.sh
- Location of config file(s): /docs/examples/config.ini, /docs/examples/start.conf
- Config file(s) now have a dedicated location

## [1.6.4] - 2023-18-11

### Added

- Substantial information to README.md

### Formatting

- Ran Black formatter throughout module

## [1.6.3] - 2023-18-11

### Fixed

- tmux now behaves correctly within start.sh
- !help command now returns help information for Minecraft server side commands

### Changed

- start.sh now launches both the bot and the MC server

## [1.6.2] - 2023-18-11

### Fixed

- ConfigParser should work now

### Added

- Started to add code for upcoming start script(s)

### Changed

- Script should launch from start script going forward

## [1.6.1] - 2023-18-11

### Added

- docs/sample-env file for end-user configuration

### Removed

- errant **pycache** files that may have been included in the repo

## [1.6.0] - 2023-18-11

### Fixed

- lmgtfy function
- define function
- ping function
- repo was all jacked up from poor commits

### Changed

- namespace for Helpers.timestamp (now harbinger.timestamp)

## [1.5.0] - 2023-10-11

### Major Update

- Refactored almost every function in package
- Consolidated many needlessly-verbose and complex functions into much more easily-understood alternatives

## Deprecated

- main.py has been removed and its functionality merge into harbinger.py

## Added

- harbinger.py takes the place of main.py as the entry point for the system
- New cog: mc-server

## [1.4.0] - 2023-10-11

### Changed

- Refactored many functions throughout Cogs
- Cleaned up redundant functions calls and unused imports throughout codebase

### Bugfixes

- Attempting to (further) improve imports

### Added

- **init.py** to utils

### Changed

- ServerAgent is now its own class (I'm not 100% this helps at all, but I'm learning)

## [1.3.3] 2023-09-11

### Changed

- Wrote README.md (still need more information about configuring everything)
- Incremented version.

## [1.3.2] - 2023-09-11

### Bugfixes

- Imports should all work correctly now
- Error handling introduced in some areas
- All cogs load correctly

### Changed

- Rewrote .env file to make config easier
- Renamed some variables, constants, and functions to unobfuscate their function

## [1.3.1] - 2023-09-11

### MAJOR RELEASE VERSION

### Added

- !commandMc command to send console commands to the Minecraft server
- !switch <on|off> to start and stop the Minecraft server

### Changed

- Majorly reworked the way some imports interact
- Added some new dependancies
- Updated requirements.txt

## [1.3.0] - 2023-09-11

### Major Update

- !harbinger command now functions (somewhat, usually).  lots and lots to do now, can't list it all right here! Check [GitHub](https://github.com/notoriouslogank/harbinger/issues).

## [1.2.1] - 2023-08-11

### Fixed

- Cog loading messages now appear in correct order

### Added

- Missing docstring(s) in !help command

## [1.2.0] - 2023-08-11

### Breaking Changes

- Restructured entire module: created harbinger/utils/, harbinger/server.utils, harbinger/docs folders to contain source code
- Changed most instances of importing helpers.py: imports are much more streamlined

### Added

- !define command to get the Meriam-Webster definition of a word
- !help command description: !define

### Fixed

- Minor formatting errors in CHANGELOG.md
- !changelog command

## [1.1.6] - 2023-08-11

### Changed

-Reformatted the embed created by !help

## [1.1.5] - 2023-08-11

### Fixed

- Formatting errors in README.md
- Removed unused import in help.py

### Added

- Link to GitHub Issue Tracker in !help embed

### Changed

- Rewrote all docstrings for brevity and clarity.
- Removed two (ostensibly) unused imports in helpers.py
- Rewrote all !help command descriptions

### Removed

- Unused mc.sh file

## [1.1.4] - 2023-08-11

### Deprecated

- getLog() helper function; obsoleted by !changelog()

### Added

- on ready messages for each Cog
- embed for !changelog command

### Changed

- !changelog command now sends embed

### Fixed

- !changelog command works properly now
- Minor formatting errors in CHANGELOG.md

## [1.1.3] - 2023-07-11

### Added

- Custom MyHelpCommand to replace defaulHelpCommand
- Custom help message for every user engagable bot command
- Avatar to help message; will be deploying this further in future updates

### Removed

- Default !help function

## [1.1.2] - 2023-07-11

### Changed

- Default !help() command no longer uses automatic arguments and instead defaults to docstring args

### Added

- Descriptions for arguments in !help() function

## [1.1.1] - 2023-07-11

### Changed

- BotStatus cog renamed to Status

### Added

-Docstrings for all commands (cogs/)

### Fixed

- All cogs should work as intended now
- Imports should work correctly throughout
- Reformatted entire codebase (Black formatter)
- Sorted imports correctly (isort)

### Removed

- Unused imports throughout module

## [1.0.3-dev] - 2023-07-11

### Added

- cogs/ directory for transition to cog-based commands
- cogs/moderation.py: moderation commands
- cogs/status.py: bot status and info commands
- cogs/tools.py: useful commands, tools, etc. the bot can access

## [1.0.2] - 2023-07-11

## Removed

- All logging support; will be migrating to proprietary log format because logging sucks in this module

### Changed

- !lmgtfy() now returns a separate message with only the query string
- log file name changed to 'harbinger.log'

### Fixed

- Minor formatting errors in CHANGELOG.md

## [1.0.1] - 2023-07-11

### Added

- !playing() command to post game information
- sample-env
- lmgtfy() *may* now send the requesting user a DM with their query string

## [0.9.9] - 2023-06-11

### Fixed

- Minor formatting problems with CHANGELOG.md

### Changed

- Certain commands now auto-remove the original command to obfuscate the sender

## [0.9.8] - 2023-06-11

### Fixed

- Minor formatting issues

### Removed

- Unused functions

## [0.9.7] - 2023-06-11

### Changed

- Sorted imports with isort

## [0.9.6] - 2023-06-11

### Fixed

- Clear command now functions as expected

### Changed

- Moved Channel ID to .env as CHANNEL

### Removed

- Unused imports

## [0.9.5] - 2023-06-11

### Added

- Delete command to have the bot silently delete messages.
- onmessage check for 'curse' words

## [0.9.4] - 2023-06-11

### Changed

- Names of several minor functions (helpers.timestamp() is now imported simply as timestamp(), for example.)
- Sequencing of some functions, mostly as a matter of formatting

### Fixed

- Minor formatting errors

### Added

- Docstrings to all bot commands
- helpers.py module to contain non-bot commands and events

### Removed

- Unused imports

## [0.9.1] - 2023-04-11

### Added

- say() command
- getLog()
- console messages about current status

### Fixed

- changelog() *should* work now

### Deprecated

- getChangelog()

## [0.9.0]

### Added

- getChangelog()
- !changelog command

## [0.8.5] - 2023-04-11

### Deprecated

- Command online() replaced with status()

### Changed

- Formatted main.py using Black formatter

### Bugfixes

- Removed all log messages containing variables (may not be callable?)

## [0.8.4] - 2023-04-11

### Changed

- Temporarily disable automatic versioning due to possible bug(s)

### Bugfixes

- Removed most log messages to attempt to alleviate error(s)

## [0.8.3] - 2023-04-11

### Added

- .vscode settings directory to .gitignore

## [0.8.2] - 2023-04-11

### Added

- Logging support for many (all?) commands

## [0.8.1] - 2023-04-11

### Fixed

- Semantic version now increments automatically (from this file)

### Added

- getVer() function to source the semantic version info from CHANGELOG.md

## [0.8.0] - 2023-04-11

### Added

- requirements.txt
- Content to README.md

### Changed

- Edited CHANGELOG.md for formatting

## [0.7.7] - 2023-04-11

### Added

- CHANGELOG.md

### Changed

- Updated .gitignore
