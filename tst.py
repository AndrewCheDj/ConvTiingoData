import threading
from tiingo import TiingoClient

config = {}
config['session'] = True
config['api_key'] = "69954dec5d2661170ef8550cb28571cfa504c100"
client = TiingoClient(config)

# создаём список для приёма котировок
s=[]

# скачивание котировок через TiingoClient и запись в список s

def potock (thr):
    global s
    tickers = client.list_stock_tickers()  # получение списка тикеров (акций)
    for t in range(thr,len(tickers),10):
        a = tickers[t]['ticker']  # название акции
        quotes = client.get_ticker_price(a, fmt='json', startDate=str(tickers[t]['endDate']), frequency='daily')
        if quotes != []:  # отсекает встречающийся пустой список
            print([a, quotes[0]['high']])  # выводит название акции и котировку по заданному значению
            s.append([a, quotes[0]['high']])


for i in range(0,10):
    my_thread = threading.Thread(target=potock, args=(i,))
    my_thread.start()


