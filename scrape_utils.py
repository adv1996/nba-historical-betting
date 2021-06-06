from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from utils import saveToHTML

def retrieveWebpage(baseURL, saveFile, element):
  options = webdriver.ChromeOptions()
  options.add_argument("--headless")
  driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
  driver.get(baseURL)
  try:
    WebDriverWait(driver, 10).until(
      EC.presence_of_element_located((By.XPATH, element))
    )
    saveToHTML(saveFile, driver.page_source)
  except Exception as e:
    print('cannot find it')
  finally:
    driver.quit()
