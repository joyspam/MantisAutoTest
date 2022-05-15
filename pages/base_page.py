from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .locators import BasePageLocators, BagReportLocators
from selenium.webdriver.support.ui import Select


class BasePage:
    # метод, который вызывается, когда мы создаем объект
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    # должен открывать нужную страницу в браузере, используя метод get()
    def open(self):
        self.browser.get(self.url)

    # элемент появляется на странице
    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    # элемент не появляется на странице в течение заданного времени:
    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True

        return False

    # будет ждать до тех пор, пока элемент не исчезнет:
    def is_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException). \
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False

        return True

    # методы для всех страниц

    # авторизация вход
    def go_to_login_page(self):
        # данные для ввода
        login = "joyrox"
        password = "34aJD6w4kz@9JqX"

        assert self.is_element_present(*BasePageLocators.LOGIN_PAGE), "mat-1. No login_page button"
        link = self.browser.find_element(*BasePageLocators.LOGIN_PAGE)
        link.click()
        self.browser.find_element(*BasePageLocators.LOGIN).send_keys(login)
        assert self.is_element_present(*BasePageLocators.ENTER_LOGIN), "mat-2. No login button"
        link = self.browser.find_element(*BasePageLocators.ENTER_LOGIN)
        link.click()
        self.browser.find_element(*BasePageLocators.PASSWORD).send_keys(password)
        assert self.is_element_present(*BasePageLocators.ENTER_PASSWORD), "mat-3. No password button"
        link = self.browser.find_element(*BasePageLocators.ENTER_PASSWORD)
        link.click()
        assert self.is_element_present(*BasePageLocators.REG_OK), "mat-4. Authorisation is failed"

    # переход на страницу создания проекта(бага)
    def go_to_choose_project(self):
        assert self.is_element_present(*BasePageLocators.CHOOSE_PROJECT), "mat-5. No project bottom from my_view_page"
        button = self.browser.find_element(*BasePageLocators.CHOOSE_PROJECT)
        button.click()
        assert self.is_element_present(
            *BasePageLocators.CHOOSE_PROJECT_BUTTON), "mat-6. No project bottom from bugs/login_select_proj_page"
        button = self.browser.find_element(*BasePageLocators.CHOOSE_PROJECT_BUTTON)
        button.click()

        # здесь можно создать отдельную страницу bag_report.py для крупного теста

        # данные для ввода
        category = "administration"
        subject = "Заголовок баг-репорта отвечающий на вопрос 'Что? Где? Когда?'"
        description = "Описание баг-репорта"

        assert self.is_element_present(*BagReportLocators.SELECT_CATEGORY), "mat-7. Can't find select bottom"
        select = Select(self.browser.find_element(*BagReportLocators.SELECT_CATEGORY))
        select.select_by_visible_text(category)
        assert self.is_element_present(*BagReportLocators.SUBJECT), "mat-8. Can't find text area for subject"
        self.browser.find_element(*BagReportLocators.SUBJECT).send_keys(subject)
        assert self.is_element_present(*BagReportLocators.DESCRIPTION), "mat-9. Can't find text area for description"
        self.browser.find_element(*BagReportLocators.DESCRIPTION).send_keys(description)

        assert self.is_element_present(*BagReportLocators.CREATE_PROJECT), "mat-10. No bottom to create a project"
        button = self.browser.find_element(*BagReportLocators.CREATE_PROJECT)
        button.click()
        assert self.is_not_element_present(*BagReportLocators.SPAM_RESULT), \
            "mat-11. System considers that it's a spam, wait a few minutes or change login."
        assert self.is_element_present(*BagReportLocators.RESULT), "mat-12. Task is not created"
