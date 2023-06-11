import os

DISCORD_TOKEN = os.environ.get("DISCORD_TOKEN")
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")

SYSTEM_PROMPT = "Generate code for discord bot for the following usecase"
BOT_COMMAND_PREFIX = "!bot"