import discord
from discord.ext import commands
import openai
from config import TOKEN, OPENAI_API_KEY
from openai_api import generate_code

intents = discord.Intents.default()
intents.typing = False
intents.presences = False

bot = commands.Bot(command_prefix="!bot", intents=intents)

openai.api_key = OPENAI_API_KEY

@bot.event
async def on_ready():
    print(f"{bot.user.name} is online!")

@bot.command()
async def code(ctx, *, user_message: str):
    systemprompt = "Generate code for discord bot for the following usecase"
    userprompt = user_message

    gpt_message = generate_code(systemprompt, userprompt)

    await ctx.send(f"```{gpt_message}```")

if __name__ == "__main__":
    bot.run(TOKEN)