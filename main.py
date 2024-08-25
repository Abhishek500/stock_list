from flask import Flask, request, jsonify
import yfinance as yf

app = Flask(__name__)

@app.route('/stock', methods=['GET'])
def get_stock_prices():
    ticker = request.args.get('ticker', None)
    if not ticker:
        return jsonify({"error": "Please provide a stock ticker"}), 400
    
    stock = yf.Ticker(ticker)
    hist = stock.history(period="1d")

    if hist.empty:
        return jsonify({"error": "Invalid stock ticker or no data available"}), 404

    # Convert the data to a dictionary format
    stock_data = hist[['Open', 'High', 'Low', 'Close', 'Volume']].iloc[0].to_dict()
    
    return jsonify(stock_data)

if __name__ == "__main__":
    app.run(debug=True)
