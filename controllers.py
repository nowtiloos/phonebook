from services import contact_manager
from tabulate import tabulate
from config import settings


def add_contact():
    name = input("Введите имя контакта: ")
    number = input("Введите номер телефона: ")


def find_contact():
    name = input("Введите имя контакта для поиска: ")


def delete_contact():
    name = input("Введите имя контакта для удаления: ")


def show_contacts(page_size=settings.PAGE_SIZE, sort_by=settings.SORT_BY):
    contacts: list[dict] = contact_manager(file=settings.FILE_NAME, mode="r")
    contacts.sort(key=lambda x: x[sort_by])
    total_pages: int = (len(contacts) + page_size - 1) // page_size
    current_page: int = 1

    while True:
        start = (current_page - 1) * page_size
        end = start + page_size
        current_page_data = contacts[start:end]

        table = tabulate(tabular_data=current_page_data, headers="keys", tablefmt="grid")
        print(table)

        user_input = input(f"Страница {current_page}/{total_pages}. Введите номер страницы или 'exit' для выхода: ")

        if user_input.lower() == 'exit':
            break

        try:
            page_number = int(user_input)
            if 1 <= page_number <= total_pages:
                current_page = page_number
            else:
                print(f"Invalid page number. Please enter a number between 1 and {total_pages}.")
        except ValueError:
            print("Invalid input. Please enter a valid page number or 'exit'.")
