from typing import Dict, List
from Configs.Singleton import Singleton
from UI.Views.AbstractView import AbstractView
from Messages.MessagesCategory import MessagesCategory
from Messages.DcMessages import AAbstractMessage
import traceback


class MessagesManager(Singleton):
    def __init__(self) -> None:
        if not super().created:
            # Для каждой гильдии и каждой категории будет список сообщений.
            self.__guildsMessages: Dict[int, Dict[MessagesCategory, List[AAbstractMessage]]] = {}
            # control that
            self.__messagesViews: Dict[AAbstractMessage, AbstractView] = {}

    def addMessage(self, guildID: int, category: MessagesCategory, message: AAbstractMessage, view: AbstractView = None) -> None:
        if message is None:
            return

        # Если гильдия не существует, создайте Dict
        if guildID not in self.__guildsMessages.keys():
            self.__guildsMessages[guildID] = {}
        # Если категории еще нет в гильдии, добавьте
        if category not in self.__guildsMessages[guildID].keys():
            self.__guildsMessages[guildID][category] = []

        sendedMessages = self.__guildsMessages[guildID][category]
        if view is not None and isinstance(view, AbstractView):
            self.__messagesViews[message] = view
        sendedMessages.append(message)

    async def addMessageAndClearPrevious(self, guildID: int, category: MessagesCategory, message: AAbstractMessage, view: AbstractView = None) -> None:
        if message is None:
            return

        # Если гильдия не существует, создайте Dict
        if guildID not in self.__guildsMessages.keys():
            self.__guildsMessages[guildID] = {}
        # Если категории еще нет в гильдии, добавьте
        if category not in self.__guildsMessages[guildID].keys():
            self.__guildsMessages[guildID][category] = []

        sendedMessages = self.__guildsMessages[guildID][category]

        # Удалить отправленные все сообщения этой категории
        for previousMessage in sendedMessages:
            await self.__deleteMessage(previousMessage)

        # Создайте новый список только с новым сообщением.
        self.__guildsMessages[guildID][category] = [message]

        # Сохранить вид этого сообщения
        if view is not None and isinstance(view, AbstractView):
            self.__messagesViews[message] = view

    async def clearMessagesOfCategory(self, guildID: int, category: MessagesCategory) -> None:
        sendedMessages = self.__guildsMessages[guildID][category]

        for message in sendedMessages:
            self.__deleteMessage(message)

    async def clearMessagesOfGuild(self, guildID: int) -> None:
        categoriesMessages = self.__guildsMessages[guildID]

        for category in categoriesMessages.keys():
            for message in categoriesMessages[category]:
                self.__deleteMessage(message)

    async def __deleteMessage(self, message: AAbstractMessage) -> None:
        try:
            # Если есть просмотр для этого сообщения, удаляет ключ
            if message in self.__messagesViews.keys():
                messageView = self.__messagesViews.pop(message)
                messageView.stopView()
                del messageView

            await message.delete()
        except Exception:
            print(f'[ERROR DELETING MESSAGE] -> {traceback.format_exc()}')
