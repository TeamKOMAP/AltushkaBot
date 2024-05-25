from typing import Union
from Configs.Exceptions import BadCommandUsage, InvalidInput, NumberRequired, UnknownError, AltError
from Handlers.AbstractHandler import AbstractHandler
from discord.ext.commands import Context
from discord import Interaction
from Handlers.HandlerReply import HandlerResponse
from Music.Playlist import Playlist
from Music.AltushkaBot import AltushkaBot
from Parallelism.AbstractProcessMngr import AbstractPlayersManager
from Parallelism.Commands import ACommands, ACommandsType


class MoveMusicHandler(AbstractHandler):
    """Переместите музыку из определенной позиции и воспроизведите сразу"""

    def __init__(self, ctx: Union[Context, Interaction], bot: AltushkaBot) -> None:
        super().__init__(ctx, bot)

    async def run(self, musicPos: str) -> HandlerResponse:
        playersManager: AbstractPlayersManager = self.config.getPlayersManager()
        if not playersManager.verifyIfPlayerExists(self.guild):
            embed = self.embeds.NOT_PLAYING()
            error = BadCommandUsage()
            return HandlerResponse(self.ctx, embed, error)

        playerLock = playersManager.getPlayerLock(self.guild)
        acquired = playerLock.acquire(timeout=self.config.ACQUIRE_LOCK_TIMEOUT)
        if acquired:
            # попробует преобразовать input в int
            error = self.__validateInput(musicPos)
            if error:
                embed = self.embeds.ERROR_EMBED(error.message)
                playerLock.release()
                return HandlerResponse(self.ctx, embed, error)

            # очистка input
            playlist = playersManager.getPlayerPlaylist(self.guild)
            musicPos = self.__sanitizeInput(playlist, musicPos)

            # подтверждение позиции
            if not playlist.validate_position(musicPos):
                error = InvalidInput()
                embed = self.embeds.PLAYLIST_RANGE_ERROR()
                playerLock.release()
                return HandlerResponse(self.ctx, embed, error)
            try:
                # Переместить выбранную песню
                playlist.move_songs(musicPos, 1)

                # Отправка команды плееру для пропуска музыку
                command = ACommands(ACommandsType.SKIP, None)
                await playersManager.sendCommandToPlayer(command, self.guild, self.ctx)

                return HandlerResponse(self.ctx)
            except:
                embed = self.embeds.ERROR_MOVING()
                error = UnknownError()
                return HandlerResponse(self.ctx, embed, error)
            finally:
                playerLock.release()
        else:
            playersManager.resetPlayer(self.guild, self.ctx)
            embed = self.embeds.PLAYER_RESTARTED()
            return HandlerResponse(self.ctx, embed)

    def __validateInput(self, position: str) -> Union[AltError, None]:
        try:
            position = int(position)
        except:
            return NumberRequired(self.messages.ERROR_NUMBER)

    def __sanitizeInput(self, playlist: Playlist, position: int) -> int:
        position = int(position)

        if position == -1:
            position = len(playlist.getSongs())

        return position
