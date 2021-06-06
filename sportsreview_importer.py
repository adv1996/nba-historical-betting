from bs4 import BeautifulSoup
from utils import saveToJSON
import os
import json

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

import os
import json

def bulkDownloadData(base):
  data = {}
  with open(base) as dataFile:
    data = json.load(dataFile)
  
  links = data.keys()
  for link in links:
    name = data[link]['raw']
    url = data[link]['url']
    filename = 'data/downloaded_data/' + name + '.xlsx'
    os.system('wget -O "{0}" "{1}"'.format(filename, url))

  print('finished downloading')