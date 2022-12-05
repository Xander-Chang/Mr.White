from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import time

start_time = time.process_time()

# 1. 瀏覽器、網址
path = 'chromedriver.exe'
driver = webdriver.Chrome(executable_path=path)
url = 'https://tsj.tw/'
driver.get(url)



# 2. 點擊'馬上吹'
blowing = driver.find_element(By.ID,'click')
# 3. 擁有技術點
blow_points = driver.find_element(By.XPATH,'//*[@id="app"]/div[2]/div[4]/div[2]/h4[2]')
# 4. 購買鍵
buying_buttoms = []
buying_buttoms.append(driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[4]/div[4]/table/tbody/tr[2]/td[5]/button[1]'))
buying_buttoms.append(driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[4]/div[4]/table/tbody/tr[3]/td[5]/button[1]'))
buying_buttoms.append(driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[4]/div[4]/table/tbody/tr[4]/td[5]/button[1]'))
print(buying_buttoms)
# 5. 價格
buying_prices = []
buying_prices.append(driver.find_element(By.XPATH,'//*[@id="app"]/div[2]/div[4]/div[4]/table/tbody/tr[2]/td[4]'))
buying_prices.append(driver.find_element(By.XPATH,'//*[@id="app"]/div[2]/div[4]/div[4]/table/tbody/tr[3]/td[4]'))
buying_prices.append(driver.find_element(By.XPATH,'//*[@id="app"]/div[2]/div[4]/div[4]/table/tbody/tr[4]/td[4]'))
print(buying_prices)



# 6. 建立 actions 物件 、 點擊
actions = ActionChains(driver)     #建立 執行物件
actions.click(blowing)



# 7. 開始吹

for i in range(1000):
    actions.perform()
    points = int(blow_points.text.replace('您目前擁有', '').replace('技術點', ''))    # points放在迴圈外面 永遠是0
    for j in range(3): 
        needed_price = int(buying_prices[j].text.replace('技術點',''))

        if points >= needed_price:
            # 購買的動作  建立另一個 ActionChains(driver)
            upgrade_actions = ActionChains(driver)
            upgrade_actions.move_to_element(buying_buttoms[j])    # 第 j 個足夠就買第 j 個,
            upgrade_actions.click()
            upgrade_actions.perform()
            break

    if points > 1000:
        break




end_time = time.process_time()
print('花費時間:', end_time-start_time)
time.sleep(5)
driver.close()