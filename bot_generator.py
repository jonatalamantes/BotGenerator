from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()
driver.get('https://facebook.com')

#logins to facebook credential, edit them
user_facebook = 'someemail@email.com'
pass_facebook = 'somepassword'

with open('jquery.js', 'r') as _f:
    jquery = _f.read()

#try to login using the preview credentiales
try:
    elem = driver.find_element_by_id('email')
    elem.clear()    
    elem.send_keys(user_facebook)

    elem = driver.find_element_by_id('pass')
    elem.clear()
    elem.send_keys(pass_facebook)

    elem.send_keys(Keys.RETURN)
except:
    pass

#Edit the follow range for more bots
for i in range(5,10):

    #Also you can change the bot name
    _botname = 'Bot{0}'.format(i)

    #Load the page face
    driver.get('https://www.facebook.com/pages/creation/?ref_type=logout_gear')
    driver.execute_script(jquery)

    time.sleep(3)
    driver.execute_script("$('._43rl')[2].click()")
    time.sleep(1)

    #Register the page
    elems = driver.find_elements_by_class_name('_58al')
    elems[2].clear()
    elems[2].send_keys(_botname)

    elems[3].clear()
    elems[3].send_keys('Solo')
    time.sleep(5)
    elems[3].send_keys(Keys.RETURN)

    driver.execute_script("$('._43rl')[3].click()")
    time.sleep(2)

    #Dont upload photo
    driver.execute_script(jquery)
    driver.execute_script("$('._42ft')[4].click()")
    time.sleep(2)

    driver.execute_script(jquery)
    driver.execute_script("$('._42ft')[4].click()")
    time.sleep(2)

    #Load the Challange page
    driver.get('https://www.facebook.com/somefacebookpage')
    driver.execute_script(jquery)

    driver.execute_script("$('._55pi')[11].click()")
    time.sleep(1)
    driver.execute_script("$('._alf:contains(\"{0}\")')[0].click()".format(_botname))
    time.sleep(1)

    driver.execute_script("$('._1mto > ._khz._4sz1 > .accessible_elem')[8].click()")
    time.sleep(1)

    driver.execute_script("$('._628b > span')[1].click()")
    time.sleep(1)

driver.close()
