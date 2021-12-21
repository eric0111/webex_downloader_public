#saving cookies
def save_cookies():
    import pickle
    from selenium import webdriver
    driver = webdriver.Firefox()
    driver.get('http://www.quora.com')
    # login code
    pickle.dump(driver.get_cookies() , open("Cookies.pkl","wb"))

#loading cookies
def load_cookies():
    import pickle 
    from selenium import webdriver 
    driver = webdriver.Firefox() 
    driver.get('http://www.quora.com') 
    for cookie in pickle.load(open("Cookies.pkl", "rb")): 
        driver.add_cookie(cookie) 