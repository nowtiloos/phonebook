import functools


def return_to_menu_decorator(func):
    @functools.wraps(func)
    def wrapper():
        func()
        return_to_menu = input("Введите 'm' для возврата в главное меню: ")
        if return_to_menu.lower() == 'm':
            return True
        return False

    return wrapper
