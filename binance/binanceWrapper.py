from binance.client import Client
from binance.exceptions import BinanceAPIException
import os


load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
(os.getenv("OPENAI_API_KEY"))
client = openai.OpenAI()

# Your testnet API key and secret (from https://testnet.binance.vision)
API_KEY = "YOUR_TESTNET_API_KEY"
API_SECRET = "YOUR_TESTNET_API_SECRET"

# Create a Binance client using testnet
client = Client(API_KEY, API_SECRET, testnet=True)

try:
    # Check server time
    print("Server time:", client.get_server_time())

    # Fetch account info
    account = client.get_account()
    print("\nBalances:")
    for asset in account['balances']:
        if float(asset['free']) > 0 or float(asset['locked']) > 0:
            print(asset)

    # Create a test order (not executed on real market)
    print("\nPlacing a test order...")
    order = client.create_test_order(
        symbol='BTCUSDT',
        side=Client.SIDE_BUY,
        type=Client.ORDER_TYPE_LIMIT,
        timeInForce=Client.TIME_IN_FORCE_GTC,
        quantity=0.001,
        price='20000'
    )
    print("Test order placed successfully (simulation only).")

except BinanceAPIException as e:
    print("Binance API Exception:", e.message)
except Exception as e:
    print("General Exception:", str(e))
