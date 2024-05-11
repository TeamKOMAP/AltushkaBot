from discord import Embed
from discord.ext.commands import Cog, command
from Config.Configs import AConfigs
from Config.Helper import Helper
from Config.Colors import AColors
from Music.AltushkaBot import AltushkaBot
from Config.Embeds import AEmbeds

helper = Helper()


class ControlCog(Cog):
    """Class to handle discord events"""

    def __init__(self, bot: AltushkaBot):
        self.__bot = bot
        self.__config = AConfigs()
        self.__colors = AColors()
        self.__embeds = AEmbeds()
        self.__commands = {
            'MUSIC': ['resume', 'pause', 'loop', 'stop',
                      'skip', 'play', 'queue', 'clear',
                      'np', 'shuffle', 'move', 'remove',
                      'reset', 'prev', 'history', 'volume'],
            'RANDOM': ['choose', 'cara', 'random']

        }

    @command(name="help", help=helper.HELP_HELP, description=helper.HELP_HELP_LONG, aliases=['h'])
    async def help_msg(self, ctx, command_help=''):
        if command_help != '':
            for command in self.__bot.commands:
                if command.name == command_help:
                    txt = command.description if command.description else command.help

                    embedhelp = Embed(
                        title=f'**Информация о команде {command_help}**',
                        description=txt,
                        colour=self.__colors.BLUE
                    )

                    await ctx.send(embed=embedhelp)
                    return

            embedhelp = Embed(
                title='Все команды!',
                description=f'Команды {command_help} не существует, используй {self.__config.BOT_PREFIX}help для просмотра всех команд',
                colour=self.__colors.BLACK
            )

            await ctx.send(embed=embedhelp)
        else:

            helptxt = ''
            help_music = '🎧 `MUSIC`\n'
            help_random = '🎲 `RANDOM`\n'
            help_help = '👾 `HELP`\n'

            for command in self.__bot.commands:
                if command.name in self.__commands['MUSIC']:
                    help_music += f'**{command}** - {command.help}\n'

                elif command.name in self.__commands['RANDOM']:
                    help_random += f'**{command}** - {command.help}\n'

                else:
                    help_help += f'**{command}** - {command.help}\n'

            helptxt = f'\n{help_music}\n{help_help}\n{help_random}'
            helptxt += f'\n\nИспользуй {self.__config.BOT_PREFIX}help "command" для подробной информации о конкретной команде'
            embedhelp = Embed(
                title=f'**{self.__bot.user.name} знает эти команды**',
                description=helptxt,
                colour=self.__colors.BLUE
            )

            if self.__bot.user.avatar != None:
                embedhelp.set_thumbnail(url=self.__bot.user.avatar)
            await ctx.send(embed=embedhelp)

    @command(name='invite', help=helper.HELP_INVITE, description=helper.HELP_INVITE_LONG, aliases=['inv'])
    async def invite_bot(self, ctx):
        invite_url = self.__config.INVITE_URL.format(self.__bot.user.id)
        txt = self.__config.INVITE_MESSAGE.format(invite_url, invite_url)

        embed = Embed(
            title="Заказать Альтушку",
            description=txt,
            colour=self.__colors.BLUE
        )

        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(ControlCog(bot))
