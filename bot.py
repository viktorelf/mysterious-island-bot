import asyncio
import os

from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")
ADMIN_ID = os.getenv("ADMIN_ID")

dp = Dispatcher()

RULES_TEXT = """
🏝 Спасибо за участие в конкурсе «Таинственный остров»!

📌 Напоминаем правила:

• Главный герой — Чонгук
• Обязательная метка — «Необитаемые острова»
• Размер работы: от 10 до 50 страниц
• Рейтинг: G, PG-13, R, NC-17
• Пэйринг: любой с Чонгуком
• Направленность: слэш
• Статус работы: завершён

📌 При сдаче работы укажите:
• @юзернейм автора
• Остров + ссылка на фанфик

⏳ Работы принимаются до 10.08.2026, 23:59.

⚓ Удачи! Таинственный остров уже ждёт вашу историю.
""".strip()


@dp.message(CommandStart())
async def start(message: types.Message):
    await message.answer(
        "🏝 Привет! Это бот конкурса «Таинственный остров».\n\n"
        "Для регистрации отправьте:\n"
        "Остров + ссылка на профиль Фикбука"
    )


@dp.message()
async def auto_reply(message: types.Message):
    username = (
        f"@{message.from_user.username}"
        if message.from_user.username
        else "без username"
    )
    text = message.text or message.caption or "[не текстовое сообщение]"

    await message.bot.send_message(
        ADMIN_ID,
        f"""
🏝 Новая заявка!

👤 {message.from_user.full_name}
📎 {username}
🆔 {message.from_user.id}

Сообщение:
{text}
""",
    )

    await message.answer("Спасибо за участие в конкурсе! 🏝\n\n" + RULES_TEXT)


async def main():
    if not TOKEN:
        raise ValueError("Не указан BOT_TOKEN")
    if not ADMIN_ID:
        raise ValueError("Не указан ADMIN_ID")

    bot = Bot(token=TOKEN)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
