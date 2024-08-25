from flask import Flask, request, jsonify
import yfinance as yf
import pandas as pd

app = Flask(__name__)

@app.route('/stock_prices', methods=['GET'])
def get_stock_prices():
    # Get stock ticker from query parameters
    ticker = request.args.get('ticker')
    
    if not ticker:
        return jsonify({'error': 'Ticker is required'}), 400
    
    # Fetch stock data
    try:
        stock = yf.Ticker(ticker)
        hist = stock.history(period="1d")
        hist.reset_index(inplace=True)

        # Convert the DataFrame to a dictionary format for JSON serialization
        data = hist.to_dict(orient="records")
        return jsonify(data), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
