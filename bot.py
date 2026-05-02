import os

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CommandHandler, ContextTypes


NEW_BOT_URL = os.getenv("NEW_BOT_URL", "https://t.me/AetherTaarot_bot")
NEW_BOT_NAME = os.getenv("NEW_BOT_NAME", "@AetherTaarot_bot")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    keyboard = InlineKeyboardMarkup(
        [[InlineKeyboardButton("Перейти в нового бота", url=NEW_BOT_URL)]]
    )

    await update.message.reply_text(
        f"Мы переехали в {NEW_BOT_NAME}.\n\n"
        "Нажми кнопку ниже, чтобы перейти:",
        reply_markup=keyboard,
    )


def main() -> None:
    token = os.getenv("BOT_TOKEN")
    if not token:
        raise RuntimeError("Set BOT_TOKEN environment variable")

    app = Application.builder().token(token).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()


if __name__ == "__main__":
    main()
