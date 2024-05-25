from discord.ext.commands import Context
from Music.AltushkaBot import AltushkaBot
from Handlers.AbstractHandler import AbstractHandler
from Handlers.HandlerReply import HandlerResponse
from Parallelism.AbstractProcessMngr import AbstractPlayersManager
from Utils.Utils import Utils
from typing import Union
from discord import Interaction


class HistoryHandler(AbstractHandler):
    def __init__(self, ctx: Union[Context, Interaction], bot: AltushkaBot) -> None:
        super().__init__(ctx, bot)

    async def run(self) -> HandlerResponse:
        # Получение текущего процесса guild
        playersManager: AbstractPlayersManager = self.config.getPlayersManager()
        if playersManager.verifyIfPlayerExists(self.guild):
            playerLock = playersManager.getPlayerLock(self.guild)
            acquired = playerLock.acquire(timeout=self.config.ACQUIRE_LOCK_TIMEOUT)
            if acquired:
                history = playersManager.getPlayerPlaylist(self.guild).getSongsHistory()
                playerLock.release()
            else:
                # Если плеер не отвечает вовремя, мы перезапускаем его
                playersManager.resetPlayer(self.guild, self.ctx)
                embed = self.embeds.PLAYER_RESTARTED()
                return HandlerResponse(self.ctx, embed)
        else:
            history = []

        if len(history) == 0:
            text = self.messages.HISTORY_EMPTY
        else:
            text = f'\n📜 History Length: {len(history)} | Max: {self.config.MAX_SONGS_HISTORY}\n'
            for pos, song in enumerate(history, start=1):
                text += f"**`{pos}` - ** {song.title} - `{Utils.format_time(song.duration)}`\n"

        embed = self.embeds.HISTORY(text)
        return HandlerResponse(self.ctx, embed)
