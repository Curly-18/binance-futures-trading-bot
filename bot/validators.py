def validate_side(side):
    """Validate order side (BUY/SELL)"""
    if side not in ["BUY", "SELL"]:
        raise ValueError("Side must be BUY or SELL")

def validate_order_type(order_type):
    """Validate order type (MARKET, LIMIT, STOP_LIMIT)"""
    valid_types = ["MARKET", "LIMIT", "STOP_LIMIT"]
    if order_type not in valid_types:
        raise ValueError(f"Order type must be one of: {', '.join(valid_types)}")

def validate_price(order_type, price):
    """Validate price is provided for price-dependent order types"""
    if order_type in ["LIMIT", "STOP_LIMIT"] and price is None:
        raise ValueError(f"Price is required for {order_type} orders")
