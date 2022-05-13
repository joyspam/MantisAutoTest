from .pages.base_page import BasePage


# проверка добавления задачи

class TestLoginFromMainPage:
    # добавление задачи
    def test_user_can_add_new_task(self, browser):
        link = "https://www.mantisbt.org/bugs/my_view_page.php"
        page = BasePage(browser,
                        link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page.open()  # открываем страницу
        page.go_to_login_page()  # авторизируемся
        page.go_to_choose_project()  # выполняем метод страницы — переходим на страницу логина
