import pickle
from time import sleep
from selenium import webdriver

def load_session():
    #init firefox
    fp = webdriver.FirefoxProfile('/Users/eb/PycharmProjects/webex_downloader/bin/firefox_profiles/rust_mozprofileiEZYZK')
    fp.set_preference("browser.helperApps.alwaysAsk.force", False)
    fp.set_preference("browser.download.manager.showWhenStarting", False)
    driver = webdriver.Firefox(executable_path=r'/Users/eb/Documents/geckodriver', firefox_profile=fp)

    #go to webex
    webex = 'https://politecnicomilano.webex.com'
    driver.get(webex)

    #load webex-cookies
    try:
        cookies = pickle.load(open("/Users/eb/PycharmProjects/webex_downloader/bin/webex.pkl", "rb"))
        for cookie in cookies:
            driver.add_cookie(cookie)
        print('webex cookies loaded')
    except Exception as e:
        print(e)
        print('cookies not found')

    sleep(3)
    driver.find_element_by_css_selector('#guest_signin_split_button-action > span:nth-child(1)').click()
    sleep(5)

    #go to webeep
    webeep = 'https://webeep.polimi.it/my/'
    driver.get(webeep)

    sleep(5)

    # load webeep-cookies
    try:
        cookies = pickle.load(open("/Users/eb/PycharmProjects/webex_downloader/bin/webeep.pkl", "rb"))
        for cookie in cookies:
            driver.add_cookie(cookie)
        print('webeep cookies loaded')
    except Exception as e:
        print(e)
        print('cookies not found')

    sleep(3)
    # open webeep
    # log in webeep using cookies
    driver.find_element_by_css_selector('a.btn:nth-child(1) > span:nth-child(1)').click()

    sleep(5)

    return driver

