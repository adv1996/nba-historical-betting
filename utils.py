import json

def saveToHTML(filename, data):
  with open(filename, 'w') as tfile:
    tfile.write(data)

def saveToJSON(filename, data):
  with open(filename, 'w') as fname:
    json.dump(data, fname)
  print('saved to', filename)