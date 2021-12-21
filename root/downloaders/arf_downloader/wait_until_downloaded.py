import os
from time import sleep


def wait_until_downloaded(download_folder, title):
    sleep(5)
    while True:
        files = os.listdir(download_folder)
        partial_file = title+'.part'
        if partial_file in files:
            sleep(20)
            print('still downloading, going to sleep')
        else:
            break
