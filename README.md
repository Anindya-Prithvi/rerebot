# Rerebot

## What is it?

**\<NEW>** Rerebot, tell me you have nitro without telling me you have nitro. I'll go first, Rerebot allows YOU to send actual messages to a channel as a BOT. It is also has file i/o and repeater capabilities
  
Rerebot ~~is currently~~was a file-i/o bot for discord made in discord.py. Now, it is much more. Current motive is inter-server communication using file-writes... Yes, that's outrageous lol. The idea sprouted out from no where and hence the project may contain a few cool features which maybe totally unrelated from the others. You may invite the ocassionally active bot using this [link](https://discord.com/api/oauth2/authorize?client_id=906607423916245063&permissions=377957387328&scope=bot). Operate the bot by prefixing `,rr ` to your messages.

## How to run (With conda):
1. Clone this repository
2. Install conda or miniconda ([skip?](https://github.com/Anindya-Prithvi/rerebot#how-to-run-without-conda))
3. Type in `conda env create --name discordBot -f environment.yml` to create an environment (the download size is currently very small)
4. Go to https://discord.com/developers/applications/ and create a bot account and obtain it's token. (There are many well explained tutorials for this online). You might also add the bot to your server.
5. Edit the file named `.env` inside this directory and add `token=<enter your token>`. Save the file and exit.
6. Inside the directory, on your shell/cmd, type `python main.py`. The bot is up and running! Play with it now. Type `!!help` in chat to get list of commands.

## How to run (without conda):
1. Clone this repository
2. Install python (if not already)
3. Install `discord.py` and `python-dotenv` using `pip install <package name>` command.
4. Follow the remaining steps from above.
