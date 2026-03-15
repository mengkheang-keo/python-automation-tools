import asyncio
import datetime
import os

from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# generate tokens from BotFather
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

if not TOKEN:
    raise ValueError("Bot token not found. Set TELEGRAM_BOT_TOKEN environment variable.")

# Store active countdowns
active_countdowns = {}


# countdown commands
async def countdown_timer(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Start a countdown timer."""

    try:
        chat_id = update.effective_chat.id
        args = context.args

        if len(args) < 2:
            await update.message.reply_text(
                "Usage:\n/countdown_timer <task_name> <YYYY-MM-DD>"
            )
            return

        task_name = args[0]
        deadline = datetime.datetime.strptime(args[1], "%Y-%m-%d").date()

        today = datetime.date.today()
        days_left = (deadline - today).days

        if days_left < 0:
            await update.message.reply_text(
                f"❌ The deadline for '{task_name}' has already passed."
            )
            return

        message = await update.message.reply_text(
            f"🕒 Countdown for '{task_name}': {days_left} days remaining."
        )

        active_countdowns[chat_id] = (task_name, deadline, message.message_id)

        asyncio.create_task(
            update_countdown(chat_id, task_name, deadline, message, context)
        )

    except ValueError:
        await update.message.reply_text("Invalid date format. Use YYYY-MM-DD.")

# update countdown
async def update_countdown(chat_id, task_name, deadline, message, context):
    """Continuously update the countdown message."""

    while True:
        now = datetime.datetime.now()
        days_left = (deadline - now.date()).days

        if days_left > 1:
            text = f"🕒 Countdown for '{task_name}': {days_left} days remaining."
            sleep_time = 24 * 60 * 60

        elif days_left == 1:
            text = f"⚠️ '{task_name}' is due in **1 day**."
            sleep_time = 24 * 60 * 60

        else:
            hours_left = (deadline - now).total_seconds() / 3600

            if hours_left > 1:
                text = f"⚠️ '{task_name}' is due in **{int(hours_left)} hours**."
                sleep_time = 60 * 60

            else:
                minutes_left = int((deadline - now).total_seconds() / 60)

                if minutes_left > 0:
                    text = f"⏳ '{task_name}' is due in **{minutes_left} minutes**."
                    sleep_time = 60
                else:
                    text = f"🚨 The deadline for '{task_name}' is NOW!"
                    await context.bot.edit_message_text(
                        chat_id=chat_id,
                        message_id=message.message_id,
                        text=text,
                    )
                    break

        try:
            await context.bot.edit_message_text(
                chat_id=chat_id,
                message_id=message.message_id,
                text=text,
            )
        except:
            break

        await asyncio.sleep(sleep_time)

# main func
def main():
    """Start the Telegram bot."""

    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("countdown_timer", countdown_timer))

    print("Countdown bot is running...")

    app.run_polling()

if __name__ == "__main__":
    main()