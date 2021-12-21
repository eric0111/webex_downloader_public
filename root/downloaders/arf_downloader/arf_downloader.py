from time import sleep
from root.downloaders.arf_downloader.load_arf_modules import load_arf_modules
from root.downloaders.arf_downloader.wait_until_downloaded import wait_until_downloaded
from root.load_session.load_session import load_session
import os

def arf_downloader(registrations_course_link, download_folder):
    driver = load_session()
    sleep(8)

    modules = load_arf_modules(driver, registrations_course_link)

    urls = []
    #get download links
    for module in modules:
        #go to module
        url = module.get_attribute('href')
        print(url)
        urls.append(url)


    #download every arf module
    for url in urls:
        #clean folder from old .part files
        sleep(2)
        files = os.listdir(download_folder)
        for file in files:
            if '.part' in file:
                os.remove(download_folder+'/'+file)
                os.remove(download_folder+'/'+file.split('.part')[0])

        #go to module
        driver.get(url)
        sleep(5)

        #go to webex
        url = driver.find_element_by_css_selector('.urlworkaround > a:nth-child(1)').get_attribute('href')

        if 'webex' in url:
            print(url)
            driver.get(url)
            sleep(5)
            title = driver.find_element_by_class_name('recordingTitle').text + '.mp4'
            files = os.listdir(download_folder)
            print(title)

            if(title in files):
                print('already downloaded')

            else:
                #download modul but wait to go forward until downloaded

                print('downloading : '+url)
                sleep(5)
                driver.find_element_by_class_name("icon-download").click()
                wait_until_downloaded(download_folder, title)

        else:
            print('not a webex link!')

        # # go back to arf homepage
        # webeep = 'https://webeep.polimi.it/course/view.php?id=976&section=3'
        # driver.get(webeep)
