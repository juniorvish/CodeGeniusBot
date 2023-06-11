import discord
from discord.ext import commands
from openai_api import generate_code

class CodeGeniusBot(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def bot(self, ctx, *, user_message: str):
        systemprompt = "Generate code for discord bot for the following usecase"
        userprompt = user_message

        generated_code = generate_code(systemprompt, userprompt)

        await ctx.send(f"```{generated_code}```")

def setup(bot):
    bot.add_cog(CodeGeniusBot(bot))