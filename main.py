from scrape_utils import retrieveWebpage
from sportsreview_importer import retrieveLinks, bulkDownloadData

def saveSportReviewWebpage():
  baseURL = 'https://www.sportsbookreviewsonline.com/scoresoddsarchives/nba/nbaoddsarchives.htm'
  saveFile = 'data/sportsbookreview_nba_odds_archive.html'
  element = '/html/body/table[2]/tbody/tr[1]/td[2]/table/tbody/tr[2]/td/ul/li[1]/a'
  retrieveWebpage(baseURL, saveFile, element)

def retrieveSportsReviewLinks():
  webpage = 'data/sportsbookreview_nba_odds_archive.html'
  base = 'https://www.sportsbookreviewsonline.com/scoresoddsarchives/nba/'
  saveFile = 'data/sportsbookreview_downloadable_archive_links.json'
  retrieveLinks(webpage, base, saveFile)

def main():
  # saveSportReviewWebpage()
  # retrieveSportsReviewLinks()
  saveFile = 'data/sportsbookreview_downloadable_archive_links.json'
  bulkDownloadData(saveFile)
if __name__ == "__main__":
  main()