# https://www.dumskaya.net/

def register_user():
    from factory.new_user import User
    from selenium import webdriver
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.chrome.service import Service
    from selenium.webdriver.chrome.options import Options as ChromeOptions
    import os


    my_user12 = User()
    my_user12.password2 = my_user12.password + my_user12.password


    options = ChromeOptions()
    options.headless = True  # True Запуск теста без включения браузера

    path = f'{os.getcwd()}/drivers/chromedriver'
    service = Service(executable_path=path)
    driver = webdriver.Chrome(service=service, options=options)
    url = 'https://www.dumskaya.net/'

    driver.maximize_window()
    driver.get(url)

    xpath_enter_button = '//a[@id="pp"]/b'
    xpath_enter_registration_button = '//a[@href="/register/"]'

    xpath_register_email = '//td/input[@name="email"]'
    xpath_register_nick = '//input[@name="nick"]'
    xpath_register_password = '//input[@name="password1"]'
    xpath_register_password2 = '//input[@name="password2"]'
    xpath_register_gender_male = '//input[@name="gender"][@value="m"]'
    xpath_register_button = '//input[@type="submit"]/following::input[@type="submit"]'  # XPath Axis ось XPath
    # xpath_user_finish = '//a[@class="celluname1"]'

    enter_button = WebDriverWait(driver, 30).until(EC.presence_of_element_located(('xpath', xpath_enter_button)))
    enter_button.click()
    enter_registration_button = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located(('xpath', xpath_enter_registration_button)))
    enter_registration_button.click()

    register_email_field = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located(('xpath', xpath_register_email)))
    register_email_field.send_keys(my_user12.email)

    register_nick_field = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located(('xpath', xpath_register_nick)))
    register_nick_field.send_keys(my_user12.nick)

    register_password = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located(('xpath', xpath_register_password)))
    register_password.send_keys(my_user12.password)

    register_password2 = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located(('xpath', xpath_register_password2)))
    register_password2.send_keys(my_user12.password2)

    register_gender_male = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located(('xpath', xpath_register_gender_male)))
    register_gender_male.click()

    register_gender_button = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located(('xpath', xpath_register_button)))
    register_gender_button.click()

    login_textarea = WebDriverWait(driver, 30).until(EC.presence_of_element_located(('xpath', '//td[@class="newscol"]/div')))
    login = login_textarea.text

    error_password = 'Пароли не совпадают.'
    driver.close()

    return login, error_password



if __name__ == '__main__':
    print(register_user())