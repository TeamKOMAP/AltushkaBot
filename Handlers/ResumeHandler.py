from discord.ext.commands import Context
from Handlers.AbstractHandler import AbstractHandler
from Handlers.HandlerReply import HandlerResponse
from Parallelism.AbstractProcessMngr import AbstractPlayersManager
from Parallelism.Commands import ACommands, ACommandsType
from Music.AltushkaBot import AltushkaBot
from typing import Union
from discord import Interaction


class ResumeHandler(AbstractHandler):
    def __init__(self, ctx: Union[Context, Interaction], bot: AltushkaBot) -> None:
        super().__init__(ctx, bot)

    async def run(self) -> HandlerResponse:
        playersManager: AbstractPlayersManager = self.config.getPlayersManager()
        if playersManager.verifyIfPlayerExists(self.guild):
            command = ACommands(ACommandsType.RESUME, None)
            await playersManager.sendCommandToPlayer(command, self.guild, self.ctx)
            embed = self.embeds.PLAYER_RESUMED()
            return HandlerResponse(self.ctx, embed)
        else:
            embed = self.embeds.NOT_PLAYING()
            return HandlerResponse(self.ctx, embed)
