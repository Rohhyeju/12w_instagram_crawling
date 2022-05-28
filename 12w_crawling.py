from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
import pandas as pd
from selenium.webdriver.common.by import By


id = 'selenium.pnu'
pw = 'selenium0527'

chromedriver = r'./chromedriver.exe'
driver = webdriver.Chrome(chromedriver)
driver.implicitly_wait(10)

driver.get('https://www.instagram.com/?hl=ko')

time.sleep(3)

id_inp = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label')
id_inp.click()
id_inp.send_keys(id)

pw_inp = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label')
pw_inp.click()
pw_inp.send_keys(pw)

log_btn = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button')
log_btn.click()

time.sleep(1)
option_btn = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button')
option_btn.click()

AlarmPopup = driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[3]/button[2]')
AlarmPopup.send_keys(Keys.ENTER)
time.sleep(2)

serch = driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input')
serch.send_keys('#코로나')
time.sleep(3)
serch.send_keys(Keys.ENTER)
serch.send_keys(Keys.ENTER)

driver.find_element_by_css_selector('div.v1Nh3.kIKUG._bz0w').click()
time.sleep(5)

results = []
count = 200
for i in range(count):
    data = driver.find_elements_by_css_selector('a.xil3i') 
    for j in range(len(data)):
        results.append(data[j].text.replace("#","")) 
    
    if (i+1)%10 == 0: 
        print('{}번째 게시물 완료'.format(i+1))
    driver.find_element_by_css_selector('div.l8mY4.feth3 > .wpO6b').send_keys(Keys.ENTER)
    time.sleep(3)
print(results)
driver.quit()

data = pd.DataFrame(results)
data.to_csv('./data.csv')
    












