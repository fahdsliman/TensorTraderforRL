TensorTrade Trading Environment

Welcome to my TensorTrade Trading Environment project. This is a beginner-friendly Python project I built while learning algorithmic trading (algo trading) and Python programming. It creates a simulated trading environment using the TensorTrade library, where an AI can practice trading a fictional stock ("TTRD") with historical price data.

What Does This Project Do?

This code sets up a virtual trading "world" where:

You start with $1,000 in cash.
You can buy or sell a fake stock called "TTRD" on a fake exchange ("TTSE").
The AI uses past stock data (like prices and volume) to learn how to trade.
It’s all simulated—no real money is involved!
Think of it as a trading game for an AI to practice making money.

Prerequisites

Before running this, you’ll need:

Python 3.x installed (I used Python 3.9, but newer versions should work).
A CSV file with historical stock data (see "Data Format" below).
A GitHub account (if you want to fork or contribute!).
Installation

How to: 

Clone the Repository:
git clone https://github.com/[your-username]/[your-repo-name].git
cd [your-repo-name]
python -m venv venv source venv/bin/activate # On Windows: venv\Scripts\activate

pip install pandas tensortrade

Data Format The code expects a CSV file with these columns:

Datetime: Date and time (e.g., "2023-01-01 09:30:00"). Open: Opening price. High: Highest price. Low: Lowest price. Close: Closing price. Volume: Trading volume.

Example (data.csv):

Datetime,Open,High,Low,Close,Volume 2023-01-01 09:30:00,100.5,101.2,100.1,100.8,1000 2023-01-01 09:31:00,100.8,101.5,100.6,101.2,1200

You can use real stock data or make up your own!

How to Use Prepare Your Config: Create a Python dictionary with these settings:

config = { "csv_filename": "path/to/your/data.csv", "reward_window_size": 10, # How many steps to measure profit "window_size": 20, # How much past data the AI sees "max_allowed_loss": 0.2 # Stop if you lose 20% of starting cash }

Run the Code: Save the code in a file (e.g., trading_env.py), then:

from trading_env import create_env env = create_env(config) print("Trading environment created!")

This sets up the environment. Next steps would involve training an AI (not included here yet).

Project Structure trading_env.py: The main script that builds the trading environment. README.md: This file! What’s Inside the Code? Loads Data: Reads stock prices from a CSV file. Creates an Exchange: A fake market ("TTSE") with a 0.35% commission. Sets Up Money: Starts with $1,000 and 0 stocks in a portfolio. Prepares Data: Streams prices for the AI and display. Defines Rules: The AI can Buy, Sell, or Hold and earns points for profit. Builds the World: Combines everything into a trading simulator. Next Steps Add an AI model to train in this environment (e.g., reinforcement learning). Visualize trades with charts. Test with real stock data. Contributing This is a learning project, so I’d love feedback! Feel free to:

Fork the repo. Submit a pull request with improvements. Open an issue if something’s broken. Acknowledgments Thanks to TensorTrade for the awesome trading library. Inspired by online tutorials and my journey into Python and algo trading!
