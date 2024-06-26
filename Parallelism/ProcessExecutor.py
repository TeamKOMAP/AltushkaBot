from typing import List
from discord import Button, Guild, TextChannel
from discord.ui import View
from Configs.Emojis import AEmojis
from Messages.MessagesCategory import MessagesCategory
from Music.Playlist import Playlist
from Music.AltushkaBot import AltushkaBot
from Configs.Messages import Messages
from Music.Song import Song
from Configs.Embeds import AEmbeds
from UI.Buttons.HandlerButtons import HandlerButtons
from UI.Views.BasicView import BasicView
from Messages.MessagesManager import MessagesManager
from Handlers.PrevHandler import PrevHandler
from Handlers.PauseHandler import PauseHandler
from Handlers.SkipHandler import SkipHandler
from Handlers.StopHandler import StopHandler
from Handlers.ResumeHandler import ResumeHandler
from Handlers.LoopHandler import LoopHandler
from Handlers.QueueHandler import QueueHandler


class ProcessCommandsExecutor:
    MESSAGES = Messages()
    EMBEDS = AEmbeds()
    EMOJIS = AEmojis()
    MSG_MANAGER = MessagesManager()

    def __init__(self, bot: AltushkaBot, guildID: int) -> None:
        self.__bot = bot
        self.__guildID = guildID
        self.__messagesManager = MessagesManager()
        self.__messages = Messages()
        self.__embeds = AEmbeds()
        self.__emojis = AEmojis()

    @classmethod
    async def sendNowPlayingToGuild(cls, bot: AltushkaBot, playlist: Playlist, channel: TextChannel, song: Song, guild: Guild) -> None:
        # Get the lock of the playlist
        if playlist.isLoopingOne():
            title = cls.MESSAGES.ONE_SONG_LOOPING
        else:
            title = cls.MESSAGES.SONG_PLAYING

        # Create View and Embed
        embed = cls.EMBEDS.SONG_INFO(song.info, title)
        view = cls.__getPlayerViewForGuild(channel, guild.id, bot)
        # Send Message and add to the MessagesManager
        message = await channel.send(embed=embed, view=view)
        await cls.MSG_MANAGER.addMessageAndClearPrevious(guild.id, MessagesCategory.NOW_PLAYING, message, view)

        # Set in the view the message witch contains the view
        view.set_message(message=message)

    @classmethod
    def __getPlayerViewForGuild(cls, channel: TextChannel, guildID: int, bot: AltushkaBot) -> View:
        buttons = cls.__getPlayerButtonsForGuild(channel, guildID, bot)
        view = BasicView(bot, buttons)
        return view

    @classmethod
    def __getPlayerButtonsForGuild(cls, textChannel: TextChannel, guildID: int, bot: AltushkaBot) -> List[Button]:
        """Create the Buttons to be inserted in the Player View"""
        buttons: List[Button] = []

        buttons.append(HandlerButtons(bot, PrevHandler, cls.EMOJIS.BACK,
                                      textChannel, guildID, MessagesCategory.PLAYER, "Back"))
        buttons.append(HandlerButtons(bot, PauseHandler, cls.EMOJIS.PAUSE,
                                      textChannel, guildID, MessagesCategory.PLAYER, "Pause"))
        buttons.append(HandlerButtons(bot, ResumeHandler, cls.EMOJIS.PLAY,
                                      textChannel, guildID, MessagesCategory.PLAYER, "Play"))
        buttons.append(HandlerButtons(bot, StopHandler, cls.EMOJIS.STOP,
                                      textChannel, guildID, MessagesCategory.PLAYER, "Stop"))
        buttons.append(HandlerButtons(bot, SkipHandler, cls.EMOJIS.SKIP,
                                      textChannel, guildID, MessagesCategory.PLAYER, "Skip"))
        buttons.append(HandlerButtons(bot, QueueHandler, cls.EMOJIS.QUEUE,
                                      textChannel, guildID, MessagesCategory.QUEUE, "Songs"))
        buttons.append(HandlerButtons(bot, LoopHandler, cls.EMOJIS.LOOP_ONE,
                                      textChannel, guildID, MessagesCategory.LOOP, "Loop One", 'One'))
        buttons.append(HandlerButtons(bot, LoopHandler, cls.EMOJIS.LOOP_OFF,
                                      textChannel, guildID, MessagesCategory.LOOP, "Loop Off", 'Off'))
        buttons.append(HandlerButtons(bot, LoopHandler, cls.EMOJIS.LOOP_ALL,
                                      textChannel, guildID, MessagesCategory.LOOP, "Loop All", 'All'))

        return buttons

    async def sendNowPlaying(self, playlist: Playlist, channel: TextChannel, song: Song) -> None:
        # Get the lock of the playlist
        if playlist.isLoopingOne():
            title = self.__messages.ONE_SONG_LOOPING
        else:
            title = self.__messages.SONG_PLAYING

        # Create View and Embed
        embed = self.__embeds.SONG_INFO(song.info, title)
        view = self.__getPlayerView(channel)
        # Send Message and add to the MessagesManager
        message = await channel.send(embed=embed, view=view)
        await self.__messagesManager.addMessageAndClearPrevious(self.__guildID, MessagesCategory.NOW_PLAYING, message, view)

        # Set in the view the message witch contains the view
        view.set_message(message=message)

    def __getPlayerView(self, channel: TextChannel) -> View:
        buttons = self.__getPlayerButtons(channel)
        view = BasicView(self.__bot, buttons)
        return view

    def __getPlayerButtons(self, textChannel: TextChannel) -> List[Button]:
        """Create the Buttons to be inserted in the Player View"""
        buttons: List[Button] = []

        buttons.append(HandlerButtons(self.__bot, PrevHandler, self.__emojis.BACK,
                                      textChannel, self.__guildID, MessagesCategory.PLAYER, "Предыдущая"))
        buttons.append(HandlerButtons(self.__bot, PauseHandler, self.__emojis.PAUSE,
                                      textChannel, self.__guildID, MessagesCategory.PLAYER, "Пауза"))
        buttons.append(HandlerButtons(self.__bot, ResumeHandler, self.__emojis.PLAY,
                                      textChannel, self.__guildID, MessagesCategory.PLAYER, "Играть"))
        buttons.append(HandlerButtons(self.__bot, StopHandler, self.__emojis.STOP,
                                      textChannel, self.__guildID, MessagesCategory.PLAYER, "Стоп"))
        buttons.append(HandlerButtons(self.__bot, SkipHandler, self.__emojis.SKIP,
                                      textChannel, self.__guildID, MessagesCategory.PLAYER, "Следующая"))
        buttons.append(HandlerButtons(self.__bot, QueueHandler, self.__emojis.QUEUE,
                                      textChannel, self.__guildID, MessagesCategory.QUEUE, "Треки"))
        buttons.append(HandlerButtons(self.__bot, LoopHandler, self.__emojis.LOOP_ONE,
                                      textChannel, self.__guildID, MessagesCategory.LOOP, "Повтор трека", 'One'))
        buttons.append(HandlerButtons(self.__bot, LoopHandler, self.__emojis.LOOP_OFF,
                                      textChannel, self.__guildID, MessagesCategory.LOOP, "Выкл. повтор", 'Off'))
        buttons.append(HandlerButtons(self.__bot, LoopHandler, self.__emojis.LOOP_ALL,
                                      textChannel, self.__guildID, MessagesCategory.LOOP, "Повтор всего", 'All'))

        return buttons
