from services import CsvExecutor, Paginator
from config import settings
from schemas import Contact


def add_contact():
    contact = Contact(name=input("Введите имя контакта: ").title(),
                      patronymic=input("Введите отчество контакта: ").title(),
                      surname=input("Введите фамилию контакта: ").title(),
                      organization=input("Введите название организации: ").title(),
                      work_phone=input("Введите рабочий номер телефона: "),
                      personal_phone=input("Введите личный номер телефона: "))
    executor: CsvExecutor = CsvExecutor(file=settings.FILE_NAME)
    executor.add_one(contact.model_dump())
    print(f"\nКонтакт добавлен в {settings.FILE_NAME}\n")


def find_contact():
    name = input("Введите имя контакта для поиска: ")


def delete_contact():
    name = input("Введите имя контакта для удаления: ")


def show_contacts(page_size=settings.PAGE_SIZE, sort_by=settings.SORT_BY) -> None:
    executor: CsvExecutor = CsvExecutor(file=settings.FILE_NAME)
    contacts: list[dict] = executor.read_data()

    paginator: Paginator = Paginator(data=contacts, page_size=page_size, sort_by=sort_by)
    total_pages = paginator.get_total_pages()
    current_page = 1

    while True:

        user_input = input(f"Страница {current_page}/{total_pages}. Введите номер страницы или 'exit' для выхода: ")
        if user_input.lower() == 'exit':
            break

        try:
            paginator.display_page(current_page)
            page_number = int(user_input)
            if 1 <= page_number <= total_pages:
                current_page = page_number
            else:
                print(f"ВНИМАНИЕ! >>> Некорректный номер страницы. Введите номер страницы от 1 до {total_pages}.")
        except ValueError:
            print("ВНИМАНИЕ! >>> Некорректный ввод. Введите номер страницы или 'exit' для выхода.")
