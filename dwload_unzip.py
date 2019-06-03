import requests
import zipfile

f = open(r'E:\code\tiingoCSV\tiingoDATA.zip', "wb")  # открываем файл для записи, в режиме wb
ufr = requests.get("https://apimedia.tiingo.com/docs/tiingo/daily/supported_tickers.zip")  # делаем запрос
f.write(ufr.content)  # записываем содержимое в файл
f.close()

z = zipfile.ZipFile('E:\\code\\tiingoCSV\\tiingoDATA.zip', 'r')
z.printdir()
z.extract('supported_tickers.csv')
