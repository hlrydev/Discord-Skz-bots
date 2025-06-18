import discord
intents = discord.Intents(messages=True, guilds=True)
intents.reactions = True
import random
from discord.ext import commands
client2 = commands.Bot(command_prefix='?', intents=intents)


@client2.event
async def on_message(message):
    if message.author == client2.user:
        return

    if message.content.startswith('Hello'):
        await message.channel.send('STRAY KIDS IN THE BUILDING WE ARE GONNA GO ALL IN')

    if message.content.startswith('Hi'):
        await message.channel.send('STRAY KIDS IN THE BUILDING WE ARE GONNA GO ALL IN')

    if message.content.startswith('AH'):
        await message.channel.send('2020 WE GONNA GET EM')

    if message.content.startswith('Why'):
        await message.channel.send('This is for "aMerICanO. chOwA ChOWa. pAmPARAMpAmpaM-"')
    
    if message.content.startswith('HAN'):
        await message.channel.send('NOONAAAA!!!')

    if message.content.startswith('Te voy a dar'):
        await message.channel.send('No le peguen a la Quokka')

    if message.content.startswith('...'):
        await message.channel.send('GAY')
    
    if message.content.startswith('QUOKKA'):
        await message.channel.send('AH AH AH AH AH')

    if message.content.startswith('Who?'):
        await message.channel.send('tHis iS Mr.hAn')

    if message.content.startswith('What?'):
        await message.channel.send('JEOGIYO NOONA HOKSHI NAMJACHINGU ISSEOYO?')
    
    if message.content.startswith('yeah'):
        await message.channel.send('Goose goose, the language only Han Jisung can speak')

    if message.content.startswith('NO'):
        await message.channel.send('Oh, I am sorry...', delete_after=3.0)

    if message.content.startswith('I LOVE YOU'):
        await message.channel.send('I love you too!')

    if message.content.startswith('MARRY ME'):
        await message.channel.send('I cannot')

    if message.content.startswith('OMG'):
        await message.channel.send('HOOOOOOLY MOLY')

    if message.content.startswith('Han'):
        await message.channel.send('Yeah?')

    if message.content.startswith('Jisung'):
        await message.channel.send('Yeah?')

    if message.content.startswith('How are you?'):
        await message.channel.send('Yeah good, thanks. How about you?')

    if message.content.startswith('Hyunjin'):
        await message.channel.send('LLAMA')

    if message.content.startswith('WHAT'):
        await message.channel.send('ANSWER')

    if message.content.startswith('I AM TRYING'):
        await message.channel.send('TRY HARDER')
    
    if message.content.startswith('Felix'):
        await message.channel.send('FELIIIIIX')
    
    if message.content.startswith('Minho'):
        await message.channel.send('Lee Know hyung')

    if message.content.startswith('Lee Know'):
        await message.channel.send('Lee Know hyung')

    if message.content.startswith('Bangchan'):
        await message.channel.send('CHAAAAAAAAAAAAN HYUUUUUUUUUUNG')

    if message.content.startswith('IN'):
        await message.channel.send('IN!')

    if message.content.startswith('Jeongin'):
        await message.channel.send('IN!')

    if message.content.startswith('Changbin'):
        await message.channel.send('pAbBit hYuNG')

    if message.content.startswith('Seungmin'):
        await message.channel.send('AWWWWWWWWWWWWW')

    if message.content.startswith('Stray Kids'):
        await message.channel.send('YEAAAAAAAAAAAAAAH')

    if message.content.startswith('Lee Know'):
        await message.channel.send('Minho hyung')
    
    if message.content.startswith('I hope your behavior is not ugh.'):
        await message.channel.send('Hyunjin-')

    if message.content.startswith('JISUNG'):
        await message.channel.send('Going!')

    if message.content.startswith("Qball"):
        lucky_num = random.randint(0,len(responses) - 1)
        await message.channel.send(responses[lucky_num])

    await client2.process_commands(message)



@client2.event
async def on_member_join(member):
     for channel in member.guild.text_channels :
         if str(channel) == "general" :
             on_mobile=False
             if member.is_on_mobile() == True :
                 on_mobile = True
             await channel.send("You have joined the party! {}!!\n On Mobile : {}".format(member.name,on_mobile))  


@client2.event
async def on_ready():
    print('{0.user} HAS JOINED THE PARTY!'.format(client2))
    for guild in client2.guilds:
        for channel in guild.text_channels :
            if str(channel) == "general" :
                await channel.send('Quokkabot activated!')
                await channel.send(file=discord.File('C://Users//Infol//OneDrive//Documents//.vscode//Discord Bots Skz//Quokkabot//Jisung hi.gif'))


@client2.command(help = "Prints details of Server")
async def where_am_i(ctx):
    owner=str(ctx.guild.owner)
    region = str(ctx.guild.region)
    guild_id = str(ctx.guild.id)
    memberCount = str(ctx.guild.member_count)
    icon = str(ctx.guild.icon_url)
    desc=ctx.guild.description
    
    embed = discord.Embed(
        title=ctx.guild.name + " Server Information",
        description=desc,
        color=discord.Color.blue()
    )
    embed.set_thumbnail(url=icon)
    embed.add_field(name="Owner", value=owner, inline=True)
    embed.add_field(name="Server ID", value=guild_id, inline=True)
    embed.add_field(name="Region", value=region, inline=True)
    embed.add_field(name="Member Count", value=memberCount, inline=True)

    await ctx.send(embed=embed)


@commands.command()
async def shutdown(self,ctx):
    if ctx.message.author.id == 804097211347632148:
      print("shutdown")
      try:
        await self.bot.logout()
      except:
        print("EnvironmentError")
        self.bot.clear()
    else:
      await ctx.send("You do not own the Quokkabot!")

@client2.command()
@commands.is_owner()
async def shutdown(ctx):
    print("#SalvenALasQuokkas.")
    exit()


responses = ['I guess yeah', 'Cannot answer, leave the quokka to sleep', 'I will tell you later', 'Idk, ask Hyunjin', 'Concentrate my friend', 'I do not think so', 'Certainly yup', 'Maybe.', 'Mmmmm almost sure.', 'Ehhhh no.', 'Chan says no', 'That does not look good', 'That looks good.', 'I aint replying', 'Almost a yeah.', 'Think about it', 'Definitely', 'YES.', 'Yes', 'Count on it.']


client2.run('ODA0MjE5Mzc0MjMwNTY4OTgw.YBJJqA._PkHXYg5eI0MchLnjKrnvrXVpic')
