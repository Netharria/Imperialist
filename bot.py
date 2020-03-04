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

#8ball random answer

@client.command(aliases=['8ball'])
@commands.has_permissions(manage_messages=True)
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

#temp conversions
def c_f_conversion(start_temp):
    new_temp = (start_temp * 9/5) + 32
    return new_temp
def f_c_conversion(start_temp):
    new_temp = (start_temp - 32) * 5/9
    return new_temp
def k_c_conversion(start_temp):
    new_temp = start_temp - 273.15
    return new_temp
def c_k_conversion(start_temp):
    new_temp = start_temp + 273.15
    return new_temp

#temp Commands
@client.command()
async def temp(ctx, *, conversion):
    conversion_scrub = conversion.upper()
    conversion_split = conversion_scrub.split()
    start_temp = conversion_split[0]
    int_temp = float(start_temp[:-1])
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
    await ctx.send(f'{start_temp} is {new_temp:.2f} {degree}')

#Length Conversions to meters
def km_m_conversion(start_len):
    new_len = start_len * 1000
    return new_len
def cm_m_conversion(start_len):
    new_len = start_len / 100
    return new_len
def mm_m_conversion(start_len):
    new_len = start_len / 1000
    return new_len
def mi_m_conversion(start_len):
    new_len = start_len * 1609.344
    return new_len
def yd_m_conversion(start_len):
    new_len = start_len * 0.9144
    return new_len
def ft_m_conversion(start_len):
    new_len = start_len * 0.3048
    return new_len
def in_m_conversion(start_len):
    new_len = start_len * .0254
    return new_len

#Length Conversions from meters
def m_km_conversion(start_len):
    new_len = start_len / 1000
    return new_len
def m_cm_conversion(start_len):
    new_len = start_len * 100
    return new_len
def m_mm_conversion(start_len):
    new_len = start_len * 1000
    return new_len
def m_mi_conversion(start_len):
    new_len = start_len * 0.00062137119223733
    return new_len
def m_yd_conversion(start_len):
    new_len = start_len * 1.0936132983377
    return new_len
def m_ft_conversion(start_len):
    new_len = start_len * 3.2808398950131
    return new_len
def m_in_conversion(start_len):
    new_len = start_len * 39.370078740157
    return new_len

#Length command
@client.command(aliases=['len'])
async def _len(ctx, *, conversion):
    conversion_scrub = conversion.lower()
    conversion_split = conversion_scrub.split()
    start_len = conversion_split[0]
    end_conv = conversion_split [2]
    int_len = float(start_len[:-2])
    new_len = 0
    unit = ''
    if 'km' in start_len:
        meter_conv = km_m_conversion(int_len)
    elif 'cm' in start_len:
        meter_conv = cm_m_conversion(int_len)
    elif 'mm' in start_len:
        meter_conv = mm_m_conversion(int_len)
    elif 'mi' in start_len:
        meter_conv = mi_m_conversion(int_len)
    elif 'yd' in start_len:
        meter_conv = yd_m_conversion(int_len)
    elif 'ft' in start_len:
        meter_conv = ft_m_conversion(int_len)
    elif 'in' in start_len:
        meter_conv = in_m_conversion(int_len)
    elif 'm' in start_len:
        meter_conv = float(start_len[:-1])
    else:
        await ctx.send(f'The Correct format is Exp:`imp.len 10km to mi`  Valid units are km m cm mm mi yd ft in')
    if end_conv == 'm':
        new_len = meter_conv
        unit = 'Meters'
    else:
        if 'km' in end_conv:
            new_len = m_km_conversion(meter_conv)
            unit = 'Kilometers'
        elif 'cm' in end_conv:
            new_len = m_cm_conversion(meter_conv)
            unit = 'Centimeters'
        elif 'mm' in end_conv:
            new_len = m_mm_conversion(meter_conv)
            unit = 'Millimeters'
        elif 'mi' in end_conv:
            new_len = m_mi_conversion(meter_conv)
            unit = 'Miles'
        elif 'yd' in end_conv:
            new_len = m_yd_conversion(meter_conv)
            unit = 'Yards'
        elif 'ft' in end_conv:
            new_len = m_ft_conversion(meter_conv)
            unit = 'Feet'
        elif 'in' in end_conv:
            new_len = m_in_conversion(meter_conv)
            unit = 'Inches'
        else:
            await ctx.send(f'The Correct format is Exp:`imp.len 10km to mi`   Valid units are km m cm mm mi yd ft in')
    await ctx.send(f'{start_len} is {new_len:.4f} {unit}')



#weight conversion to grams
def kg_g_conversion(start_wgt):
    new_wgt = start_wgt * 1000
    return new_wgt
def lb_g_conversion(start_wgt):
    new_wgt = start_wgt * 453.5924
    return new_wgt
def oz_g_conversion(start_wgt):
    new_wgt = start_wgt * 28.349556839727
    return new_wgt

#weight conversion from grams
def g_kg_conversion(start_wgt):
    new_wgt = start_wgt / 1000
    return new_wgt
def g_lb_conversion(start_wgt):
    new_wgt = start_wgt * 0.002204622476038
    return new_wgt
def g_oz_conversion(start_wgt):
    new_wgt = start_wgt * 0.03527392
    return new_wgt
#Length command
@client.command()
async def wgt(ctx, *, conversion):
    conversion_scrub = conversion.lower()
    conversion_split = conversion_scrub.split()
    start_wgt = conversion_split[0]
    end_conv = conversion_split [2]
    int_wgt = float(start_wgt[:-2])
    new_wgt = 0
    unit = ''
    if 'kg' in start_wgt:
        grams_conv = kg_g_conversion(int_wgt)
    elif 'lb' in start_wgt:
        grams_conv = lb_g_conversion(int_wgt)
    elif 'oz' in start_wgt:
        grams_conv = oz_g_conversion(int_wgt)
    elif 'g' in start_wgt:
        grams_conv = float(start_wgt[:-1])
    else:
        await ctx.send(f'The Correct format is Exp:`imp.wgt 180lb to kg`  Valid units are kg g lb oz')
    if end_conv == 'g':
        new_wgt = grams_conv
        unit = 'Grams'
    else:
        if 'kg' in end_conv:
            new_wgt = g_kg_conversion(grams_conv)
            unit = 'Kilograms'
        elif 'lb' in end_conv:
            new_wgt = g_lb_conversion(grams_conv)
            unit = 'Pounds'
        elif 'oz' in end_conv:
            new_wgt = g_oz_conversion(grams_conv)
            unit = 'Ounces'
        else:
            await ctx.send(f'The Correct format is Exp:`imp.wgt 180lb to kg`  Valid units are kg g lb oz')
    await ctx.send(f'{start_wgt} is {new_wgt:.2f} {unit}')
with open("token","r") as f:
    client.run(f.readline().strip())
