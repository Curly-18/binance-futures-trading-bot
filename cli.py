import argparse
import sys
from bot.orders import execute_order
from bot.logging_config import setup_logging

def main():
    setup_logging()

    parser = argparse.ArgumentParser(
        description="Binance Futures Testnet Trading Bot",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Market Order (BUY)
  python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001

  # Limit Order (SELL)
  python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 60000

  # Stop-Limit Order
  python cli.py --symbol BTCUSDT --side BUY --type STOP_LIMIT --quantity 0.001 --price 58000 --stop-price 57500
"""
    )

    parser.add_argument("--symbol", required=True, help="Trading symbol (e.g., BTCUSDT)")
    parser.add_argument("--side", required=True, choices=["BUY", "SELL"], help="Order side")
    parser.add_argument("--type", required=True, choices=["MARKET", "LIMIT", "STOP_LIMIT"], 
                        dest="order_type", help="Order type")
    parser.add_argument("--quantity", type=float, required=True, help="Order quantity")
    parser.add_argument("--price", type=float, help="Limit price (required for LIMIT and STOP_LIMIT)")
    parser.add_argument("--stop-price", type=float, dest="stop_price", 
                        help="Stop price (required for STOP_LIMIT)")

    args = parser.parse_args()

    if args.order_type == "STOP_LIMIT" and args.stop_price is None:
        print("\nError: --stop-price is required for STOP_LIMIT orders")
        print("Example: python cli.py --symbol BTCUSDT --side BUY --type STOP_LIMIT --quantity 0.001 --price 58000 --stop-price 57500")
        sys.exit(1)

    try:
        execute_order(
            symbol=args.symbol.upper(),
            side=args.side.upper(),
            order_type=args.order_type.upper(),
            quantity=args.quantity,
            price=args.price,
            stop_price=args.stop_price
        )
    except Exception as e:
        print(f"\nFailed to place order: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
