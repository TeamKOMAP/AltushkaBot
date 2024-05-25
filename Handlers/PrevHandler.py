from discord.ext.commands import Context
from Handlers.AbstractHandler import AbstractHandler
from Configs.Exceptions import BadCommandUsage, ImpossibleMove
from Handlers.HandlerReply import HandlerResponse
from Parallelism.AbstractProcessMngr import AbstractPlayersManager
from Parallelism.Commands import ACommands, ACommandsType
from Music.AltushkaBot import AltushkaBot
from typing import Union
from discord import Interaction


class PrevHandler(AbstractHandler):
    def __init__(self, ctx: Union[Context, Interaction], bot: AltushkaBot) -> None:
        super().__init__(ctx, bot)

    async def run(self) -> HandlerResponse:
        if not self.__user_connected():
            error = ImpossibleMove()
            embed = self.embeds.NO_CHANNEL()
            return HandlerResponse(self.ctx, embed, error)

        playersManager: AbstractPlayersManager = self.config.getPlayersManager()
        if not playersManager.verifyIfPlayerExists(self.guild):
            embed = self.embeds.NOT_PLAYING()
            error = BadCommandUsage()
            return HandlerResponse(self.ctx, embed, error)

        playlist = playersManager.getPlayerPlaylist(self.guild)
        if len(playlist.getHistory()) == 0:
            error = ImpossibleMove()
            embed = self.embeds.NOT_PREVIOUS_SONG()
            return HandlerResponse(self.ctx, embed, error)

        if playlist.isLoopingAll() or playlist.isLoopingOne():
            error = BadCommandUsage()
            embed = self.embeds.FAIL_DUE_TO_LOOP_ON()
            return HandlerResponse(self.ctx, embed, error)

        # Send a prev command, together with the user voice channel
        prevCommand = ACommands(ACommandsType.PREV, self.author.voice.channel.id)
        await playersManager.sendCommandToPlayer(prevCommand, self.guild, self.ctx)

        embed = self.embeds.RETURNING_SONG()
        return HandlerResponse(self.ctx, embed)

    def __user_connected(self) -> bool:
        if self.author.voice:
            return True
        else:
            return False
