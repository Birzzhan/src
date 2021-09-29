from pycoingecko import CoinGeckoAPI
gecko = CoinGeckoAPI()
def print_coin(coin):
    print(" current price of ", coin['symbol'], " is:  " , coin['current_price'], "$")

def sort_by_cap(e):
    return e['market_cap_rank']

while True:
    n = int(input(" Enter number to know top N cryptocurrencies by market capitalization: "))
    coin_list = gecko.get_coins_markets("usd")[:n]
    coin_list.sort(key=sort_by_cap)
    for coin in coin_list:
        print_coin(coin) 
