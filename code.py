import yfinance as yf

# Define the ticker symbol
# ticker_symbol = "RELIANCE.NS"  # Apple Inc.

# # Get data on this ticker
# ticker_data = yf.Ticker(ticker_symbol)

# # Get historical market data
# hist = ticker_data.history(period="1mo")  # You can adjust the period (e.g., "1d", "5d", "1mo", "1y", "max")

# # Display the data
# print(hist)

telegram_token = "6471256734:AAEKPEwo1Vm5kKvWzFEelSeQZs1Dm15nwqA"


from  telegram import Bot
import asyncio
# Replace this with your bot's API token
bot_token = telegram_token
async def get_chat_id():
    # Initialize the bot
    bot = Bot(token=bot_token)

    # Get updates sent to the bot
    updates = await bot.get_updates()

    # Print the chat ID from the latest message
    for update in updates:
        print("Chat ID:", update.message.chat.id)

asyncio.run(get_chat_id())
