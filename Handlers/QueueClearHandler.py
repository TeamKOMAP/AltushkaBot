from typing import Union
from discord import Interaction
from discord.ext.commands import Context
from Music.AltushkaBot import AltushkaBot
from Handlers.AbstractHandler import AbstractHandler
from Handlers.HandlerReply import HandlerResponse
from Parallelism.AbstractProcessMngr import AbstractPlayersManager


class ClearHandler(AbstractHandler):
    def __init__(self, ctx: Union[Context, Interaction], bot: AltushkaBot) -> None:
        super().__init__(ctx, bot)

    async def run(self) -> HandlerResponse:
        # Получение текущего процесса guild
        playersManager: AbstractPlayersManager = self.config.getPlayersManager()
        if playersManager.verifyIfPlayerExists(self.guild):
            # очистка плейлиста
            playlist = playersManager.getPlayerPlaylist(self.guild)
            playerLock = playersManager.getPlayerLock(self.guild)
            acquired = playerLock.acquire(timeout=self.config.ACQUIRE_LOCK_TIMEOUT)
            if acquired:
                playlist.clear()
                playerLock.release()
                embed = self.embeds.PLAYLIST_CLEAR()
                return HandlerResponse(self.ctx, embed)
            else:
                playersManager.resetPlayer(self.guild, self.ctx)
                embed = self.embeds.PLAYER_RESTARTED()
                return HandlerResponse(self.ctx, embed)
