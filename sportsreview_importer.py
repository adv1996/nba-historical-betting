from bs4 import BeautifulSoup
from utils import saveToJSON
import os
import json
import pandas as pd

def retrieveLinks(webpage, base, saveFile):
  htmlFile = ""
  with open(webpage) as dataFile:
    htmlFile = dataFile.read()

  soup = BeautifulSoup(htmlFile, 'html.parser')
  downloadTable = soup.findAll('table')[6]
  downloadLinks = downloadTable.findAll('a')
  
  data = {}

  for link in downloadLinks:
    link_id = link.text
    data[link_id] = {
      "raw": link.text,
      "url": base + link['href'],
    }
  saveToJSON(saveFile, data)
  return data

def bulkDownloadData(base):
  retval = getSeasonKeys(base)
  data = retval[0]
  links = retval[1]

  for link in links:
    name = data[link]['raw']
    url = data[link]['url']
    filename = 'data/downloaded/' + name + '.xlsx'
    os.system('wget -O "{0}" "{1}"'.format(filename, url))

  print('finished downloading')

def getSeasonKeys(base):
  data = {}
  with open(base) as dataFile:
    data = json.load(dataFile)
  links = data.keys()
  return [data, links]

def collateData(base):
  seasonKeys = getSeasonKeys(base)[1]
  collated_df = pd.DataFrame()
  for season in seasonKeys:
    download_file = f'data/downloaded/{season}.xlsx'
    df = pd.read_excel(download_file, index_col=None)
    collated_df = pd.concat([collated_df, df])
  collated_df.to_csv('data/processed/collated_data.csv')