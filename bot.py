import discord
from discord.ext import commands

client = commands.Bot(command_prefix = 'imp.')

@client.event
async def on_ready():
    print('Bot is ready.')

@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)}ms')

import random

@client.command(aliases=['8ball', 'test'])
async def _8ball(ctx, *, question):
    responses = ['It is certain.',
                'It is decidedly so.',
                'Without a doubt.',
                'Yes - definitely.',
                'You may rely on it.',
                'As I see it, yes.',
                'Most likely.',
                'Outlook good.',
                'Yes.',
                'Signs point to yes.',
                'Reply hazy, try again.',
                'Ask again later.',
                'Better not tell you now.',
                'Cannot predict now.',
                'Concentrate and ask again.',
                'Don\'t count on it.',
                'My reply is no.',
                'My sources say no.',
                'Outlook not so good.',
                'Very doubtful.']
    await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')
def c_f_conversion(start_temp):
    new_temp = (start_temp * 9/5) + 3200
    return new_temp
def f_c_conversion(start_temp):
    new_temp = (start_temp - 3200) * 5/9
    return new_temp
def k_c_conversion(start_temp):
    new_temp = start_temp - 27315
    return new_temp
def c_k_conversion(start_temp):
    new_temp = start_temp + 27315
    return new_temp


@client.command()
async def temp(ctx, *, conversion):
    conversion_scrub = conversion.upper()
    conversion_split = conversion_scrub.split()
    start_temp = conversion_split[0]
    int_temp = int(start_temp[:-1])
    int_temp *= 100
    if 'C' in start_temp:
        if 'F' in conversion_split[2]:
            new_temp = c_f_conversion(int_temp)
            degree = 'Fahrenheit'
        if 'K' in conversion_split[2]:
            new_temp = c_k_conversion(int_temp)
            degree = 'Kelvin'

    elif 'F' in start_temp:
        if 'C' in conversion_split[2]:
            new_temp = f_c_conversion(int_temp)
            degree = 'Celcius'
        if 'K' in conversion_split[2]:
            new_temp = c_k_conversion(f_c_conversion(int_temp))
            degree = 'Kelvin'
    elif 'K' in start_temp:
        if 'C' in conversion_split[2]:
            new_temp = k_c_conversion(int_temp)
            degree = 'Celcius'
        if 'F' in conversion_split[2]:
            new_temp = c_f_conversion(k_c_conversion(int_temp))
            degree = 'Fahrenheit'
    else:
        await ctx.send(f'The Correct format is Exp:`imp.temp 10F to C`')
    await ctx.send(f'{start_temp} is {(int(new_temp)/100)} {degree}')




client.run('')
