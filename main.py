from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)
file = 0
query = "trimmer for men"
query_1 = query.replace(" ", "-")
query_2 = query.replace(" ", "+")
for i in range(1,60):
    driver.get(f"https://www.aliexpress.com/w/wholesale-{query_1}.html?page={i}&g=n&SearchText={query_2}")
    
    elements = WebDriverWait(driver, 20).until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'multi--content-list--3630fHz')))
        
    for elem in elements:
        outer_html = elem.get_attribute('outerHTML')
        with open(f"data/{query}_{file}.html", "w", encoding="utf-8") as f:
            f.write(outer_html)
            file += 1
driver.close()