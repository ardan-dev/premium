import discord
from discord.ext import commands
import datetime
import os
import json
import asyncio
from itertools import cycle

#client config

status = ["Prefix = 'p>'", 'ArdanKR_#9290', 'p>help', "접두사 = 'p>'", 'ArdanKR_#9290', 'p>도움말', 'Mention Me', '저를 호출해보세요']

client = commands.Bot(command_prefix = 'p>')
client.remove_command('help')

async def change_status():
    await client.wait_until_ready()
    msgs = cycle(status)

    while not client.is_closed:
        current_status = next(msgs)
        await client.change_presence(game=discord.Game(name=current_status, type=3))
        await asyncio.sleep(5)

#commands

@client.event
async def on_message(message):
    if message.content.startswith('d>userinfo'):
        date = datetime.datetime.utcfromtimestamp(((int(message.author.id) >> 22) + 1420070400000) / 1000)
        embed = discord.Embed(color=0x6184ff)

        embed.set_author(name=message.author.name + '#' + message.author.discriminator + "'s Profile")
        embed.add_field(name='**Nickname & Tag**', value=message.author.name + '#' + message.author.discriminator, inline=True)
        embed.add_field(name='**In-Server Name**', value=message.author.display_name, inline=True)
        embed.add_field(name='**Account creation date**', value=str(date.year) + 'Y ' + str(date.month) + 'M ' + str(date.day) + 'D ', inline=True)
        embed.add_field(name='**User ID**', value=message.author.id, inline=True)
        embed.set_thumbnail(url=message.author.avatar_url)
        embed.set_footer(text='Requested by • ' + message.author.name + '#' + message.author.discriminator)

        await client.send_message(message.channel, embed=embed)

    if message.content.startswith('d>list'):
        list = []
        for server in client.servers:
            list.append(server.name)
        await client.send_message(message.channel, "\n".join(list))

    if message.content.startswith('d>avatar'):
        date = datetime.datetime.utcfromtimestamp(((int(message.author.id) >> 22) + 1420070400000) / 1000)
        embed = discord.Embed(color=0x6184ff)

        embed.set_author(name=message.author.name + '#' + message.author.discriminator + "'s Avatar")
        embed.set_thumbnail(url=message.author.avatar_url)
        embed.set_footer(text='Requested by • ' + message.author.name + '#' + message.author.discriminator, icon_url=message.author.avatar_url)

        await client.send_message(message.channel, embed=embed)

    if message.content.startswith('d>developer'):
        date = datetime.datetime.utcfromtimestamp(((int(message.author.id) >> 22) + 1420070400000) / 1000)
        embed = discord.Embed(color=0x6184ff)

        embed.set_author(name='Credits')
        embed.add_field(name='Master Developer', value='``ArdanKR_#9290``', inline=True)
        embed.add_field(name='Code', value='``PYTHON``', inline=False)
        embed.add_field(name='Hosting', value='``Heroku 24 hour``', inline=False)
        embed.add_field(name='Other', value='`Copyright ⓒ 2019 ArdanKR_#9290 All right reserved`', inline=False)
        await client.send_message(message.channel, embed=embed)

    if message.content.startswith('d>help'):
        date = datetime.datetime.utcfromtimestamp(((int(message.author.id) >> 22) + 1420070400000) / 1000)
        embed = discord.Embed(color=0x6184ff)

        embed.set_author(name='DST Bot Command List')
        embed.add_field(name='**General Command**', value='``d>help`` , ``d>avatar`` , ``d>list`` , ``d>userinfo`` , ``d>about``', inline=True)
        embed.add_field(name='**Bot Information**', value='``d>delvoper``', inline=False)
        embed.add_field(name='**Other**', value='`Copyright ⓒ 2019 ArdanKR_ All right reserved`', inline=False)
        embed.set_footer(text='Thanks to use DST Bot. If you have an error or problem, please contact ArdanKR_#9290')
        await client.send_message(message.channel, embed=embed)

    if message.content.startswith('d>about'):
        date = datetime.datetime.utcfromtimestamp(((int(message.author.id) >> 22) + 1420070400000) / 1000)
        embed = discord.Embed(color=0x6184ff)

        embed.set_author(name='About Bot')
        embed.add_field(name='Version', value='**0.1 **', inline=True)
        embed.add_field(name='󠀀󠀀 󠀀󠀀', value='󠀀󠀀 󠀀󠀀')
        embed.add_field(name='DST Bot#7380 BOT Profile', value='󠀀󠀀 󠀀󠀀')
        embed.add_field(name='**Nickname & Tag**', value='DST Bot#7380', inline=True)
        embed.add_field(name='**Bot ID**', value='604886711578787841', inline=True)
        embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/606346201784123396/606792801635663881/1564741015418.png')
        embed.set_footer(text='DST Bot By ArdanKR_#9290', icon_url='https://cdn.discordapp.com/attachments/603214980707516416/606795951037743123/1564741015418.png')

        await client.send_message(message.channel, embed=embed)

    if message.content.startswith('<@604886711578787841>'):
        date = datetime.datetime.utcfromtimestamp(((int(message.author.id) >> 22) + 1420070400000) / 1000)
        embed = discord.Embed(color=0x6184ff)

        await client.send_message(message.channel, "'d>help' to see bot command list")



#client setting
client.loop.create_task(change_status())
access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
