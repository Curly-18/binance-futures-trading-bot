# Binance Futures Testnet Trading Bot

A Python application for placing orders on Binance Futures Testnet (USDT-M) with clean, reusable structure, proper logging, and error handling.

## Features

- Market Orders - Buy/Sell at current market price
- Limit Orders - Buy/Sell at specified price
- Stop-Limit Orders - Advanced order type with stop price (BONUS)
- Input Validation - Validates all parameters before placing orders
- Error Handling - Comprehensive exception handling with clear error messages
- Logging - Logs to both file and console for debugging

## Prerequisites

- Python 3.7+
- Binance Futures Testnet Account

## Setup

### 1. Clone the Repository
```
git clone <your-repo-url>
cd trading_bot
```

### 2. Create Virtual Environment
```
python -m venv venv
venv\Scripts\activate
```

### 3. Install Requirements
```
pip install -r requirements.txt
```

### 4. Configure API Keys
Register at https://testnet.binancefuture.com and add credentials to .env file

## Usage Examples

### Market Order (BUY)
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001

### Market Order (SELL)
python cli.py --symbol BTCUSDT --side SELL --type MARKET --quantity 0.001

### Limit Order (BUY)
python cli.py --symbol BTCUSDT --side BUY --type LIMIT --quantity 0.001 --price 58000

### Limit Order (SELL)
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 62000

### Stop-Limit Order
python cli.py --symbol BTCUSDT --side BUY --type STOP_LIMIT --quantity 0.001 --price 58000 --stop-price 57500

## Output

The bot provides clear console output showing order summary and response details.

## Logging

Logs are saved to trading_bot.log and also displayed in console.

## Project Structure

trading_bot/
- bot/
  - client.py - Binance API client wrapper
  - orders.py - Order execution logic
  - validators.py - Input validation
  - logging_config.py - Logging configuration
- cli.py - CLI entry point
- requirements.txt - Python dependencies

## Assumptions

- User has valid Binance Futures Testnet account
- Testnet has sufficient balance for test orders
- Network connectivity to testnet API

## Troubleshooting

- API Key Error: Check .env file has valid credentials
- Invalid Order Type: Use MARKET, LIMIT, or STOP_LIMIT
- Missing Price: Required for LIMIT and STOP_LIMIT orders
- Missing Stop Price: Required for STOP_LIMIT orders
