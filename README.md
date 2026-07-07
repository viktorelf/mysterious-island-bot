# Mysterious Island Bot

[![Python](https://img.shields.io/badge/Python-3.11%2B-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Aiogram](https://img.shields.io/badge/Aiogram-3.x-2A5ADA?logo=telegram&logoColor=white)](https://docs.aiogram.dev/)
[![Telegram Bot](https://img.shields.io/badge/Telegram-Bot-26A5E4?logo=telegram&logoColor=white)](https://core.telegram.org/bots/api)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](./LICENSE)
[![Status](https://img.shields.io/badge/Status-Portfolio%20Ready-111111)](#)

Telegram bot for the "Mysterious Island" writing event. It collects submissions from participants, forwards them to the organizer, and automatically responds with the event rules.

## Project Goals

This project was built as a lightweight submission bot for a writing community event. The goal was to remove manual intake friction, keep all entries in one place, and give participants instant confirmation without relying on external dashboards or a database.

## Why This Project Matters

This repository shows practical product thinking in a small scope:

- it solves a real moderation workflow rather than being a demo-only bot;
- it reduces organizer overhead by standardizing how submissions arrive;
- it improves participant experience with immediate, consistent responses;
- it stays intentionally simple so the bot can be deployed and maintained quickly.

## Key Features

- Handles `/start` onboarding for participants.
- Accepts free-form submissions in chat.
- Forwards each submission to the organizer with sender details.
- Sends a structured confirmation message and contest rules back to the participant.
- Runs as a minimal polling bot with a very small setup footprint.

## Tech Stack

- Python
- Aiogram 3
- Telegram Bot API

## Screenshots

Place project screenshots in [`docs/screenshots/`](./docs/screenshots/).

- `docs/screenshots/chat-start.png` — bot welcome message
- `docs/screenshots/submission-flow.png` — example submission exchange
- `docs/screenshots/admin-notification.png` — organizer notification example

## Demo GIF

Place a short demo GIF in [`docs/demo/`](./docs/demo/).

- `docs/demo/mysterious-island-bot-demo.gif` — suggested demo recording path

## Installation

### Requirements

- Python 3.11 or newer
- A Telegram bot token from BotFather
- Your Telegram user ID for organizer notifications

### Clone and install

```bash
git clone https://github.com/viktorelf/mysterious-island-bot.git
cd mysterious-island-bot
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### Windows setup

```powershell
git clone https://github.com/viktorelf/mysterious-island-bot.git
cd mysterious-island-bot
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
Copy-Item .env.example .env
notepad .env
```

### Environment variables

Create a local `.env` file or set environment variables in your shell:

```env
BOT_TOKEN=your-telegram-bot-token
ADMIN_ID=your-telegram-user-id
```

## Usage

Run the bot locally:

```bash
python bot.py
```

Or use the included Procfile-style command:

```bash
python bot.py
```

## Folder Structure

```text
mysterious-island-bot/
|-- .env.example
|-- .gitignore
|-- bot.py
|-- Procfile
|-- requirements.txt
|-- docs/
|   |-- architecture.md
|   |-- roadmap.md
|   |-- demo/
|   |   `-- .gitkeep
|   `-- screenshots/
|       `-- .gitkeep
|-- CHANGELOG.md
|-- CONTRIBUTING.md
`-- LICENSE
```

## Architecture Notes

Short architecture notes live in [`docs/architecture.md`](./docs/architecture.md).

At a high level:

- `bot.py` contains the full bot flow.
- `CommandStart` handles onboarding.
- A single message handler accepts submissions and forwards them to the organizer.
- Configuration is provided via environment variables to keep secrets out of source control.

## Future Improvements

- Add structured validation for submission format.
- Persist submissions to SQLite or Google Sheets for auditability.
- Add admin commands for status updates and message templates.
- Add tests for message handlers.

## Author

Created and maintained by [@viktorelf](https://github.com/viktorelf).
