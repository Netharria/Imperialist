import random

import discord
from discord.ext import commands

import length
import temperature
import volume
import weight

bot = commands.Bot(command_prefix="imp.")


@bot.event
async def on_ready():
    await bot.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.watching, name="over her vast colonies."
        )
    )
    print("Bot is ready.")


@bot.command()
async def ping(ctx):
    embed = discord.Embed(
        title="**Ping**", description=f"Pong! {round(bot.latency * 1000)}ms"
    )
    embed.set_author(name=f"{bot.user.display_name}", icon_url=bot.user.avatar_url)
    await ctx.send(embed=embed)


# 8ball random answer


def is_in_channel():
    def predicate(ctx):
        return ctx.channel.id == 390318225440768000

    return commands.check(predicate)


def has_permissions():
    def predicate(ctx):
        return ctx.author.guild_permissions.manage_messages is True

    return commands.check(predicate)


@bot.command(aliases=["8ball"])
@commands.check_any(is_in_channel(), has_permissions())
async def _8ball(ctx, *, question):
    responses = [
        "It is certain.",
        "It is decidedly so.",
        "Without a doubt.",
        "Yes - definitely.",
        "You may rely on it.",
        "As I see it, yes.",
        "Most likely.",
        "Outlook good.",
        "Yes.",
        "Signs point to yes.",
        "Reply hazy, try again.",
        "Ask again later.",
        "Better not tell you now.",
        "Cannot predict now.",
        "Concentrate and ask again.",
        "Don't count on it.",
        "My reply is no.",
        "My sources say no.",
        "Outlook not so good.",
        "Very doubtful.",
    ]
    professions = [
        "healthcare professional",
        "artist",
        "business professional",
        "transport engineer",
        "military officer",
        "accountant",
        "social worker",
        "ship captain",
        "vocalist",
        "linguist",
        "musician",
        "HR representative",
        "scientist",
        "home inspector",
        "cable technician",
        "plumber",
        "electrian",
        "structural engineer",
        "arborist",
    ]
    embed = discord.Embed(
        title=f"**Magic 8Ball**",
        description=f"**Question: {question}\n\nAnswer: {random.choice(responses)}**",
        color=0x8000FF,
    )
    embed.set_author(name=f"{ctx.author.display_name}", icon_url=ctx.author.avatar_url)
    embed.set_footer(
        text=f"This is not intended to give actual advice. | "
        f"For actual advice, please consult a trained {random.choice(professions)}."
    )
    await ctx.send(embed=embed)


@bot.command()
async def roll(ctx, *, limit=100):
    embed = discord.Embed(
        title=f"**Roll**", description=f"**{random.randint(1, int(limit))}/{limit}**"
    )
    embed.set_author(name=f"{bot.user.display_name}", icon_url=bot.user.avatar_url)
    await ctx.send(embed=embed)


# temp Commands
@bot.command()
async def temp(ctx, start_temp, start_unit, word, destination_unit):
    result = temperature.convert_temp(
        float(start_temp), start_unit, destination_unit
    )
    start_unit = temperature.convert_units(start_unit)
    end_unit = temperature.convert_units(destination_unit)
    if result is False:
        await ctx.send(f"The Correct format is Exp:`imp.temp 10 F to C`")
    else:
        embed = discord.Embed(
            title=f"**Temperature Conversions**",
            description=f"{start_temp} {start_unit} is {result:.2f} {end_unit}",
        )
        embed.set_author(name=f"{bot.user.display_name}", icon_url=bot.user.avatar_url)
        await ctx.send(embed=embed)


# Length command
@bot.command(aliases=["len"])
async def _len(ctx, start_len, start_unit, word, destination_unit):
    result = length.convert_length(
        float(start_len), start_unit, destination_unit
    )
    start_unit = length.convert_unit(start_unit)
    end_unit = length.convert_unit(destination_unit)
    if result is False:
        await ctx.send(
            f"The Correct format is Exp:`imp.len 10 km to mi`   Valid units are km m cm mm mi yd ft in"
        )
    else:
        embed = discord.Embed(
            title=f"**Length Conversions**",
            description=f"{start_len} {start_unit} is {result:.4f} {end_unit}",
        )
        embed.set_author(name=f"{bot.user.display_name}", icon_url=bot.user.avatar_url)
        await ctx.send(embed=embed)


# Length command
@bot.command()
async def wgt(ctx, start_wgt, start_unit, word, destination_unit):
    result = weight.convert_wgt(float(start_wgt), start_unit, destination_unit)
    start_unit = weight.convert_unit(start_unit)
    end_unit = weight.convert_unit(destination_unit)
    if result is False:
        await ctx.send(
            f"The Correct format is Exp:`imp.wgt 180 lb to kg`  Valid units are kg g lb oz"
        )
    else:
        embed = discord.Embed(
            title=f"Weight Conversions",
            description=f"{start_wgt} {start_unit} is {result:.2f} {end_unit}",
        )
        embed.set_author(name=f"{bot.user.display_name}", icon_url=bot.user.avatar_url)
        await ctx.send(embed=embed)


@bot.command()
async def vol(ctx, start_vol, start_unit, word, destination_unit):
    result = volume.convert_vol(float(start_vol), start_unit, destination_unit)
    start_unit = volume.convert_units(start_unit)
    end_unit = volume.convert_units(destination_unit)
    if result is False:
        await ctx.send(
            f"The Correct format is Exp:`imp.vol 180L to gal`  Valid units are L mL gal qt pt c oz tbsp tsp"
        )
    else:
        embed = discord.Embed(
            title=f"Volume Conversions",
            description=f"{start_vol} {start_unit} is {result:.2f} {end_unit}",
        )
        embed.set_author(name=f"{bot.user.display_name}", icon_url=bot.user.avatar_url)
        await ctx.send(embed=embed)


with open("token", "r") as f:
    bot.run(f.readline().strip())
