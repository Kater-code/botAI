# botAI — Telegram Bot with GPT Integration

Telegram bot with AI responses powered by GPT and a subscription system.

## Features
- GPT-powered responses for every user message
- Free trial limit with subscription paywall
- User database (registration, usage tracking)
- Modular architecture (handlers / services / database)

## Stack
- Python
- aiogram
- OpenAI API (GPT)
- asyncio

## Structure
botTG/
├── handlers/      # Message handlers + AI logic
├── services/      # GPT API integration
├── database/      # User data & subscription tracking
├── bot.py         # Entry point
└── config.py      # Configuration
## Setup
```bash
pip install -r requirements.txt
python bot.py
```
