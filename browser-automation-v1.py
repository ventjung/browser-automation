# ventjung browser-automation v1
# what does it do : 
# 1- automatically login facebook
# 2- and like the first post available

from time import sleep
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

# option to disable notification
chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)

# start chrome
browser = webdriver.Chrome(executable_path='./chromedriver.exe', chrome_options=chrome_options)
browser.get('https://www.facebook.com')

# login routine
emailInput = browser.find_element_by_id("email")
passwordInput = browser.find_element_by_id("pass")
loginButton = browser.find_element_by_xpath("//form/table/tbody/tr/td/label/input")

ActionChains(browser)\
    .move_to_element(emailInput)\
    .click()\
    .send_keys("your email")\
    .perform()

ActionChains(browser)\
    .move_to_element(passwordInput)\
    .click()\
    .send_keys("your password")\
    .perform()

ActionChains(browser)\
    .move_to_element(loginButton)\
    .click()\
    .perform()

sleep(5)

# for feed post list
# posts = browser.find_elements_by_xpath('//div[@class="_5jmm _5pat _3lb4 b_x07tm_r9z"]')

# like first unliked post

likeButton = browser.find_element_by_xpath('//a[@class=" _6a-y _3l2t  _18vj"]')

ActionChains(browser)\
    .move_to_element(likeButton)\
    .click()\
    .perform()

sleep(5)

# close browser
browser.close()