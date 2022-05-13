import pytest
from selenium import webdriver


# функция выбора параметров при запуске: окружение, язык и отключение браузера Chrome
def pytest_addoption(parser):
    # выбор окружения chrome or firefox
    parser.addoption('--browser_name', action='store', default='chrome',
                     help="Choose browser: chrome or firefox")
    # выбор языка
    parser.addoption('--language', action='store', default='en',
                     help="Choose your language(ru, en, ...)")

    # выбор отключения браузера Chrome
    parser.addoption('--headless', action='store', default=None,
                     help="Open a browser invisible, without GUI is used by default")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    language = request.config.getoption("language")
    headless = request.config.getoption('headless')
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        from selenium.webdriver.chrome.options import Options
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': language})
        if headless == 'true':
            options.add_argument('headless')
        browser = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", language)
        browser = webdriver.Firefox(firefox_profile=fp)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser  # поведение браузера в конце теста
    print("\nquit browser..")
    browser.quit()
