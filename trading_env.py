import pandas as pd
from tensortrade.feed.core import DataFeed, Stream
from tensortrade.oms.instruments import Instrument
from tensortrade.oms.exchanges import Exchange, ExchangeOptions
from tensortrade.oms.services.execution.simulated import execute_order
from tensortrade.oms.wallets import Wallet, Portfolio
import tensortrade.env.default as default


def create_env(config):
    # Read CSV and handle missing values
    dataset = pd.read_csv(
        filepath_or_buffer=config["csv_filename"],
        parse_dates=['Datetime']
    ).fillna(method='backfill').fillna(method='ffill')

    ttse_commission = 0.0035  # TODO: adjust according to your commission percentage
    price = Stream.source(list(dataset["Close"]), dtype="float").rename("USD-TTRD")
    ttse_options = ExchangeOptions(commission=ttse_commission)
    ttse_exchange = Exchange("TTSE", service=execute_order, options=ttse_options)(price)

    # Instruments, Wallets and Portfolio
    USD = Instrument("USD", 2, "US Dollar")
    TTRD = Instrument("TTRD", 2, "TensorTrade Corp")
    cash = Wallet(ttse_exchange, 1000 * USD)
    asset = Wallet(ttse_exchange, 0 * TTRD)
    portfolio = Portfolio(USD, [cash, asset])

    # Renderer feed
    renderer_feed = DataFeed([
        Stream.source(list(dataset["Datetime"])).rename("date"),
        Stream.source(list(dataset["Open"]), dtype="float").rename("open"),
        Stream.source(list(dataset["High"]), dtype="float").rename("high"),
        Stream.source(list(dataset["Low"]), dtype="float").rename("low"),
        Stream.source(list(dataset["Close"]), dtype="float").rename("close"),
        Stream.source(list(dataset["Volume"]), dtype="float").rename("volume")
    ])

    # Features feed
    features = []
    for c in dataset.columns[1:]:
        s = Stream.source(list(dataset[c]), dtype="float").rename(c)
        features.append(s)

    feed = DataFeed(features)
    feed.compile()

    reward_scheme = default.rewards.SimpleProfit(window_size=config["reward_window_size"])
    action_scheme = default.actions.BSH(cash=cash, asset=asset)

    env = default.create(
        feed=feed,
        portfolio=portfolio,
        action_scheme=action_scheme,
        reward_scheme=reward_scheme,
        renderer_feed=renderer_feed,
        renderer=[],
        window_size=config["window_size"],
        max_allowed_loss=config["max_allowed_loss"]
    
    return env