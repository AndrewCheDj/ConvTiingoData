# библиотеки для записи CSV
from tiingo import TiingoClient
import csv

# библиотеки для скачивания и анзипа котировок
import requests
import zipfile

# скачивание и анзип котировок
f = open(r'E:\code\tiingoCSV\tiingoDATA.zip', "wb")  # открывает файл для записи, в режиме wb
ufr = requests.get("https://apimedia.tiingo.com/docs/tiingo/daily/supported_tickers.zip")  # делает запрос
f.write(ufr.content)  # записывает содержимое в файл
f.close()

z = zipfile.ZipFile('E:\\code\\tiingoCSV\\tiingoDATA.zip', 'r')
z.printdir()
z.extract('supported_tickers.csv')


# всратые переменные
a=0
b=[]

# переработка котировок
with open ("E:\\code\\tiingoCSV\\code\\supported_tickers.csv", "r") as objcsv:
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
#               print(b[a - 1])  # выводит название акции
               print ([tick, quotes[0]['high']])         # выводит название акции и котировку по заданному значению
               writer = csv.writer(f, delimiter=';')
               writer.writerow([tick, quotes[0]['high']])

