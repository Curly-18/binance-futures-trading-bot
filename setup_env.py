"""
Setup script to configure Binance Futures Testnet API credentials.
Run this script to input your API keys.
"""

import os
import sys

def setup_api_credentials():
    print("\n" + "="*60)
    print("  Binance Futures Testnet API Setup")
    print("="*60)
    
    print("\n📋 Step 1: Get API Keys from Binance Testnet")
    print("-" * 60)
    print("1. Go to: https://testnet.binancefuture.com")
    print("2. Click 'Register' to create a testnet account")
    print("3. After login, go to 'API' section (top menu)")
    print("4. Click 'Create API' and follow the instructions")
    print("5. Copy your API Key and Secret Key")
    print()
    
    print("\n🔑 Step 2: Enter Your API Credentials")
    print("-" * 60)
    
    api_key = input("Enter your API Key: ").strip()
    api_secret = input("Enter your API Secret: ").strip()
    
    if not api_key or not api_secret:
        print("\n❌ Error: Both API Key and Secret are required!")
        sys.exit(1)
    
    # Write to .env file
    env_content = f"""# Binance Futures Testnet API Credentials
BINANCE_API_KEY={api_key}
BINANCE_API_SECRET={api_secret}
"""
    
    # Get the directory of this script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    env_file_path = os.path.join(script_dir, ".env")
    
    with open(env_file_path, "w") as f:
        f.write(env_content)
    
    print("\n✅ API credentials saved to .env file!")
    print(f"   Location: {env_file_path}")
    print("\n" + "="*60)
    print("  Setup Complete!")
    print("="*60)
    print("\nYou can now run the trading bot:")
    print("  python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001")
    print()

if __name__ == "__main__":
    setup_api_credentials()
