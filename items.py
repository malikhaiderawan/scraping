from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By 
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
query='concerts'
driver.get(f"https://www.stubhub.com/secure/search?q={query}&searchguid=a64353b4-a3b3-4633-86e1-5698ef1c32d2")

elem = driver.find_elements(By.TAG_NAME, "ul")



l = []
for i in elem:
  
  li_elems = i.find_elements(By.TAG_NAME, "li")
  for m in li_elems:
    title=m.find_elements(By.TAG_NAME , "span")
    for z in title:
      title = z.text
      print(f"Title: {title}")
    
    z=l.append(
      {
        'title':title
      }
    )
    print(z)
print(l)


driver.close()
