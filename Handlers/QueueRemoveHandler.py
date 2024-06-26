from discord.ext.commands import Context
from Handlers.AbstractHandler import AbstractHandler
from Handlers.HandlerReply import HandlerResponse
from Configs.Exceptions import BadCommandUsage, AltError, ErrorRemoving, InvalidInput, NumberRequired
from Music.Playlist import Playlist
from Music.AltushkaBot import AltushkaBot
from Parallelism.AbstractProcessMngr import AbstractPlayersManager
from typing import Union
from discord import Interaction


class RemoveHandler(AbstractHandler):
    def __init__(self, ctx: Union[Context, Interaction], bot: AltushkaBot) -> None:
        super().__init__(ctx, bot)

    async def run(self, position: str) -> HandlerResponse:
        playersManager: AbstractPlayersManager = self.config.getPlayersManager()
        if not playersManager.verifyIfPlayerExists(self.guild):
            embed = self.embeds.NOT_PLAYING()
            error = BadCommandUsage()
            return HandlerResponse(self.ctx, embed, error)

        playlist = playersManager.getPlayerPlaylist(self.guild)
        if playlist is None:
            embed = self.embeds.NOT_PLAYING()
            error = BadCommandUsage()
            return HandlerResponse(self.ctx, embed, error)

        error = self.__validateInput(position)
        if error:
            embed = self.embeds.ERROR_EMBED(error.message)
            return HandlerResponse(self.ctx, embed, error)

        position = self.__sanitizeInput(playlist, position)
        if not playlist.validate_position(position):
            error = InvalidInput()
            embed = self.embeds.PLAYLIST_RANGE_ERROR()
            return HandlerResponse(self.ctx, embed, error)

        try:
            song = playlist.remove_song(position)
            name = song.title if song.title else song.identifier

            embed = self.embeds.SONG_REMOVED(name)
            return HandlerResponse(self.ctx, embed)
        except:
            error = ErrorRemoving()
            embed = self.embeds.ERROR_REMOVING()
            return HandlerResponse(self.ctx, embed, error)

    def __validateInput(self, position: str) -> Union[AltError, None]:
        try:
            position = int(position)
        except:
            return NumberRequired(self.messages.ERROR_NUMBER)

    def __sanitizeInput(self, playlist: Playlist, position: str) -> int:
        position = int(position)

        if position == -1:
            position = len(playlist.getSongs())
        return position
