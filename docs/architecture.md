# Architecture Notes

## Overview

`mysterious-island-bot` is a compact Telegram bot built around a single conversational flow:

1. A participant starts the bot.
2. The bot explains how to submit an entry.
3. The participant sends their message.
4. The bot forwards the submission details to the organizer.
5. The bot confirms receipt and returns the contest rules.

## Components

- `bot.py`
  Main application entry point, message handlers, and polling setup.
- Telegram Bot API
  Delivery channel for participant interactions and organizer notifications.
- Environment variables
  Used for runtime configuration (`BOT_TOKEN`, `ADMIN_ID`) so secrets stay out of the repository.

## Design Choices

- No database:
  The bot is intentionally lightweight and optimized for quick deployment.
- Polling:
  Simpler to run for a small event workflow than a webhook-based setup.
- Single-purpose flow:
  Keeps the UX focused and the maintenance cost low.

## Security Note

Sensitive runtime values must never be committed. Use `.env` locally or your hosting provider's environment variable settings.
