from typing import Awaitable
from Configs.Emojis import AEmojis
from discord import ButtonStyle, Interaction, Message, TextChannel
from discord.ui import Button, View
from Handlers.HandlerReply import HandlerResponse
from Messages.MessagesCategory import MessagesCategory
from Messages.MessagesManager import MessagesManager
from Music.AltushkaBot import AltushkaBot


class CallbackButtons(Button):
    """При нажатии кнопки она выполнит обратный вызов, передав аргументы и kwargs."""

    def __init__(self, bot: AltushkaBot, cb: Awaitable, emoji: AEmojis, textChannel: TextChannel, guildID: int, category: MessagesCategory, label=None, *args, **kwargs):
        super().__init__(label=label, style=ButtonStyle.secondary, emoji=emoji)
        self.__channel = textChannel
        self.__guildID = guildID
        self.__category = category
        self.__messagesManager = MessagesManager()
        self.__bot = bot
        self.__args = args
        self.__kwargs = kwargs
        self.__callback = cb
        self.__view: View = None

    async def callback(self, interaction: Interaction) -> None:
        """Callback to when Button is clicked"""
        # Return to Discord that this command is being processed
        await interaction.response.defer()

        response: HandlerResponse = await self.__callback(*self.__args, **self.__kwargs)

        message = None
        if response and response.view is not None:
            message: Message = await self.__channel.send(embed=response.embed, view=response.view)
            response.view.set_message(message)
        elif response.embed:
            message: Message = await self.__channel.send(embed=response.embed)

        # Clear the last sended message in this category and add the new one
        if message:
            await self.__messagesManager.addMessageAndClearPrevious(self.__guildID, self.__category, message, response.view)

    def set_view(self, view: View):
        self.__view = view

    def get_view(self) -> View:
        return self.__view
