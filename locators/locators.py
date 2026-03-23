from selenium.webdriver.common.by import By


class MainPageLocators:
    # Кнопка «Войти в аккаунт» в конструкторе (видна только неавторизованным)
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти в аккаунт']")

    # Ссылка «Личный Кабинет» в шапке (тег <a href="/account">)
    PERSONAL_ACCOUNT_LINK = (By.XPATH, "//a[@href='/account']")

    # Ссылка «Конструктор» в шапке (тег <a href="/">)
    CONSTRUCTOR_LINK = (By.XPATH, "//a[@href='/'][.//p[contains(@class,'AppHeader_header__linkText')]]")

    # Логотип Stellar Burgers в шапке (div-обёртка с классом header__logo)
    LOGO = (By.XPATH, "//div[contains(@class,'AppHeader_header__logo')]")

    # Вкладка «Булки» в конструкторе (кликабельный div с текстом внутри span)
    BUNS_TAB = (By.XPATH, "//div[contains(@class,'tab_tab')]//span[text()='Булки']")

    # Вкладка «Соусы» в конструкторе
    SAUCES_TAB = (By.XPATH, "//div[contains(@class,'tab_tab')]//span[text()='Соусы']")

    # Вкладка «Начинки» в конструкторе
    FILLINGS_TAB = (By.XPATH, "//div[contains(@class,'tab_tab')]//span[text()='Начинки']")

    # Заголовок раздела «Булки» в списке ингредиентов (h2)
    BUNS_HEADING = (By.XPATH, "//h2[text()='Булки']")

    # Заголовок раздела «Соусы» в списке ингредиентов (h2)
    SAUCES_HEADING = (By.XPATH, "//h2[text()='Соусы']")

    # Заголовок раздела «Начинки» в списке ингредиентов (h2)
    FILLINGS_HEADING = (By.XPATH, "//h2[text()='Начинки']")


class LoginPageLocators:
    # Поле ввода email на странице входа (первый fieldset, оба поля имеют name="name")
    EMAIL_INPUT = (By.XPATH, "//fieldset[1]//input")

    # Поле ввода пароля на странице входа (второй fieldset, name="Пароль")
    PASSWORD_INPUT = (By.XPATH, "//input[@name='Пароль']")

    # Кнопка «Войти» на странице входа
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")

    # Ссылка «Зарегистрироваться» на странице входа (класс Auth_link)
    REGISTER_LINK = (By.XPATH, "//a[@href='/register']")

    # Ссылка «Восстановить пароль» на странице входа
    FORGOT_PASSWORD_LINK = (By.XPATH, "//a[@href='/forgot-password']")


class RegisterPageLocators:
    # Поле «Имя» на странице регистрации (первый fieldset)
    NAME_INPUT = (By.XPATH, "//fieldset[1]//input")

    # Поле «Email» на странице регистрации (второй fieldset)
    EMAIL_INPUT = (By.XPATH, "//fieldset[2]//input")

    # Поле «Пароль» на странице регистрации (третий fieldset)
    PASSWORD_INPUT = (By.XPATH, "//fieldset[3]//input")

    # Кнопка «Зарегистрироваться»
    REGISTER_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']")

    # Ссылка «Войти» на странице регистрации (ведёт на /login)
    LOGIN_LINK = (By.XPATH, "//a[@href='/login']")

    # Сообщение об ошибке при некорректном пароле
    PASSWORD_ERROR = (By.XPATH, "//p[text()='Некорректный пароль']")


class ForgotPasswordPageLocators:
    # Ссылка «Войти» на странице восстановления пароля (ведёт на /login)
    LOGIN_LINK = (By.XPATH, "//a[@href='/login']")


class ProfilePageLocators:
    # Кнопка «Выйти» в боковом меню личного кабинета
    LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выход']")

