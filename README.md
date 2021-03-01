# Algo-Trading-with-python

Data : NSE live and historical data

Tool : Pycharm, kiteconnect, kite.trade

Packages: numpy,pandas,datetime,talib,tsf

Objective:
Get the data from live API, Using python(Zerodha Documentation) Automated trade calls (buy,sell) 
whwn the given condition is satisfied

BUY/SELL Condtion:
Intraday Simple moving average strategy:
SMA20,SMA5

buy when sma5 > sma20
sell when sma5 < sma 20

Calcualted the sma for both live data and historic data in real time for the past 100 days 

TIME Condition:
Interval is given as 5 and the program runs in a continuos while loop where the condition satisfies
every five minutes.

Results

The sma is a very good strategy for intraday however picking the stock is whole different scenario.
I'm gonna update this repository with more interesting strategies and continue to implement advanced
algorithms in addition to the current stratagies.

connect on linkedin for questions:
https://www.linkedin.com/in/muthurishikesh/
