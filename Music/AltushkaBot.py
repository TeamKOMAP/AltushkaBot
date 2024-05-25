from asyncio import AbstractEventLoop
from discord import Guild, Status, Game, Message
from discord.ext.commands.errors import CommandNotFound, MissingRequiredArgument
from Configs.Configs import AConfigs
from discord.ext.commands import Bot, Context
from Configs.Messages import Messages
from Configs.Embeds import AEmbeds


class AltushkaBot(Bot):
    def __init__(self, listingSlash: bool = False, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__listingSlash = listingSlash
        self.__configs = AConfigs()
        self.__messages = Messages()
        self.__embeds = AEmbeds()
        self.remove_command("help")

    @property
    def listingSlash(self) -> bool:
        return self.__listingSlash

    def startBot(self) -> None:
        """Функция блокировки, которая запустит бота"""
        if self.__configs.BOT_TOKEN == '':
            print('DEVELOPER NOTE -> Token not found')
            exit()

        super().run(self.__configs.BOT_TOKEN, reconnect=True)

    async def startBotCoro(self, loop: AbstractEventLoop) -> None:
        """Запустить сопрограмму бота, не ждет установления соединения"""
        task = loop.create_task(self.__login())
        await task
        loop.create_task(self.__connect())

    async def __login(self):
        """Сопрограмма для входа в бот в Discord"""
        await self.login(token=self.__configs.BOT_TOKEN)

    async def __connect(self):
        """Сопрограмма для подключения бота в Discord"""
        await self.connect(reconnect=True)

    async def on_ready(self):
        if self.__listingSlash:
            print(self.__messages.STARTUP_MESSAGE)
        await self.change_presence(status=Status.online, activity=Game(name=f"Альтушка для скуфа | {self.__configs.BOT_PREFIX}help"))
        # статус бота формата "Играет в name"
        if self.__listingSlash:
            print(self.__messages.STARTUP_COMPLETE_MESSAGE)

    async def on_command_error(self, ctx, error):
        if isinstance(error, MissingRequiredArgument):
            embed = self.__embeds.MISSING_ARGUMENTS()
            await ctx.send(embed=embed)

        elif isinstance(error, CommandNotFound):
            embed = self.__embeds.COMMAND_NOT_FOUND()
            await ctx.send(embed=embed)

        else:
            print(f'DEVELOPER NOTE -> Command Error: {error}')
            embed = self.__embeds.UNKNOWN_ERROR()
            await ctx.send(embed=embed)

    async def process_commands(self, message: Message):
        if message.author.bot:
            return

        ctx = await self.get_context(message, cls=Context)

        if ctx.valid and not message.guild:
            return

        await self.invoke(ctx)


class Context(Context):
    bot: AltushkaBot
    guild: Guild
