from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# explicit waits
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

path = 'chromedriver.exe'
driver = webdriver.Chrome(executable_path=path)
url = 'https://www.instagram.com/'
driver.get(url)

# 進入之前有等待時間
# driver.implicitly_wait(10)
# 帳號
username = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.NAME, 'username'))
)
username.clear()
username.send_keys('kle6463162@gmail.com')

# 密碼
password = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.NAME, 'password'))
)
password.clear()
password.send_keys('klo84323')

# 登入
login = driver.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[3]/button').click()
# 搜尋 頁面跳轉 一樣有等待時間
search = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="react-root"]/div/div/section/nav/div[2]/div/div/div[2]/input'))
)
search.find_element(By.XPATH,'//*[@id="react-root"]/div/div/section/nav/div[2]/div/div/div[2]/input')







# !!!!!!!!無法搜尋  未解決
search.send_keys('#cat')
time.sleep(1)
search.send_keys(Keys.RETURN)
time.sleep(1)
search.send_keys(Keys.RETURN)



#driver.close()