import discord
from discord.ext import commands
import os
import asyncio
from dotenv import load_dotenv
import youtube_dl


load_dotenv()
DISCORD_TOKEN = os.getenv("ODUwMTgzNDA3ODExMTY2MjQw.YLmBAA.mpKA90OW26FC6Ldw59tFONHMLcE")

intents = discord.Intents().all()
client = discord.Client(intents=intents)
bot = commands.Bot(command_prefix='!',intents=intents)


youtube_dl.utils.bug_reports_message = lambda: ''

ytdl_format_options = {
    'format': 'bestaudio/best',
    'restrictfilenames': True,
    'noplaylist': True,
    'nocheckcertificate': True,
    'ignoreerrors': False,
    'logtostderr': False,
    'quiet': True,
    'no_warnings': True,
    'default_search': 'auto',
    'source_address': '192.168.0.5' 
}

ffmpeg_options = {
    'options': '-vn'
}

ytdl = youtube_dl.YoutubeDL(ytdl_format_options)

class YTDLSource(discord.PCMVolumeTransformer):
    def __init__(self, source, *, data, volume=0.5):
        super().__init__(source, volume)
        self.data = data
        self.title = data.get('title')
        self.url = ""

    @classmethod
    async def from_url(cls, url, *, loop=None, stream=False):
        loop = loop or asyncio.get_event_loop()
        data = await loop.run_in_executor(None, lambda: ytdl.extract_info(url, download=not stream))
        if 'entries' in data:
            data = data['entries'][0]
        filename = data['title'] if stream else ytdl.prepare_filename(data)
        return filename


@bot.command(name='play', help='To play song')
async def play(ctx,url):

    try :
        server = ctx.message.guild
        voice_channel = server.voice_client

        async with ctx.typing():
            filename = await YTDLSource.from_url(url, loop=bot.loop)
            voice_channel.play(discord.FFmpegPCMAudio(executable="ffmpeg.exe", source=filename))
        await ctx.send('**Now playing:** {}'.format(filename))
    except:
        await ctx.send("Llamabot is not connected to a voice channel.")


@bot.command(name='join', help='Tells the bot to join the voice channel')
async def join(ctx):
    if not ctx.message.author.voice:
        await ctx.send("{} is not connected to a voice channel".format(ctx.message.author.name))
        return
    else:
        channel = ctx.message.author.voice.channel
    await channel.connect()


@bot.command(name='pause', help='This command pauses the song')
async def pause(ctx):
    voice_client = ctx.message.guild.voice_client
    if voice_client.is_playing():
        await voice_client.pause()
    else:
        await ctx.send("Llamabot is not playing anything at the moment.")
    
@bot.command(name='resume', help='Resumes the song')
async def resume(ctx):
    voice_client = ctx.message.guild.voice_client
    if voice_client.is_paused():
        await voice_client.resume()
    else:
        await ctx.send("Llamabot was not playing anything before this. Use play command")
    

@bot.command(name='leave', help='To make the bot leave the voice channel')
async def leave(ctx):
    voice_client = ctx.message.guild.voice_client
    if voice_client.is_connected():
        await voice_client.disconnect()
    else:
        await ctx.send("Llamabot is not connected to a voice channel.")

@bot.command(name='stop', help='Stops the song')
async def stop(ctx):
    voice_client = ctx.message.guild.voice_client
    if voice_client.is_playing():
        await voice_client.stop()
    else:
        await ctx.send("Llamabot is not playing anything at the moment.")
    
    await bot.process_commands()


@bot.event
async def on_ready():
    print('{0.user} HAS JOINED THE PARTY!'.format(bot))
    for guild in bot.guilds:
        for channel in guild.text_channels :
            if str(channel) == "general" :
                await channel.send('Llamabot activated!')
                await channel.send(file=discord.File('C://Users//Infol//OneDrive//Documents//.vscode//Discord Bots Skz//Llamabot//Hyunjin hi.gif'))
        print('Active in {}\n Member Count : {}'.format(guild.name,guild.member_count))


@bot.event
async def on_message(message):

    if message.content.startswith('Hello'):
        await message.channel.send('Hi')

    if message.content.startswith('LLAMA'):
        await message.channel.send('WHAT')
    
    if message.content.startswith('ANSWER'):
        await message.channel.send('I AM TRYING')
    
    if message.content.startswith('Sunhi'):
        await message.channel.send('Doll!')

    if message.content.startswith('How are you?'):
        await message.channel.send('Am doing awesome. And you?')
    
    if message.content.startswith('HYUNJIN'):
        await message.channel.send('WHAT')

    if message.content.startswith('Hyunjin'):
        await message.channel.send('Yeah?')

    if message.content.startswith('Americano'):
        await message.channel.send('Americano, chowa chowa')

    if message.content.startswith('Fuck'):
        await message.channel.send('YOUR BEHAVIOR IS SO *UGH*')

    if message.content.startswith('Bangchan'):
        await message.channel.send('AUSSIEEEEEEEEEEEEEEEEEEEEEEEEEEEEE, WOAH!')

    if message.content.startswith('Felix'):
        await message.channel.send('AUSSIEEEEEEEEEEEEEEEEEEEEEEEEEEEEE, WOAH!')
    
    if message.content.startswith('Han'):
        await message.channel.send('JISUNG')

    if message.content.startswith('Jisung'):
        await message.channel.send('JISUNG')

    if message.content.startswith('Hyundai'):
        await message.channel.send('What-')
    
    if message.content.startswith('Seungmin'):
        await message.channel.send('He is like a puppy TT')

    if message.content.startswith('IN'):
        await message.channel.send('THE BABY')

    if message.content.startswith('Jeongin'):
        await message.channel.send('THE BABY')
    
    if message.content.startswith('Minho'):
        await message.channel.send('He is old')

    if message.content.startswith('Lee Know'):
        await message.channel.send('He is old')

    if message.content.startswith('Changbin'):
        await message.channel.send('Dwaekki')

    await bot.process_commands(message)

@bot.command()
@commands.is_owner()
async def shutdown(ctx):
    print("Llamabot out.")
    exit()

if __name__ == "__main__" :
    bot.run('ODUwMTgzNDA3ODExMTY2MjQw.YLmBAA.mpKA90OW26FC6Ldw59tFONHMLcE')