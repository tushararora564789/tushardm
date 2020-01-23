import discord
from discord.ext.commands import Bot
from discord.ext import commands
from discord.ext.commands.cooldowns import BucketType
import asyncio
import platform
import colorsys
import random
import os
import time
from discord.voice_client import VoiceClient
from discord import Game, Embed, Color, Status, ChannelType


Forbidden= discord.Embed(title="Permission Denied", description="1) Please check whether you have permission to perform this action or not. \n2) Please check whether my role has permission to perform this action in this channel or not. \n3) Please check my role position.", color=0x00ff00)
client = Bot(description="DarkBot Bot is best", command_prefix="n!", pm_help = True)
client.remove_command('help')


async def status_task():
    while True:
        await client.change_presence(game=discord.Game(type=1,name='with TRIVIA NATION 2.0'))
        await asyncio.sleep(5)
        await client.change_presence(game=discord.Game(type=1,name='Joined Till Now '+str(len(set(client.get_all_members())))+' users'))
        await asyncio.sleep(5)
        await client.change_presence(game=discord.Game(type=1,name='with KESHAV RAJ ᴳᵒᵈ'))
        await asyncio.sleep(5)
        

	
@client.event
async def on_ready():
    print('Logged in as '+client.user.name+' (ID:'+client.user.id+') | Connected to '+str(len(client.servers))+' servers | Connected to '+str(len(set(client.get_all_members())))+' users')
    print('--------')
    print('--------')
    print('Started TRIVIA NATION 2.O')
    print('Created by KESHAV RAJ ᴳᵒᵈ')
    client.loop.create_task(status_task())


@client.event
async def on_message(message):
	await client.process_commands(message)

@client.event
async def on_member_join(member):
    print("In our server" + member.name + " just joined")
    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
    embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
    embed.set_author(name='Welcome message')
    embed.add_field(name = '**__Welcome to Our Server TRIVIA NATION 2.0__**',value ='**Hope you will be active here. Check Our server <#610816633287606274> and never try to break any rules**. ',inline = False)
    embed.set_image(url = 'https://cdn.discordapp.com/attachments/610828452442013737/610897950201217048/390.gif')
    embed.set_thumbnail(url=member.avatar_url)
    embed.set_footer(text=f"created by KESHAV RAJ ᴳᵒᵈ#7735",icon_url="https://cdn.discordapp.com/attachments/609581567135842314/609937606964281365/JPEG_20190811_080005.jpg")
    await client.send_message(member,embed=embed)
    print("Sent message to " + member.name)
    channel = discord.utils.get(client.get_all_channels(), server__name='TRIVIA NATION 2.0', name='welcome')
    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
    embed = discord.Embed(title=f'❤{member.server.name} ❤', description=' **Do not forget to check <#610816633287606274> and never try to break any one of them**', color = discord.Color((r << 16) + (g << 8) + b))
    embed.add_field(name='__Thanks for joining__', value=member.name, inline=True)
    embed.add_field(name='Your join position is', value=member.joined_at)
    embed.set_image(url = 'https://cdn.discordapp.com/attachments/610828452442013737/610898014059495424/tenor.gif')
    embed.set_thumbnail(url=member.avatar_url)
    embed.set_footer(text=f"created by KESHAV RAJ ᴳᵒᵈ#7735",icon_url="https://cdn.discordapp.com/attachments/609581567135842314/609937606964281365/JPEG_20190811_080005.jpg")
    await client.send_message(channel, embed=embed)


client.run('NjEwMTc0NzU0Nzc5MDM3Njk2.XVDwuw.alVmHrb6uJi6LTuZsjNQelY_yqE')
