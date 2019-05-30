from tiingo import TiingoClient
import csv
config = {}
config['session'] = True
config['api_key'] = "69954dec5d2661170ef8550cb28571cfa504c100"
client = TiingoClient(config)
quotes = client.get_ticker_price('000001', fmt='json', startDate='1980-01-01', frequency='daily')
print (quotes)

with open("E:\code\ploe.txt","w") as out:
   for i in quotes:
      print(i,file=out)


def json_to_csv(quotes):
   with open("E:\code\pp.csv", 'w', newline='') as f:
      writer = csv.writer(f, delimiter=';')
      writer.writerow(
         ['date', 'o', 'h', 'l', 'c', 'v', 'a_o', 'a_h', 'a_l',
          'a_c', 'a_v', 'div', 'split'])
      for d in quotes:
         o = d['open']
         c = d['close']
         h = d['high']
         l = d['low']
         v = d['volume']
         adj_o = d['adjOpen']
         adj_c = d['adjClose']
         adj_h = d['adjHigh']
         adj_l = d['adjLow']
         adj_v = d['adjVolume']
         div_cash = d['divCash']
         split_factor = d['splitFactor']
         date = d['date'].split("T")[0].replace("-", "")
         writer.writerow(
            [date, o, h, l, c, v, adj_o, adj_h, adj_l, adj_c, adj_v, div_cash, split_factor])
json_to_csv(quotes)
print ('ok')