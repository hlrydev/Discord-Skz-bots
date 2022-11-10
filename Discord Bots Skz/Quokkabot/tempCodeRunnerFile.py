
import os
from discord.ext import commands

client = commands.Bot(command_prefix = '.')
def main():
    client.add_cog(Commands(client))
