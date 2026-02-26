import os
import logging
from binance.client import Client
from binance.exceptions import BinanceAPIException
from dotenv import load_dotenv

load_dotenv()

class BinanceFuturesClient:
    """Binance Futures Testnet API Client"""
    
    TESTNET_URL = "https://testnet.binancefuture.com/fapi"
    
    def __init__(self):
        self.api_key = os.getenv("BINANCE_API_KEY")
        self.api_secret = os.getenv("BINANCE_API_SECRET")
        
        if not self.api_key or not self.api_secret:
            raise ValueError("API keys not found. Please set BINANCE_API_KEY and BINANCE_API_SECRET in .env file")

        self.client = Client(self.api_key, self.api_secret)
        self.client.FUTURES_URL = self.TESTNET_URL
        logging.info("Binance Futures Client initialized for Testnet")

    def place_order(self, symbol, side, order_type, quantity, price=None, stop_price=None):
        """Place an order on Binance Futures Testnet"""
        try:
            logging.info(f"=== ORDER REQUEST ===")
            logging.info(f"Symbol: {symbol}")
            logging.info(f"Side: {side}")
            logging.info(f"Type: {order_type}")
            logging.info(f"Quantity: {quantity}")
            if price:
                logging.info(f"Price: {price}")
            if stop_price:
                logging.info(f"Stop Price: {stop_price}")

            params = {
                "symbol": symbol,
                "side": side,
                "type": order_type,
                "quantity": quantity
            }

            # Handle LIMIT orders
            if order_type == "LIMIT":
                if price is None:
                    raise ValueError("Price is required for LIMIT orders")
                params["price"] = price
                params["timeInForce"] = "GTC"
            
            # Handle STOP_LIMIT orders
            elif order_type == "STOP_LIMIT":
                if price is None or stop_price is None:
                    raise ValueError("Price and stopPrice are required for STOP_LIMIT orders")
                params["price"] = price
                params["stopPrice"] = stop_price
                params["timeInForce"] = "GTC"

            logging.info(f"API params: {params}")
            
            response = self.client.futures_create_order(**params)

            logging.info(f"=== ORDER RESPONSE ===")
            logging.info(f"Full response: {response}")
            logging.info(f"Order ID: {response.get('orderId')}")
            logging.info(f"Status: {response.get('status')}")
            
            return response

        except BinanceAPIException as e:
            error_msg = f"Binance API Error: {e.status_code} - {e.message}"
            logging.error(error_msg)
            raise

        except ValueError as e:
            logging.error(f"Validation Error: {e}")
            raise
            
        except Exception as e:
            logging.error(f"Unexpected Error: {str(e)}", exc_info=True)
            raise
