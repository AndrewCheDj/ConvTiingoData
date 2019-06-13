# библиотеки для записи CSV
from tiingo import TiingoClient
import csv
import threading  # библиотека для создания потоков



def get_rates ():
    threads = []
    print(threads)
    for y in range(5):
        a=threads.append(threading.Thread(target=get_rates, args=(y))

    # Запускаем каждый поток
    for thread in threads:
       thread.start()
       print ('starting thread'+ str(pair))

    # Ждем завершения каждого потока
    for thread in threads:
       thread.join()
get_rates ()





config = {}
config['session'] = True
config['api_key'] = "69954dec5d2661170ef8550cb28571cfa504c100"
client = TiingoClient(config)

# скачивание котировок через TiingoClient и запись в файл CSV
with open("E:\\code\\tiingoCSV\\rec.csv", 'w', newline='') as f:
    tickers = client.list_stock_tickers()    # получение списка тикеров (акций)
    for t in range(len(tickers)):
        a = tickers[t]['ticker']  # название акции
        quotes = client.get_ticker_price(a, fmt='json', startDate=str(tickers[t]['endDate']), frequency='daily')
        if quotes != []:  # отсекает встречающийся пустой список
            print([a, quotes[0]['high']])  # выводит название акции и котировку по заданному значению
            writer = csv.writer(f, delimiter=';')
            writer.writerow([a, quotes[0]['high']])


