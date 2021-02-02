from kiteconnect import KiteConnect
import pandas as pd
import talib
from datetime import datetime, timedelta

if __name__ == '__main__':
    api_key = open('api_key.txt', 'r').read()
    api_secret = open('api_secret.txt', 'r').read()

    kite = KiteConnect(api_key=api_key)
    print('a')

    # first time connection

    # print(kite.login_url())
    # data = kite.generate_session("",api_secret=api_secret)
    # print(data['access_token'])
    # kite.set_access_token(data['access_token'])
    #
    # with open('access_token.txt', 'w' ) as ak:
    #    ak.write(data['access_token'])
    access_token = open('access_token.txt','r').read()
    kite.set_access_token(access_token)
    # from date
    from_date = datetime.strftime(datetime.now() - timedelta(100),'%Y-%m-%d')

    ##yyyy-mm-dd
    to_date = datetime.today().strftime('%Y-%m-%d')

    ## time interval between data
    interval = '5minute'

    tokens = {486657: 'CUMMINSIND', 779521:'SBIN'}
    print('b')
    while True:
        if (datetime.now().second == 0) and (datetime.now().minute % 5 == 0):
         for token in tokens:
            records = kite.historical_data(token, from_date= from_date,to_date=to_date,interval=interval)
            df = pd.DataFrame(records)
            df.drop(df.tail(1).index,inplace=True)


            open = df['open'].values
            high = df['high'].values
            low = df['low'].values
            close = df['close'].values
            volume = df['volume'].values

            sma5 = talib.SMA(close,5)
            sma20 = talib.SMA(close,20)


            price = kite.ltp('NSE:' + tokens[token])


            ltp = price['NSE:'+ tokens[token]]['last_price']

            #Buy Sell Conditions
            if (sma5[-2]<sma20[-2]) and (sma5[-1]>sma20[-1]):

                buy_order_id = kite.place_order(variety= kite.VARIETY_REGULAR,
                                                exchange= kite.EXCHANGE_NSE,
                                                order_type= kite.ORDER_TYPE_MARKET,
                                                tradingsymbol=tokens[token],
                                                transaction_type= kite.TRANSACTION_TYPE_BUY,
                                                quantity= 10,
                                                validity= kite.VALIDITY_DAY,
                                                product= kite.PRODUCT_MIS,
                                                )
            if (sma5[-2]>sma20[-2]) and (sma5[-1]<sma20[-1]):
                sell_order_id = kite.place_order(variety=kite.VARIETY_REGULAR,
                                                exchange=kite.EXCHANGE_NSE,
                                                order_type=kite.ORDER_TYPE_MARKET,
                                                tradingsymbol=tokens[token],
                                                transaction_type=kite.TRANSACTION_TYPE_SELL,
                                                quantity=10,
                                                validity=kite.VALIDITY_DAY,
                                                product=kite.PRODUCT_MIS,
                                                )

            print(kite.orders())
            print(sma5[-2])
            print(sma5[-1])
            print(sma20[-2])
            print(sma20[-1])



