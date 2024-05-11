from discord.ext.commands import Context
from Handlers.AbstractHandler import AbstractHandler
from Handlers.HandlerResponse import HandlerResponse
from Parallelism.AbstractProcessManager import AbstractPlayersManager
from Parallelism.Commands import ACommands, ACommandsType
from Music.AltushkaBot import AltushkaBot
from typing import Union
from discord import Interaction


class ResetHandler(AbstractHandler):
    def __init__(self, ctx: Union[Context, Interaction], bot: AltushkaBot) -> None:
        super().__init__(ctx, bot)

    async def run(self) -> HandlerResponse:
        playersManager: AbstractPlayersManager = self.config.getPlayersManager()
        if playersManager.verifyIfPlayerExists(self.guild):
            command = ACommands(ACommandsType.RESET, None)
            await playersManager.sendCommandToPlayer(command, self.guild, self.ctx)
            return HandlerResponse(self.ctx)
        else:
            embed = self.embeds.NOT_PLAYING()
            return HandlerResponse(self.ctx, embed)
