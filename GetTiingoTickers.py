from tiingo import TiingoClient
import csv

a=0
b=[]

with open ("E:\\code\\tiingoCSV\\supported_tickers.csv", "r") as objcsv:
   reader = csv.reader(objcsv)
   for row in reader:
      ticker = str(row[0])         # названия акций
      if row[4] != '':             # отсечение данных без даты
          b.append(ticker)         # создание списка из названий акций
   print (b)                       # печать этого списка


config = {}
config['session'] = True
config['api_key'] = "69954dec5d2661170ef8550cb28571cfa504c100"
client = TiingoClient(config)

with open("E:\\code\\tiingoCSV\\rec.csv", 'w', newline='') as f:
    for tick in b:
       a += 1
       if a > 1:  # отсечение первой строки так как в ней нет полезной для нас информации и пустых по дате строк
           quotes = client.get_ticker_price(tick, fmt='json', startDate=str(row[5]), frequency='daily')
           if quotes != []:     # отсекает встречающийся пустой список
               print(b[a - 1])  # выводит название акции
               writer = csv.writer(f, delimiter=';')
               writer.writerow([tick, quotes[0]['high']])

