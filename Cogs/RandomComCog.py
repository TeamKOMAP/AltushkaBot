from random import randint, random
from Music.AltushkaBot import AltushkaBot
from discord.ext.commands import Context, command, Cog
from Configs.Descriptions import Descriptions
from Configs.Embeds import AEmbeds

import discord
import datetime


helper = Descriptions()


class RandomCog(Cog):
    def __init__(self, bot: AltushkaBot):
        self.__embeds = AEmbeds()

    @command(name='random', help=helper.HELP_RANDOM, description=helper.HELP_RANDOM_LONG, aliases=['rand'])
    async def random(self, ctx: Context, arg: str) -> None:
        try:
            arg = int(arg)

        except:
            embed = self.__embeds.ERROR_NUMBER()
            await ctx.send(embed=embed)
            return None

        if arg < 1:
            a = arg
            b = 1
        else:
            a = 1
            b = arg

        x = randint(a, b)
        embed = self.__embeds.RANDOM_NUMBER(a, b, x)
        await ctx.send(embed=embed)

    @command(name='Komaru', help=helper.HELP_CARA, description=helper.HELP_CARA_LONG, aliases=['Komugi'])
    async def cara(self, ctx: Context) -> None:
        x = random()
        if x < 0.5:
            result = 'Komaru'
        else:
            result = 'Komugi'

        embed = self.__embeds.KOMARU_KOMUGI(result)
        await ctx.send(embed=embed)

    @command(name='choose', help=helper.HELP_CHOOSE, description=helper.HELP_CHOOSE_LONG, aliases=['pick'])
    async def choose(self, ctx, *args: str) -> None:
        try:
            user_input = " ".join(args)
            itens = user_input.split(sep=',')

            index = randint(0, len(itens)-1)

            embed = self.__embeds.CHOSEN_THING(itens[index])
            await ctx.send(embed=embed)
        except:
            embed = self.__embeds.BAD_CHOOSE_USE()
            await ctx.send(embed=embed)

    @command(name='purge', help=helper.HELP_PURGE, description=helper.HELP_PURGE_LONG,
             aliasses=["pur", "delete", "del"])
    async def purge(self, ctx: Context, arg: int) -> None:
        if not ctx.author.guild_permissions.manage_messages:
            delete_embed = discord.Embed(
                title=":x: Нет разрешения",
                color=0xff9999)

            if ctx.author.avatar:
                avatar_url = ctx.author.avatar.url
            else:
                avatar_url = ctx.author.default_avatar.url
            delete_embed.set_footer(text=f"{ctx.author.name}・{datetime.datetime.now().strftime('%I:%M:%S %p')}",
                                    icon_url=avatar_url)
            await ctx.send(embed=delete_embed, delete_after=20)
            return

        if arg is None:
            delete_embed = discord.Embed(
                title=":warning: Warning!",
                description=f"> Вы должны указать действительный ** номер**, чтобы удалить сообщения в {ctx.channel.mention}!",
                color=0xffffcc)
            if ctx.author.avatar:
                avatar_url = ctx.author.avatar.url
            else:
                avatar_url = ctx.author.default_avatar.url
            delete_embed.set_footer(text=f"{ctx.author.name}・{datetime.datetime.now().strftime('%I:%M:%S %p')}",
                                    icon_url=avatar_url)
            await ctx.send(embed=delete_embed, delete_after=20)
            return

        await ctx.channel.purge(limit=arg + 1)
        success_embed = discord.Embed(
            title=":white_check_mark: Очистка успешна",
            description=f"> Успешно удалено `{arg} сообщений` в {ctx.channel.mention}!",
            color=0xb3ffb3)
        if ctx.author.avatar:
            avatar_url = ctx.author.avatar.url
        else:
            avatar_url = ctx.author.default_avatar.url
        success_embed.set_footer(text=f"{ctx.author.name}・{datetime.datetime.now().strftime('%I:%M:%S %p')}",
                                 icon_url=avatar_url)
        await ctx.send(embed=success_embed, delete_after=20)




def setup(bot):
    bot.add_cog(RandomCog(bot))
