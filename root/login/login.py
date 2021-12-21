import pickle
from time import sleep
from selenium import webdriver

def login(infocert_pass, infocert_email, webex_email):
    start_site = 'https://webeep.polimi.it/'
    fp = webdriver.FirefoxProfile()

    driver = webdriver.Firefox(executable_path=r'/Users/eb/Documents/geckodriver',firefox_profile=fp)

    #go to webeep
    driver.get(start_site)

    #webeep login
    driver.find_element_by_css_selector('a.btn:nth-child(1) > span:nth-child(1)').click()

    #infocert login
    driver.find_element_by_css_selector('#RESTA_CONNESSO').click()
    driver.find_element_by_css_selector('.italia-it-button-text').click()
    driver.find_element_by_name('infocert_id').click()
    sleep(5)

    #fill infocert data
    driver.find_element_by_css_selector('#username').send_keys(infocert_email)
    driver.find_element_by_css_selector('#password').send_keys(infocert_pass)
    driver.find_element_by_css_selector('.italia-it-button-text').click()

    #manually confirm infocert-spid notification
    print('click on spid phone notification')
    sleep(30)

    #save webeep cookies
    pickle.dump(driver.get_cookies(), open("/Users/eb/PycharmProjects/webex_downloader/bin/webeep.pkl", "wb"))
    print('Webeep Cookies Saved')

    sleep(5)

    #webex login
    driver.get('https://politecnicomilano.webex.com')
    sleep(3)
    driver.find_element_by_css_selector('#guest_signin_split_button-action > span:nth-child(1)').click()
    sleep(8)
    driver.find_element_by_xpath('//*[@id="IDToken1"]').send_keys(webex_email)
    sleep(5)
    driver.find_element_by_xpath('//*[@id="IDButton2"]').click()
    sleep(8)

    #save webex cookies
    pickle.dump(driver.get_cookies(), open("/Users/eb/PycharmProjects/webex_downloader/bin/webex.pkl", "wb"))
    print('Webex Cookies Saved')

    sleep(5)
    driver.close()
