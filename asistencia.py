import sys

from selenium.webdriver import Edge, Chrome, Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

links = ['https://eva.unl.edu.ec/mod/attendance/view.php?id=1197294']

class Asistant():
    driver = ''
    wait = ''

    def select_browser(self, browser):
        if browser == 'edge':
            self.driver = Edge(executable_path='./drivers/msedgedriver.exe')
            self.wait = WebDriverWait(self.driver, 10)
        elif browser == 'chrome':
            self.driver = Chrome(executable_path='./drivers/chromedriver.exe')
            self.wait = WebDriverWait(self.driver, 10)
        elif browser == 'firefox':
            self.driver = Firefox(executable_path='./drivers/geckodriver.exe')
            self.wait = WebDriverWait(self.driver, 10)
        else:
            self.driver = Edge(executable_path='./drivers/msedgedriver.exe')
            self.wait = WebDriverWait(self.driver, 10)

    def open_website(self, url):
        self.driver.get(url)

    def login_in_platform(self, email, passwd):
        input_user = self.wait.until(
            EC.presence_of_element_located(
                (By.XPATH, '//body//div//form//input[@id="username"]')
            )
        )
        input_pass = self.driver.find_element(
            By.XPATH, '//body//div//form//input[@id="password"]')
        button_login = self.driver.find_element(
            By.XPATH, '//form//input[@value="INICIAR SESIÓN"]')

        input_user.send_keys(email)
        input_pass.send_keys(passwd)
        button_login.click()

    def open_asistant_page(self):
        link_asistence = self.wait.until(
            EC.presence_of_element_located(
                (By.XPATH,
                 '//table//tbody//td//a[contains(text(), "Enviar asistencia")]')
            )
        )

        link_asistence.click()

    def set_asistant(self):
        input_present = self.wait.until(
            EC.presence_of_element_located(
                (By.XPATH, '//input[@id="id_status_10442"]'))
        )
        send_assistant = self.driver.find_element(
            By.XPATH, '//input[@id="id_submitbutton"]')

        input_present.click()
        send_assistant.click()

    def close_browser(self):
        self.driver.close()
        

if __name__ == '__main__':
    core = Asistant()
    core.select_browser('firefox')
    core.open_website('https://google.com')
    core.login_in_platform('', '')
    core.close_browser()