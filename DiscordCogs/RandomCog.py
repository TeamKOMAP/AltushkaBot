from random import randint, random
from Music.AltushkaBot import AltushkaBot
from discord.ext.commands import Context, command, Cog
from Config.Helper import Helper
from Config.Embeds import AEmbeds

helper = Helper()


class RandomCog(Cog):
    """Class to listen to commands of type Random"""

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

        embed = self.__embeds.CARA_COROA(result)
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


def setup(bot):
    bot.add_cog(RandomCog(bot))
