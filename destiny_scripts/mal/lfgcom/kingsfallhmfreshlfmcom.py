import time
import datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox()
browser.get('http://destinylfg.com')
assert 'DestinyLFG.com - The Bungie Featured Destiny LFG Site' in browser.title
time.sleep(6)

list_my_guardian = browser.find_element_by_xpath(".//*[@id='listMe']").click()
time.sleep(1.5)

select_console = browser.find_element_by_xpath(".//*[@id='selectConsole']/option[2]").click()
select_language = browser.find_element_by_xpath(".//*[@id='selectRegion']/option[2]").click()

psn_name = browser.find_element_by_xpath(".//*[@id='inputName']")
psn_name.send_keys('Conscious_Acts')
select_class = browser.find_element_by_xpath(".//*[@id='selectClass']/option[2]").click()
level = browser.find_element_by_xpath(".//*[@id='inputLvl']")
level.send_keys('40')
select_light = browser.find_element_by_xpath(".//*[@id='selectLight']/option[2]").click()
mic_select = browser.find_element_by_xpath(".//*[@id='listGuardian']/div[6]/div[1]/div/label").click()
i_am_lfm = browser.find_element_by_xpath(".//*[@id='selectLF']/option[3]").click()

# choose activity from list
select_activity = browser.find_element_by_xpath(".//*[@id='selectActivity']/optgroup[10]/option[1]").click()

# write description for activity chosen
description = browser.find_element_by_xpath(".//*[@id='textComment']")
description.send_keys("KING'S FALL FRESH RUN: Need 3 +305's with experience and good weapons. Message and Friend Request me on PSN to Join! PSN = Conscious_Acts")

list_me = browser.find_element_by_xpath(".//*[@id='listMeForm']").click()

time.sleep(120)
browser.quit()

print("Script completed at:")
print datetime.datetime.now()
print("Opening next script now...\n")

import oryxhmlfgcom
