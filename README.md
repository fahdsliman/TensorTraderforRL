# TensorTrade Trading Environment

![Python](https://img.shields.io/badge/python-3.9%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![TensorTrade](https://img.shields.io/badge/TensorTrade-0.2.2-orange)

## Purpose of project

This project sets up a virtual trading "world" where:
- You start with $1,000 in cash and 0 stocks.
- Trade a fictional stock ("TTRD") on a simulated exchange ("TTSE") with a 0.35% commission.
- The AI uses historical stock data (prices and volume) to learn trading strategies.
- Ideal for learning algorithmic trading and reinforcement learning in a safe, simulated environment.

## Prerequisites

- **Python**: Version 3.9 or higher.
- **GitHub**: Account to fork or contribute (optional).
- **Data**: A CSV file with historical stock data (see [Data Format](#data-format)).

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/[your-username]/TensorTrade-Trading-Environment.git
   cd TensorTrade-Trading-Environment
   ```

2. **Set Up a Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Data Format

The code expects a CSV file (e.g., `data/data.csv`) with the following columns:
- `Datetime`: Date and time (e.g., "2023-01-01 09:30:00").
- `Open`: Opening price.
- `High`: Highest price.
- `Low`: Lowest price.
- `Close`: Closing price.
- `Volume`: Trading volume.

**Example (`data.csv`)**:
```csv
Datetime,Open,High,Low,Close,Volume
2023-01-01 09:30:00,100.5,101.2,100.1,100.8,1000
2023-01-01 09:31:00,100.8,101.5,100.6,101.2,1200
```

You can use real stock data (e.g., from Yahoo Finance) or create synthetic data.

## Usage

1. **Prepare Configuration**:
   Create a Python dictionary in your script with these settings:
   ```python
   config = {
       "csv_filename": "data/data.csv",
       "reward_window_size": 10,  # Steps to measure profit
       "window_size": 20,         # Past data for AI
       "max_allowed_loss": 0.2    # Stop if 20% of cash is lost
   }
   ```

2. **Run the Environment**:
   Save the configuration and run the main script:
   ```python
   from src.trading_env import create_env
   env = create_env(config)
   print("Trading environment created!")
   ```

   This sets up the trading environment. You can extend it by adding an AI model (e.g., reinforcement learning) to train within this environment.

## Project Structure

- `src/trading_env.py`: Main script to create the trading environment.
- `data/data.csv`: Sample historical stock data.
- `requirements.txt`: Lists Python dependencies.
- `.gitignore`: Excludes unnecessary files (e.g., virtual env, cache).
- `README.md`: Project documentation.

## How It Works

The code:
1. **Loads Data**: Reads stock prices from a CSV file.
2. **Creates Exchange**: Simulates a market ("TTSE") with a 0.35% commission.
3. **Sets Up Portfolio**: Starts with $1,000 and 0 stocks.
4. **Streams Data**: Provides price data for AI and visualization.
5. **Defines Rules**: Allows Buy, Sell, or Hold actions with profit-based rewards.
6. **Builds Environment**: Combines components into a trading simulator.

## Next Steps

- Train an AI model (e.g., using reinforcement learning) in this environment.
- Add visualizations for trades (e.g., using Matplotlib).
- Test with real-world stock data.
- Enhance with features like transaction costs or risk management.

## Contributing

This is a learning project, and feedback is welcome! To contribute:
1. Fork the repository.
2. Create a feature branch (`git checkout -b feature/YourFeature`).
3. Commit changes (`git commit -m "Add YourFeature"`).
4. Push to the branch (`git push origin feature/YourFeature`).
5. Open a pull request.

Please report issues or suggest improvements via GitHub Issues.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [TensorTrade](https://github.com/tensortrade-org/tensortrade) for the trading library.
- Inspired by online algorithmic trading tutorials and Python learning resources.
