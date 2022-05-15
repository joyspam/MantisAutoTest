from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_PAGE = (By.CSS_SELECTOR, ".btn-corner .btn-xs:nth-child(1)")
    LOGIN = (By.NAME, "username")
    ENTER_LOGIN = (By.CSS_SELECTOR, ".width-40")
    PASSWORD = (By.NAME, "password")
    ENTER_PASSWORD = (By.CSS_SELECTOR, ".width-40")
    REG_OK = (By.CSS_SELECTOR, ".label.hidden-xs.label-default.arrowed")

    CHOOSE_PROJECT = (By.CSS_SELECTOR, ".btn.btn-primary.btn-sm .fa.fa-edit")
    CHOOSE_PROJECT_BUTTON = (By.CSS_SELECTOR, ".btn-round")


class BagReportLocators:
    SELECT_CATEGORY = (By.ID, "category_id")
    SUBJECT = (By.ID, "summary")
    DESCRIPTION = (By.ID, "description")
    CREATE_PROJECT = (By.CSS_SELECTOR, ".btn-round")
    RESULT = (By.CSS_SELECTOR, ".fa.fa-bars.ace-icon")
    RESULT_TASK_NAME = (By.TAG_NAME, "title")
    SPAM_RESULT = (By.CSS_SELECTOR, ".alert.alert-danger")



