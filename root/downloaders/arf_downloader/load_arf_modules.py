

def load_arf_modules(driver,registrations_course_link):
    # go to webex and load arf modules
    # driver.find_element_by_css_selector(
    #     '#course-info-container-976-4 > div:nth-child(1) > div:nth-child(1) > a:nth-child(2) > span:nth-child(3)').click()
    # driver.find_element_by_css_selector(
    #     '#section-3 > a:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1)').click()

    driver.get(registrations_course_link)
    modules = driver.find_elements_by_partial_link_text(
        'Registrazione')  # find_element_by_id("//*[contains(@id, 'module')]")

    return modules