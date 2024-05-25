from UI.Views.AbstractView import AbstractView
from UI.Buttons.AbstractItem import AbstractItem
from Music.AltushkaBot import AltushkaBot
from Configs.Emojis import AEmojis
from discord import Message
from discord.ui import View
from typing import List

emojis = AEmojis()


class BasicView(View, AbstractView):
    """
    Класс представления, наследуемый от класса представления Discord, управляющий списком кнопок.
    и сообщением, содержащим это представление.
    """

    def __init__(self, bot: AltushkaBot, buttons: List[AbstractItem], timeout: float = 6000):
        super().__init__(timeout=timeout)
        self.__bot = bot
        self.__message: Message = None
        self.__working = True

        for button in buttons:
            # Установите для кнопок экземпляр представления, которое их содержит.
            button.set_view(self)
            self.add_item(button)

    def stopView(self):
        self.__working = False

    async def on_timeout(self) -> None:
        # Disable all itens and, if has the message, edit it
        try:
            if not self.__working:
                return

            self.disable_all_items()
            if self.__message is not None and isinstance(self.__message, Message):
                await self.__message.edit(f"{emojis.MUSIC} - Кнопки в этом сообщении были отключены по истечении времени", view=self)
        except Exception as e:
            print(f'[ERROR EDITING MESSAGE] -> {e}')

    def set_message(self, message: Message) -> None:
        self.__message = message

    async def update(self):
        """Edit the message sending the view again"""
        try:
            if not self.__working:
                return

            if self.__message is not None:
                await self.__message.edit(view=self)
        except Exception as e:
            print(f'[ERROR UPDATING MESSAGE] -> {e}')
