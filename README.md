#  Simplified Trading Bot (Binance Futures Testnet)

## Overview
This project is a Python-based trading bot that allows users to place MARKET and LIMIT orders using a command-line interface.

## Features
- Market & Limit Orders
- CLI-based UI
- Input Validation
- Logging (bot.log)
- Modular Code Structure
- Simulated Order Execution

## 🛠 Tech Stack
- Python 3
- Requests
- dotenv

## Project Structure
trading_bot/
│
├── bot/
│   ├── rest_client.py
│   ├── orders.py
│   ├── validators.py
│   ├── logging_config.py
│
├── cli.py
├── .env
├── bot.log

## How to Run

1. Install dependencies:
pip install -r requirements.txt

2. Run the bot:
python cli.py

##  Example

- Select order type
- Enter symbol (BTCUSDT)
- Enter BUY/SELL
- Enter quantity

## Note
Orders are simulated due to Binance Testnet API limitations.

## Future Improvements
- Real API integration
- GUI interface
- Stop-loss & Take-profit