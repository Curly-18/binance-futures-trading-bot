import logging
from .client import BinanceFuturesClient
from .validators import validate_side, validate_order_type, validate_price

def execute_order(symbol, side, order_type, quantity, price=None, stop_price=None):
    try:
        # Validate inputs
        validate_side(side)
        validate_order_type(order_type)
        validate_price(order_type, price)
        
        # Validate stop_price for STOP_LIMIT orders
        if order_type == "STOP_LIMIT" and stop_price is None:
            raise ValueError("stopPrice is required for STOP_LIMIT orders")

        # Log the order request
        logging.info(f"Preparing order request: symbol={symbol}, side={side}, "
                    f"type={order_type}, quantity={quantity}, price={price}, "
                    f"stopPrice={stop_price}")

        client = BinanceFuturesClient()

        response = client.place_order(
            symbol=symbol,
            side=side,
            order_type=order_type,
            quantity=quantity,
            price=price,
            stop_price=stop_price
        )

        print("\n" + "="*40)
        print("          ORDER SUMMARY")
        print("="*40)
        print(f"Symbol:     {symbol}")
        print(f"Side:       {side}")
        print(f"Type:       {order_type}")
        print(f"Quantity:   {quantity}")
        if price:
            print(f"Price:      {price}")
        if stop_price:
            print(f"Stop Price: {stop_price}")

        print("\n" + "="*40)
        print("          RESPONSE DETAILS")
        print("="*40)
        print(f"Order ID:    {response.get('orderId')}")
        print(f"Status:      {response.get('status')}")
        print(f"Executed Qty: {response.get('executedQty')}")
        print(f"Avg Price:   {response.get('avgPrice', 'N/A')}")

        print("\n✅ Order placed successfully!")
        logging.info(f"Order successfully placed. Order ID: {response.get('orderId')}")
        
    except ValueError as e:
        error_msg = f"Validation Error: {e}"
        print(f"\n❌ {error_msg}")
        logging.error(error_msg)
        raise
        
    except Exception as e:
        error_msg = f"Order Failed: {str(e)}"
        print(f"\n❌ {error_msg}")
        logging.error(error_msg, exc_info=True)
        raise
