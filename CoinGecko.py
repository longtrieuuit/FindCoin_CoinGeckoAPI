from pycoingecko import CoinGeckoAPI
import time
from logconfig import logger_coin as logger
cg = CoinGeckoAPI()
coins = cg.get_coins_list()

# exchanges = cg.get_exchanges_by_id('pancakeswap')
# print(exchanges)
total = len(coins)
STT = 0 
for coin in coins:
    
    STT = STT +1 

    if(STT<0):
        continue
    time.sleep(1.3)
    print(str(STT)+'/'+str(total))
    coin_id = coin['id']
    # coin_id = 'babyswap'

    for i in range(0,5):
        try:    
            dt = cg.get_coin_by_id(coin_id)
            break
        except:
            print("Error APU")
            time.sleep(1.3)

    market_list = []
    for market in dt['tickers']:
        # print(market)

        market_id = market['market']['identifier']
        if(market_id == 'pancakeswap'):
            SmartContract = market['base']
            # print(SmartContract)


        market_list.append(market_id)
    
    if(('pancakeswap' in market_list) and (('mxc' in market_list) or ('kucoin' in market_list) or ('gate' in market_list) or ('uniswap_v2' in market_list))):
        list_big_market = ['huobi','ftx_spot','binance']
        Check = True
        for b in list_big_market:
            if(b in market_list ):
                Check = False
                break
        
        if(Check):
            market_list = list( dict.fromkeys(market_list) )
            # print('CoinID: '+coin_id)
            logger.info(coin_id +': '+SmartContract+ ' - ' +str(market_list))
            # print(coin_id +': '+SmartContract+ ' - ' +str(market_list))

    # break

# print(len(exchanges))

