# Telegram Countdown Bot

A simple Telegram bot that creates countdown timers and updates the remaining time automatically.

The bot edits a single message to show the remaining time until the deadline.

---

## Features

- Start countdown timers with a command
- Daily countdown updates
- Hourly updates when less than 24 hours remain
- Minute updates when the deadline is very close
- Automatic message updates

---

## Requirements

Install dependency:

pip install python-telegram-bot

---

## Setup

Create a Telegram bot using **@BotFather** and obtain your bot token.

Set the token as an environment variable.

Example (Windows PowerShell):

$env:TELEGRAM_BOT_TOKEN="your_token_here"

---

## Usage

Run the bot:

python bot.py

Then use the command inside Telegram:

/countdown_timer <task_name> <YYYY-MM-DD>

Example:

/countdown_timer project_deadline 2026-04-01

---

## Example Output

🕒 Countdown for 'project_deadline': 15 days remaining.

The bot will automatically update the message as the deadline approaches.

---

## Notes

- The bot updates the same message instead of sending multiple messages.
- Countdown updates become more frequent as the deadline approaches.