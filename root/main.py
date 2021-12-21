from root.downloaders.arf_downloader.arf_downloader import arf_downloader
from root.login.login import login

if __name__ == '__main__':
    # False  True
    run_login = False
    run_downloader = True

    # User info:
    infocert_pass = ""
    infocert_email = ""
    webex_email = ""
    registrations_course_link = 'https://webeep.polimi.it/course/view.php?id=976&section=3'
    download_folder = '/Users/eb/Downloads'


    if run_login:
        login(infocert_pass, infocert_email,webex_email)

    if run_downloader:
        arf_downloader(registrations_course_link, download_folder)
