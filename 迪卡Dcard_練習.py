from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
# 顯性等待
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 1. 輸入網址、瀏覽器
PATH = r"chromedriver.exe"
driver = webdriver.Chrome(executable_path=PATH)
driver.get("https://www.dcard.tw/f")
# print(driver.title)



# 2. 等待、搜尋關鍵字
# 等待方法一: 強制等待
time.sleep(10)
# 等待方法二: 隱性等待
#driver.implicitly_wait(12)
# 等待方法三: 顯性等待   失敗!!!!!!!
#element = WebDriverWait(driver, 10).until(
#    EC.presence_of_element_located((By.NAME, "query"))
#)

search = driver.find_element(By.NAME, 'query')
search.clear()
search.send_keys('比特幣')
search.send_keys(Keys.RETURN)



# 3. 找到文章標題
titles = driver.find_elements(By.XPATH, '//a[@class="sc-8fe4d6a1-3 csyYas"]')
for title in titles:
    print(title.text)
print('= '*70)



# 4. 點擊 進入網頁
link = driver.find_element(By.LINK_TEXT, '奶奶竟然發現自己的才藝')
link.click()

# 5. 取得文章內容  未解決!!!!!!!!!!!!!!!!!!

conent = driver.find_elements(By.XPATH,'/html/body/div[2]/div/div[2]/div[1]/div/div/article/div[3]/div/div/span[1]')
print(conent)




driver.back()
driver.forward()

time.sleep(5)
driver.quit()

