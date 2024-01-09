import requests
import csv

url = "https://open-api.unisat.io/v1/indexer/block/"

headers = {
  "accept": "application/json",
  "Authorization": "Bearer YOUR_API_KEY"  
}

params = {
  "cursor": "0", 
  "size": "4000"
}

def get_data(block):
  full_url = url + str(block) + "/txs"
  response = requests.get(full_url, headers=headers, params=params)
  data = response.json()
  return data

csv_headers = ['block',
              'txid',
              'nIn',
              'nOut',
              'size',
              'witOffset',
              'locktime',
              'inSatoshi',
              'outSatoshi',
              'nNewInscription',
              'nInInscription',
              'nOutInscription',
              'nLostInscription',
              'timestamp',
              'height',
              'blkid',
              'idx',
              'confirmations']

def write_to_csv(data, block):
    with open('data.csv', 'a') as f:
        csv_writer = csv.writer(f)

        csv_writer.writerow(csv_headers)

        for item in data['data']:
          csv_writer.writerow([
              block,
              item['txid'],
              item['nIn'],
              item['nOut'],
              item['size'],
              item['witOffset'],
              item['locktime'],
              item['inSatoshi'],
              item['outSatoshi'],
              item['nNewInscription'],
              item['nInInscription'],
              item['nOutInscription'],
              item['nLostInscription'],
              item['timestamp'],
              item['height'],
              item['blkid'],
              item['idx'],
              item['confirmations'],
          ])

start_block = 823940 
end_block = 824940

def main():
  for block in range(start_block, end_block+1):
    data = get_data(block)
    write_to_csv(data, block)

if __name__ == '__main__':
  main()