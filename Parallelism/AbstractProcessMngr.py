from abc import ABC, abstractmethod
from threading import Lock
from typing import Union
from discord.ext.commands import Context
from discord import Guild, Interaction
from Music.Playlist import Playlist
from Music.Song import Song
from Parallelism.Commands import ACommands


class AbstractPlayersManager(ABC):
    def __init__(self, bot) -> None:
        pass

    @abstractmethod
    async def sendCommandToPlayer(self, command: ACommands, guild: Guild, context: Union[Context, Interaction], forceCreation: bool = False):
        """Если логическое значение ForceCreation имеет значение True, то для создаваемого игрока должен быть предоставлен контекст."""
        pass

    @abstractmethod
    def getPlayerPlaylist(self, guild: Guild) -> Playlist:
        """Если есть процесс игрока для гильдии, то вернет плейлист гильдии"""
        pass

    @abstractmethod
    def getPlayerLock(self, guild: Guild) -> Lock:
        """Если есть процесс игрока для гильдии, то вернет блокировку гильдии"""
        pass

    @abstractmethod
    def verifyIfPlayerExists(self, guild: Guild) -> bool:
        """Возвращает, если существует игрок в гильдии"""
        pass

    @abstractmethod
    def createPlayerForGuild(self, guild: Guild, context: Union[Context, Interaction]) -> None:
        """Используя контекстную информацию о гильдии, создайте внутренний плеер для гильдии."""
        pass

    @abstractmethod
    def resetPlayer(self, guild: Guild, context: Context) -> None:
        """Попытка перезапуска плеера гильдии"""
        pass

    @abstractmethod
    async def showNowPlaying(self, guildID: int, song: Song) -> None:
        pass
