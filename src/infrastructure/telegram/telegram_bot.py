"""python-telegram-bot wrapper."""

from __future__ import annotations

import asyncio
from collections.abc import Awaitable, Callable
from typing import Any

from telegram import BotCommand
from telegram.ext import Application, CommandHandler

from src.domain.interfaces.telegram import ITelegramBot


class TelegramBot(ITelegramBot):
    """Telegram bot adapter with simple command registration."""

    def __init__(self, bot_token: str) -> None:
        self.application = Application.builder().token(bot_token).build()
        self._chat_index: dict[int, int] = {}
        self._queues: dict[int, asyncio.Queue[dict[str, Any]]] = {}

    async def send_message(
        self,
        chat_id: int,
        text: str,
        reply_to_message_id: int | None = None,
        parse_mode: str | None = None,
    ) -> None:
        await self.application.bot.send_message(
            chat_id=chat_id,
            text=text,
            reply_to_message_id=reply_to_message_id,
            parse_mode=parse_mode,
        )

    async def send_document(
        self,
        chat_id: int,
        document_path: str,
        caption: str | None = None,
    ) -> None:
        with open(document_path, "rb") as file_obj:
            await self.application.bot.send_document(chat_id=chat_id, document=file_obj, caption=caption)

    async def send_photo(
        self,
        chat_id: int,
        photo_path: str,
        caption: str | None = None,
    ) -> None:
        with open(photo_path, "rb") as file_obj:
            await self.application.bot.send_photo(chat_id=chat_id, photo=file_obj, caption=caption)

    async def register_command(
        self,
        command: str,
        description: str,
        handler: Callable[[Any, Any], Awaitable[None]],
    ) -> None:
        # Our generic handler is compatible at runtime, but python-telegram-bot's
        # CommandHandler callback type is more specific than mypy can infer.
        self.application.add_handler(CommandHandler(command, handler))  # type: ignore[arg-type]
        self._chat_index.setdefault(hash(command), hash(description))

    async def set_commands(self, commands: list[dict[str, str]]) -> None:
        command_defs = [BotCommand(command=item["command"], description=item["description"]) for item in commands]
        await self.application.bot.set_my_commands(command_defs)

    async def wait_for_message(
        self,
        chat_id: int,
        timeout: float | None = None,
    ) -> dict[str, Any] | None:
        queue = self._queues.setdefault(chat_id, asyncio.Queue())
        try:
            return await asyncio.wait_for(queue.get(), timeout=timeout)
        except TimeoutError:
            return None

    async def start_polling(self) -> None:
        await self.application.initialize()
        await self.application.start()
        if self.application.updater is None:
            raise RuntimeError("Application updater is not initialised")
        await self.application.updater.start_polling()

    async def stop_polling(self) -> None:
        updater = self.application.updater
        if updater is not None:
            await updater.stop()
        await self.application.stop()
        await self.application.shutdown()

    async def get_chat_id(self, user_id: int) -> int | None:
        return self._chat_index.get(user_id)
