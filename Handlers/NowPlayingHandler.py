from discord.ext.commands import Context
from Handlers.AbstractHandler import AbstractHandler
from Handlers.HandlerReply import HandlerResponse
from Music.AltushkaBot import AltushkaBot
from Parallelism.AbstractProcessMngr import AbstractPlayersManager
from Utils.Cleaner import Cleaner
from typing import Union
from discord import Interaction


class NowPlayingHandler(AbstractHandler):
    def __init__(self, ctx: Union[Context, Interaction], bot: AltushkaBot) -> None:
        super().__init__(ctx, bot)
        self.__cleaner = Cleaner()

    async def run(self) -> HandlerResponse:
        playersManager: AbstractPlayersManager = self.config.getPlayersManager()
        if not playersManager.verifyIfPlayerExists(self.guild):
            embed = self.embeds.NOT_PLAYING()
            return HandlerResponse(self.ctx, embed)

        playlist = playersManager.getPlayerPlaylist(self.guild)
        if playlist.getCurrentSong() is None:
            embed = self.embeds.NOT_PLAYING()
            return HandlerResponse(self.ctx, embed)

        if playlist.isLoopingOne():
            title = self.messages.ONE_SONG_LOOPING
        else:
            title = self.messages.SONG_PLAYING
        await self.__cleaner.clean_messages(self.ctx, self.config.CLEANER_MESSAGES_QUANT)

        info = playlist.getCurrentSong().info
        embed = self.embeds.SONG_INFO(info, title)
        return HandlerResponse(self.ctx, embed)
